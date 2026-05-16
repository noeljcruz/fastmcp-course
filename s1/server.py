from fastmcp import FastMCP


mcp = FastMCP()


@mcp.tool
def say_hello() -> str:
    """Says hello world"""
    return f"Hello World!!"


if __name__ == "__main__":
    mcp.run()

