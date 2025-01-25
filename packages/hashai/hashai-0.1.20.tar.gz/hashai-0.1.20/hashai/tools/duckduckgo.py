# duckduckgo.py
from .base_tool import BaseTool
from duckduckgo_search import DDGS
from typing import Dict, Any, List, Optional

class DuckDuckGo(BaseTool):
    def __init__(
        self,
        enable_web_search: bool = True,
        enable_news_search: bool = False,
        enable_image_search: bool = False,
        enable_video_search: bool = False,
        region: Optional[str] = "wt-wt",  # Default to global region
        safesearch: str = "moderate",  # Options: "on", "moderate", "off"
        time_range: Optional[str] = None,  # Options: "d", "w", "m", "y"
    ):
        """
        Initialize the DuckDuckGo tool with customizable search options.

        Args:
            enable_web_search (bool): Enable web search functionality.
            enable_news_search (bool): Enable news search functionality.
            enable_image_search (bool): Enable image search functionality.
            enable_video_search (bool): Enable video search functionality.
            region (str): Region for search results (e.g., "us-en", "fr-fr").
            safesearch (str): Safesearch filter ("on", "moderate", "off").
            time_range (str): Time range for search results ("d", "w", "m", "y").
        """
        super().__init__(
            name="DuckDuckGo",
            description="Perform web, news, image, and video searches using DuckDuckGo."
        )
        self.enable_web_search = enable_web_search
        self.enable_news_search = enable_news_search
        self.enable_image_search = enable_image_search
        self.enable_video_search = enable_video_search
        self.region = region
        self.safesearch = safesearch
        self.time_range = time_range

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a search using DuckDuckGo based on the provided input.

        Args:
            input_data (Dict[str, Any]): Input data containing the query and optional parameters.

        Returns:
            Dict[str, Any]: Search results for the requested types.
        """
        query = input_data.get("query", "")
        max_results = input_data.get("max_results", 5)  # Default to 5 results
        region = input_data.get("region", self.region)
        safesearch = input_data.get("safesearch", self.safesearch)
        time_range = input_data.get("time_range", self.time_range)

        results = {}

        # Perform web search
        if self.enable_web_search:
            results["web"] = self._perform_search(
                query, max_results, region, safesearch, time_range, search_type="text"
            )

        # Perform news search
        if self.enable_news_search:
            results["news"] = self._perform_search(
                query, max_results, region, safesearch, time_range, search_type="news"
            )

        # Perform image search
        if self.enable_image_search:
            results["images"] = self._perform_search(
                query, max_results, region, safesearch, time_range, search_type="images"
            )

        # Perform video search
        if self.enable_video_search:
            results["videos"] = self._perform_search(
                query, max_results, region, safesearch, time_range, search_type="videos"
            )

        return results

    def _perform_search(
        self,
        query: str,
        max_results: int,
        region: str,
        safesearch: str,
        time_range: Optional[str],
        search_type: str,
    ) -> List[Dict[str, Any]]:
        """
        Perform a search using DuckDuckGo.

        Args:
            query (str): The search query.
            max_results (int): Maximum number of results to return.
            region (str): Region for search results.
            safesearch (str): Safesearch filter.
            time_range (Optional[str]): Time range for search results.
            search_type (str): Type of search ("text", "news", "images", "videos").

        Returns:
            List[Dict[str, Any]]: List of search results.
        """
        with DDGS() as ddgs:
            if search_type == "text":
                return list(
                    ddgs.text(
                        keywords=query,
                        max_results=max_results,
                        region=region,
                        safesearch=safesearch,
                        timelimit=time_range,
                    )
                )
            elif search_type == "news":
                return list(
                    ddgs.news(
                        keywords=query,
                        max_results=max_results,
                        region=region,
                        safesearch=safesearch,
                        timelimit=time_range,
                    )
                )
            elif search_type == "images":
                return list(
                    ddgs.images(
                        keywords=query,
                        max_results=max_results,
                        region=region,
                        safesearch=safesearch,
                        timelimit=time_range,
                    )
                )
            elif search_type == "videos":
                return list(
                    ddgs.videos(
                        keywords=query,
                        max_results=max_results,
                        region=region,
                        safesearch=safesearch,
                        timelimit=time_range,
                    )
                )
            else:
                raise ValueError(f"Unsupported search type: {search_type}")