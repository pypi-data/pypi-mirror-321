# stocks.py
from .base_tool import BaseTool
import yfinance as yf
from typing import Dict, Any, List, Optional

class StockPriceChecker(BaseTool):
    def __init__(
        self,
        default_symbol: str = "AAPL",  # Default stock symbol
        enable_historical_data: bool = True,  # Enable historical data
        enable_multiple_symbols: bool = True,  # Enable multiple stocks
        enable_metrics: bool = True,  # Enable additional metrics (e.g., volume, market cap)
    ):
        """
        Initialize the StockPriceChecker tool with customizable options.

        Args:
            default_symbol (str): Default stock symbol (e.g., "AAPL").
            enable_historical_data (bool): Enable fetching historical data.
            enable_multiple_symbols (bool): Enable fetching data for multiple stocks.
            enable_metrics (bool): Enable additional metrics like volume and market cap.
        """
        super().__init__(
            name="StockPriceChecker",
            description="Fetch real-time and historical stock prices and metrics."
        )
        self.default_symbol = default_symbol
        self.enable_historical_data = enable_historical_data
        self.enable_multiple_symbols = enable_multiple_symbols
        self.enable_metrics = enable_metrics

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