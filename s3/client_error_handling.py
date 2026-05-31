import asyncio
from fastmcp import Client


async def call_and_print(client, name, args):
    print(f"\n--- Tool call: {name} {args}")

    try:
        result = await client.call_tool(name, args)
        print("Result:", result.data)

    except Exception as e:
        print("Error type:", type(e).__name__)
        print(e.args[0])


async def main():
    client = Client("./server_error_handling.py")

    async with client:
        # result = await client.call_tool("divide", {"a": 5, "b": 2})
        # print(result)

        # result = await client.call_tool("divide", {"a": 2, "b": 0})
        # print(result)

        # Valid call
        await call_and_print(client, "divide", {"a": 5, "b": 2})

        # ToolError (division by zero)
        await call_and_print(client, "divide", {"a": 2, "b": 0})

        # Schema / validation error (non-numeric input)
        await call_and_print(client, "divide", {"a": "foo", "b": "bar"})


if __name__ == "__main__":
    asyncio.run(main())
