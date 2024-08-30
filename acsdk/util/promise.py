import asyncio
import inspect
from itertools import chain
import signal
from typing import Iterable
from asyncstdlib import filter as afilter, list as alist, reduce


class Promise:
    @staticmethod
    async def map_series(tasks, initial=None):
        return [await task(initial) for task in tasks]

    @staticmethod
    async def reduce_series(tasks, initial=None):
        async def reducer(current, next):
            if inspect.isasyncgen(current):
                return next(await alist(current))
            elif inspect.iscoroutine(current):
                result = await current

                # while inspect.iscoroutine(result) or callable(result):
                #    if callable(result):
                #        result = result()
                #
                #    result = await result

                if isinstance(result, tuple):
                    return next(*result)
                else:
                    return next(result)
            elif callable(current):
                if inspect.iscoroutinefunction(current):
                    current = await current()
                else:
                    current = current()

                return await next(current)
            else:
                if isinstance(current, tuple):
                    current = await Promise.map_parallel(current)

                    return next(*current)
                else:
                    return next(current)

        if initial is not None:
            tasks.insert(0, initial)

        # try:
        return await reduce(reducer, tasks)
        # except Exception as error:
        #    return

    @staticmethod
    async def map_parallel(iterable):
        async def identity(item=None):
            if item is None:
                item = []

            return item

        tasks = []

        for item in iterable:
            if isinstance(item, (list, tuple)):
                tasks.extend(
                    [item if inspect.iscoroutine(item) else identity(item) for item in chain.from_iterable(item)]
                )
            elif inspect.isasyncgen(item):
                tasks.append(
                    identity(
                        *[
                            item
                            async for item in afilter(
                                lambda item: not isinstance(item, Iterable) or len(item) > 0, item
                            )
                        ]
                    )
                )
            elif inspect.iscoroutine(item):
                tasks.append(item)
            else:
                tasks.append(identity(item))

        results = await asyncio.gather(*tasks)

        return results
