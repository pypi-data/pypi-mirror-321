"""Tool for the Merriam-Webster API."""

from typing import Optional

from alibaba_ai_core.callbacks import CallbackManagerForToolRun
from alibaba_ai_core.tools import BaseTool

from aibaba_ai_community.utilities.merriam_webster import MerriamWebsterAPIWrapper


class MerriamWebsterQueryRun(BaseTool):  # type: ignore[override]
    """Tool that searches the Merriam-Webster API."""

    name: str = "merriam_webster"
    description: str = (
        "A wrapper around Merriam-Webster. "
        "Useful for when you need to get the definition of a word."
        "Input should be the word you want the definition of."
    )
    api_wrapper: MerriamWebsterAPIWrapper

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Merriam-Webster tool."""
        return self.api_wrapper.run(query)
