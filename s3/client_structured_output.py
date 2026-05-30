import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_structured_output.py")

    async with client:
        print("\n------------ add ------------")
        result = await client.call_tool("add", {"a": 2, "b": 5})
        print(result)

        print("\n------------ get_user ------------")
        result = await client.call_tool("get_user")
        print(result)

        print("\n------------ get_user_model ------------")
        result = await client.call_tool("get_user_model")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
