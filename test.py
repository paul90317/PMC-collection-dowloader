import asyncio
import time
async def test():
    await asyncio.sleep(1)
    print(time.time())
tasks = [asyncio.ensure_future(test()) for _ in range(3)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
