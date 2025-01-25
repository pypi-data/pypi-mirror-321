from .base_tool import BaseTool
from pydantic import Field
import yfinance as yf
from typing import List, Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StockPriceChecker(BaseTool):
    enable_historical_data: bool = Field(default=True, description="Enable fetching historical data.")
    enable_metrics: bool = Field(default=True, description="Enable additional metrics like volume and market cap.")
    llm: Optional[Any] = Field(None, description="The LLM instance to use for symbol extraction.")

    def __init__(self, **kwargs):
        super().__init__(
            name="StockPriceChecker",
            description="Fetch real-time and historical stock prices and metrics.",
            **kwargs
        )

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            query = input_data.get("query", "")
            symbols = self._extract_symbols(query)
            results = {}

            for symbol in symbols:
                stock = yf.Ticker(symbol)
                data = {}

                # Fetch real-time price
                history = stock.history(period="1d")
                if not history.empty:
                    data["price"] = history["Close"].iloc[-1]
                else:
                    data["price"] = "No data available"

                # Fetch additional metrics
                if self.enable_metrics:
                    info = stock.info
                    data["volume"] = info.get("volume", "No volume data available")
                    data["market_cap"] = info.get("marketCap", "No market cap data available")

                results[symbol] = data

            return results
        except Exception as e:
            return {"error": str(e)}

    def _extract_symbols(self, query: str) -> List[str]:
        """
        Use the LLM to extract stock symbols from the user's query.
        """
        if not self.llm:
            logger.error("LLM instance not available for symbol extraction.")
            return []

        # Create a prompt for the LLM
        prompt = f"""
        Extract the stock symbols from the following user query. Return the symbols as a comma-separated list (e.g., "AAPL,MSFT"). If no symbols are found, return "None".

        User Query: "{query}"
        """

        try:
            # Call the LLM to generate the response
            response = self.llm.generate(prompt=prompt)
            symbols = response.strip().replace('"', '').replace("'", "")

            # Parse the response into a list of symbols
            if symbols.lower() == "none":
                return []
            return [s.strip() for s in symbols.split(",")]
        except Exception as e:
            logger.error(f"Failed to extract symbols: {e}")
            return []