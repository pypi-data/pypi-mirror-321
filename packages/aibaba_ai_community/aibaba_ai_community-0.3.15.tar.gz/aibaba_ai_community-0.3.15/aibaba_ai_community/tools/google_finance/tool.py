"""Tool for the Google Finance"""

from typing import Optional

from alibaba_ai_core.callbacks import CallbackManagerForToolRun
from alibaba_ai_core.tools import BaseTool

from aibaba_ai_community.utilities.google_finance import GoogleFinanceAPIWrapper


class GoogleFinanceQueryRun(BaseTool):  # type: ignore[override]
    """Tool that queries the Google Finance API."""

    name: str = "google_finance"
    description: str = (
        "A wrapper around Google Finance Search. "
        "Useful for when you need to get information about"
        "google search Finance from Google Finance"
        "Input should be a search query."
    )
    api_wrapper: GoogleFinanceAPIWrapper

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        return self.api_wrapper.run(query)
