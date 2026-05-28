import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_return_types.py")

    async with client:
        print("\n------------ get_info ------------")
        result = await client.call_tool("get_info")
        print(result)

        print("\n------------ get_sum ------------")
        result = await client.call_tool("get_sum")
        print(result)

        print("\n------------ get_chart ------------")
        result = await client.call_tool("get_chart")
        # print(result)
        for item in result.content:
            # print(item)
            print(type(item).__name__)

        print("\n------------ get_sum2 ------------")
        result = await client.call_tool("get_sum2")
        print(result)

        print("\n------------ get_chart_dict ------------")
        result = await client.call_tool("get_chart_dict")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
