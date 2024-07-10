from pprint import pformat as pprint
from throttler import throttle as Limiter
import asyncio
import json
import re

def flush(buffer, callback):
    for x in range(0, len(buffer)):
        if x % 2 == 0:
            callback("--> " + "\n--> ".join(buffer[x]))
        else:
            callback("\n<-- " + "\n<-- ".join(buffer[x]) + "\n")


async def attempt_parse(response):
    array_buffer = response.read()

    body = None

    content_type = response.headers.get("Content-Type")
    content_length = response.headers.get("Content-Length")

    if content_type is None and int(content_length) > 0:
        body = (await array_buffer).decode("utf8")

        if re.search(r'[^\r\n\x20-\x7E]', body):
            content_type = "text/plain"

    if content_type is not None and content_type.endswith("json"):
        try:
            body = body or json.loads((await array_buffer).decode("utf8"))
        except:
            pass
    elif content_type is not None and content_type.startswith("text") and not content_type.endswith("xml"):
        body = body or (await array_buffer).decode("utf8")

    return body


# 100 requests/minute
@Limiter(rate_limit=100, period=60)
async def fetch(session, method, url, debug=True, attempts=0, **kwargs):
    headers = kwargs.get("headers")
    body = kwargs.get("body", kwargs.get("json"))

    request_buffer = []

    if debug == True:
        request_buffer.append(method.upper() + " " + url)

    if headers is not None and headers.get("Content-Type") is not None:
        if debug == True:
            for header in ["Content-Type"]:
                if headers[header] is not None:
                    request_buffer.append(header + ": " + headers[header])

        if headers.get("Content-Type").endswith("json"):
            if debug == True:
                request_buffer.extend(pprint(body).splitlines(body))

            body = json.dumps(body)

    response_buffer = []

    try:
        # XXX: Remove `ssl=False``
        response = await getattr(session, method)(url, **kwargs, ssl=False)

        if debug == True:
            response_buffer.append("HTTP " + str(response.status))  # + " " + response.status_text)

            for header in ["Content-Length", "Content-Type", "Server", "X-Powered-By"]:
                if response.headers.get(header) is not None:
                    response_buffer.append(header + ": " + response.headers.get(header))

        if 400 <= response.status < 500 and method == "get":
            response_buffer.append("Request `" + method.upper()  + " " +  url + "` failed with status code " + str(response.status)) # + " " + response.statusText).strip())

            body = await attempt_parse(response)

            if body is not None:
                response_buffer.extend(pprint(body).splitlines())

            response_buffer.append("Retrying...")

            flush([request_buffer, response_buffer], print)

            if attempts < 2:
                await asyncio.sleep(2 ** (attempts + 1))

                return await fetch(session, method, url, debug=True, attempts=attempts + 1, **kwargs)
            else:
                raise Exception()
        else:
            body = await attempt_parse(response)

            if body is not None:
                response_buffer.extend(pprint(body).splitlines())

            flush([request_buffer, response_buffer], print)

            return response

    except Exception as error:
        if debug == True:
            response_buffer.append(error)

        flush([request_buffer, response_buffer], print)

        raise error
