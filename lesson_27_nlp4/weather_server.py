# weather_server.py  --  run as: python weather_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_forecast(city: str) -> str:
    """Return a short weather forecast for a city."""
    data = {"Kyiv": "18C, partly cloudy",
            "London": "12C, rain",
            "Tokyo": "24C, clear"}
    return data.get(city, f"No forecast available for {city}")

@mcp.resource("config://cities")
def supported_cities() -> str:
    """The cities this server has data for."""
    return "Kyiv, London, Tokyo"

if __name__ == "__main__":
    mcp.run(transport="stdio")   # talk over stdin/stdout as a subprocess
