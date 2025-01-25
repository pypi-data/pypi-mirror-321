# crypto.py
from .base_tool import BaseTool
import yfinance as yf
from typing import Dict, Any, List, Optional
from pydantic import Field

class CryptoPriceChecker(BaseTool):
    default_symbol: str = Field(default="BTC-USD", description="Default cryptocurrency symbol (e.g., 'BTC-USD').")
    enable_historical_data: bool = Field(default=True, description="Enable fetching historical data.")
    enable_multiple_symbols: bool = Field(default=True, description="Enable fetching data for multiple cryptocurrencies.")
    enable_metrics: bool = Field(default=True, description="Enable additional metrics like volume and market cap.")

    def __init__(self, **kwargs):
        super().__init__(
            name="CryptoPriceChecker",
            description="Fetch real-time and historical cryptocurrency prices and metrics.",
            **kwargs
        )

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the cryptocurrency price check based on the provided input.

        Args:
            input_data (Dict[str, Any]): Input data containing the symbol(s) and optional parameters.

        Returns:
            Dict[str, Any]: Cryptocurrency price and additional metrics.
        """
        symbols = input_data.get("symbols", [self.default_symbol])
        if isinstance(symbols, str):
            symbols = [symbols]  # Convert single symbol to list

        time_range = input_data.get("time_range", "1d")  # Default to 1 day
        metrics = input_data.get("metrics", ["price"])  # Default to price only

        results = {}

        for symbol in symbols:
            crypto = yf.Ticker(symbol)
            data = {}

            # Fetch real-time price
            if "price" in metrics:
                data["price"] = crypto.history(period=time_range)["Close"].iloc[-1]

            # Fetch historical data
            if self.enable_historical_data and "history" in metrics:
                data["history"] = crypto.history(period=time_range).to_dict()

            # Fetch additional metrics
            if self.enable_metrics:
                info = crypto.info
                if "volume" in metrics:
                    data["volume"] = info.get("volume24Hr")
                if "market_cap" in metrics:
                    data["market_cap"] = info.get("marketCap")

            results[symbol] = data

        return results