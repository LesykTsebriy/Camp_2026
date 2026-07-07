from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-hw")

@mcp.tool()
def get_forecast(city: str) -> str:
    """Return a short weather forecast for a city."""
    data = {"Kyiv": "18C, partly cloudy", "London": "12C, rain", "Tokyo": "24C, clear"}
    return data.get(city, f"No forecast available for {city}")

# TODO 1: add a get_air_quality(city) tool that returns an AQI string per city.
@mcp.tool()
def get_air_quality(city: str) -> str:
    """Return the air-quality index (AQI) for a city."""
    ...   # return e.g. {"Kyiv": "AQI 42 (good)"}.get(city, "unknown")

if __name__ == "__main__":
    mcp.run(transport="stdio")
