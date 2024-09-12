from throttler import throttle as Limiter
import asyncio


# 50 requests/minute
@Limiter(rate_limit=50, period=60)
async def fetch(session, method, url, attempts=0, retry=None, **kwargs):
    response = await getattr(session, method)(url, **kwargs)

    if 400 <= response.status < 500 and (method == "get" or retry is True):
        if attempts < 2:
            print("Request `" + method.upper() + " " + url + "` failed with status code " + str(response.status))
            print("Retrying...")

            await asyncio.sleep(2 ** (attempts + 1))

            return await fetch(session, method, url, **kwargs, attempts=attempts + 1, retry=retry)
        else:
            raise Exception()
    else:
        return response
