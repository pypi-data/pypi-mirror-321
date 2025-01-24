from typing import Dict, List, Optional, Any
from reelscraper.utils import InstagramAPI, Extractor, LoggerManager


class ReelScraper:
    """
    [ReelScraper] provides methods to gather Instagram Reels data using composition of [InstagramAPI] and [Extractor].

    :param [timeout]: Connection timeout in seconds
    :param [proxy]: Proxy string or None
    :param [logger_manager]: Optional [LoggerManager] for logging
    """

    def __init__(
        self,
        timeout: Optional[int] = None,
        proxy: Optional[str] = None,
        logger_manager: Optional[LoggerManager] = None,
    ) -> None:
        """
        Initializes [ReelScraper] with an [InstagramAPI] and an [Extractor].

        :param [timeout]: Connection timeout in seconds
        :param [proxy]: Proxy string or None (e.g., username:password@host:port)
        :param [logger_manager]: Optional instance of [LoggerManager]
        """
        self.api: InstagramAPI = InstagramAPI(timeout=timeout, proxy=proxy)
        self.extractor: Extractor = Extractor()
        self.logger_manager: Optional[LoggerManager] = logger_manager

    def _fetch_reels(
        self, username: str, max_id: Optional[str], max_retries: int
    ) -> Dict[str, Any]:
        """
        Retrieves first or subsequent batches of reels. Uses retry logic up to [max_retries].

        :param [username]: Instagram username
        :param [max_id]: Pagination identifier for further requests (None if fetching first batch)
        :param [max_retries]: Maximum number of allowed retries
        :return: Dictionary containing reels items and paging info
        :raises Exception: If data cannot be fetched within [max_retries] attempts
        """
        response: Optional[Dict[str, Any]] = None
        for retry in range(max_retries):
            if max_id is None:
                response = self.api.get_user_first_reels(username)
            else:
                response = self.api.get_user_paginated_reels(max_id, username)

            if response is not None:
                break

            if self.logger_manager is not None and retry >= 1:
                self.logger_manager.log_retry(retry, max_retries, username)

        if response is None:
            if self.logger_manager is not None:
                self.logger_manager.log_account_error(username)
            raise Exception(f"Error fetching reels for username: {username}")

        return response

    def get_user_reels(
        self, username: str, max_posts: int = 50, max_retries: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Collects user reels up to [max_posts], paginating through all available reels.

        :param [username]: Instagram username
        :param [max_posts]: Maximum number of reels to fetch (default: 50)
        :param [max_retries]: Maximum number of retry attempts for each batch
        :return: List of dictionaries with reel information
        :raises Exception: If initial reels cannot be fetched for [username]
        """
        if self.logger_manager is not None:
            self.logger_manager.log_account_begin(username)

        reels: List[Dict[str, Any]] = []

        # Fetch the first batch of reels
        first_reels_response: Dict[str, Any] = self._fetch_reels(
            username=username, max_id=None, max_retries=max_retries
        )
        first_reels: List[Dict[str, Any]] = first_reels_response["items"]
        paging_info: Dict[str, Any] = first_reels_response["paging_info"]

        for reel in first_reels:
            media: Dict[str, Any] = reel.get("media", {})
            reel_info: Optional[Dict[str, Any]] = self.extractor.extract_reel_info(
                media
            )
            if reel_info:
                reels.append(reel_info)
            if len(reels) >= max_posts:
                if self.logger_manager is not None:
                    self.logger_manager.log_account_success(username, len(reels))
                return reels

        if self.logger_manager is not None:
            self.logger_manager.log_reels_scraped(username, len(reels))

        # Paginate while more reels are available
        while paging_info.get("more_available", False):
            max_id: str = paging_info.get("max_id", "")
            paginated_reels_response: Dict[str, Any] = self._fetch_reels(
                username=username, max_id=max_id, max_retries=max_retries
            )
            paginated_reels: List[Dict[str, Any]] = paginated_reels_response["items"]

            for reel in paginated_reels:
                media: Dict[str, Any] = reel.get("media", {})
                reel_info: Optional[Dict[str, Any]] = self.extractor.extract_reel_info(
                    media
                )
                if reel_info:
                    reels.append(reel_info)
                if len(reels) >= max_posts:
                    if self.logger_manager is not None:
                        self.logger_manager.log_account_success(username, len(reels))
                    return reels

            if self.logger_manager is not None:
                self.logger_manager.log_reels_scraped(username, len(reels))

            paging_info = paginated_reels_response["paging_info"]

        if self.logger_manager is not None:
            self.logger_manager.log_account_success(username, len(reels))

        return reels
