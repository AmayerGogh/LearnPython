import asyncio
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(3)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
print("结束了")