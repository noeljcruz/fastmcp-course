import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_arguments.py")

    async with client:
        result = await client.call_tool("find_products", {"query": ""})
        print(result)
        print()

        result = await client.call_tool("place_order", {"id": 3, "amount": 7})
        print(result)
        print(result.content[0].text)
        print()


if __name__ == "__main__":
    asyncio.run(main())