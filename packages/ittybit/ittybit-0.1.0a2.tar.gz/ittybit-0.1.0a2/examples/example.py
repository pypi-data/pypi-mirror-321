import os
import asyncio
from ittybit import AsyncIttybit

client = AsyncIttybit(
    api_key=os.environ.get("API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    automation = await client.automations.create()
    print(automation.data)


asyncio.run(main())