import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_decorator.py")

    async with client:
        result = await client.call_tool("find_products", {"query": ""})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
    