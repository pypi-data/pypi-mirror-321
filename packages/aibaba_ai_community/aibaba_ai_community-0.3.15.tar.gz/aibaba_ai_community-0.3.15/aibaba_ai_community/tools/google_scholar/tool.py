"""Tool for the Google Scholar"""

from typing import Optional

from alibaba_ai_core.callbacks import CallbackManagerForToolRun
from alibaba_ai_core.tools import BaseTool

from aibaba_ai_community.utilities.google_scholar import GoogleScholarAPIWrapper


class GoogleScholarQueryRun(BaseTool):  # type: ignore[override]
    """Tool that queries the Google search API."""

    name: str = "google_scholar"
    description: str = (
        "A wrapper around Google Scholar Search. "
        "Useful for when you need to get information about"
        "research papers from Google Scholar"
        "Input should be a search query."
    )
    api_wrapper: GoogleScholarAPIWrapper

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        return self.api_wrapper.run(query)
