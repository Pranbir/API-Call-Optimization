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
    tasks = [my_async_function() for _ in range(10)]
    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main())
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

"""
Execution time: 2.0161099433898926 seconds
"""