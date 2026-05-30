import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_structured_output.py")

    async with client:
        tools = await client.list_tools()

        for tool in tools:
            print(f"\n------------ {tool.name} ------------")
            print("Output schema:")
            print(tool.outputSchema)


if __name__ == "__main__":
    asyncio.run(main())