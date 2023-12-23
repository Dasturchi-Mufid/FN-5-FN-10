""" AsyncIO """

import asyncio
from collections import namedtuple

# async def select_user():
#     print(1)
#     await asyncio.sleep(2)

# async def select_auto():
#     print(2)
#     await asyncio.sleep(2)

# print(type(select_user))

# async def main():
#     ...
#     await select_user()
#     await select_auto()

# asyncio.run(main=main())

async def select_user():
    while True:
        print(1)
        await asyncio.sleep(1)

async def select_auto():
    while True:
        print(2)
        await asyncio.sleep(1)

async def main():
    asyncio.create_task(select_user())
    asyncio.create_task(select_auto())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()