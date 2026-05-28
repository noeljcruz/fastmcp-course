from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
from mcp.types import Icon

mcp = FastMCP("server-basics")


@mcp.tool(
    name="find_products",
    description="Retrieve products based on a query.",
    tags={"products", "catalog"},
    icons=[
        Icon(
            src="https://upload.wikimedia.org/wikipedia/commons/5/55/Magnifying_glass_icon.svg"
        )
    ],
    meta={"version": "0.5", "author": "catalog-management"},
)
async def get_products(
    query: Annotated[str, "URL of the image to process"],
) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [{"id": 2, "name": "Shoes"}, {"id": 5, "name": "Jeans"}]


@mcp.tool()
async def place_order(
    id: int,
    amount=Field(5, description="Amount of the product to be ordered", ge=3, le=10),
):
    return f"Order {id} successfully placed for {amount} items"


if __name__ == "__main__":
    mcp.run()
