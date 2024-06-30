import asyncio
import time
import aiohttp

url= "http://localhost:8000/"

async def my_async_function():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()
            print("Received Response")
            return True

async def main():
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()
    await my_async_function()

start_time = time.time()
asyncio.run(main())
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

"""
Execution time: 20.060791730880737 seconds
"""