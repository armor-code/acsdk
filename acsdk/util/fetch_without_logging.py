from throttler import throttle as Limiter
import asyncio

# 100 requests/minute
@Limiter(rate_limit=100, period=60)
async def fetch(session, method, url, attempts=0, retry=None, **kwargs):
    response = await getattr(session, method)(url, ssl=False, **kwargs)

    if 400 <= response.status < 500 and (method == "get" or retry == True):
        print("Request `" + method.upper()  + " " +  url + "` failed with status code " + str(response.status))
        print("Retrying...")

        if attempts < 2:
            await asyncio.sleep(2 ** (attempts + 1))

            return await fetch(session, method, url, **kwargs, attempts=attempts + 1, retry=retry)
        else:
            raise Exception()
    else:
        return response
