from preloaded import send_request
import asyncio
​
async def request_manager(n: int) -> str:
    tasks = [send_request() for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return ''.join(results)