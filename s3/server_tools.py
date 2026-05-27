from fastmcp import FastMCP

mcp = FastMCP("server-tools")


@mcp.tool()
async def get_products(query: str) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [{"id": 2, "name": "Shoes"}, {"id": 5, "name": "Jeans"}]


if __name__ == "__main__":
    mcp.run()