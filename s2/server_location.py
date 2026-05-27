from fastmcp import FastMCP

mcp = FastMCP("location")


@mcp.tool
def coordinates(city: str) -> str:
    """Latitude and longitude for the specified city"""
    return f"{city}: lat=10.0 lon=20.0"


if __name__ == "__main__":
    mcp.run()
