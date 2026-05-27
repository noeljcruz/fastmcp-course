from fastmcp import FastMCP
import asyncio
from fastmcp import Client


async def main():

    # server = FastMCP("in-memory-server")
    # client = Client(server)
    # print(client)

    client = Client("./server.py")

    async with client:
        print("Connected:", client.is_connected())

        # call known tool
        w = await client.call_tool("weather_lookup", {"city": "London"})
        print("Tool:", w.data)

        #read all resources
        rs = await client.list_resources()
        for r in rs:
            content = await client.read_resource(r.uri)
            for block in content:
                print("Resource:", getattr(block, "text", block))

        # call prompt
        p = await client.get_prompt("text_summarization", {"topic": "tutorial"})
        print("Prompt:", p.messages)
    
    print("Connected after block:", client.is_connected())

    
if __name__ == "__main__":
    asyncio.run(main())
