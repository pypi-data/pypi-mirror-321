# stocks.py
from .base_tool import BaseTool
import yfinance as yf
from typing import Dict, Any, List, Optional
from pydantic import Field

class StockPriceChecker(BaseTool):
    default_symbol: str = Field(default="AAPL", description="Default stock symbol (e.g., 'AAPL').")
    enable_historical_data: bool = Field(default=True, description="Enable fetching historical data.")
    enable_multiple_symbols: bool = Field(default=True, description="Enable fetching data for multiple stocks.")
    enable_metrics: bool = Field(default=True, description="Enable additional metrics like volume and market cap.")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the stock price check based on the provided input.

        Args:
            input_data (Dict[str, Any]): Input data containing the symbol(s) and optional parameters.

        Returns:
            Dict[str, Any]: Stock price and additional metrics.
        """
        symbols = input_data.get("symbols", [self.default_symbol])
        if isinstance(symbols, str):
            symbols = [symbols]  # Convert single symbol to list

        time_range = input_data.get("time_range", "1d")  # Default to 1 day
        metrics = input_data.get("metrics", ["price"])  # Default to price only

        results = {}

        for symbol in symbols:
            stock = yf.Ticker(symbol)
            data = {}

            # Fetch real-time price
            if "price" in metrics:
                data["price"] = stock.history(period=time_range)["Close"].iloc[-1]

            # Fetch historical data
            if self.enable_historical_data and "history" in metrics:
                data["history"] = stock.history(period=time_range).to_dict()

            # Fetch additional metrics
            if self.enable_metrics:
                info = stock.info
                if "volume" in metrics:
                    data["volume"] = info.get("volume")
                if "market_cap" in metrics:
                    data["market_cap"] = info.get("marketCap")
                if "dividends" in metrics:
                    data["dividends"] = info.get("dividendRate")
                if "pe_ratio" in metrics:
                    data["pe_ratio"] = info.get("trailingPE")

            results[symbol] = data

        return results