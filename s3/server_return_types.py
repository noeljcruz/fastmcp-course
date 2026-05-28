from fastmcp import FastMCP
from fastmcp.utilities.types import Image

mcp = FastMCP("server-return-types")


@mcp.tool()
async def get_info():
    return "Some info about this server"


@mcp.tool()
async def get_sum():
    return 4 + 5


@mcp.tool()
async def get_chart():
    return Image(path="./chart.png")


@mcp.tool()
async def get_sum2() -> int:
    return 4 + 5


@mcp.tool()
async def get_chart_dict():
    return {"file": Image(path="./chart.png")}


if __name__ == "__main__":
    mcp.run()
    