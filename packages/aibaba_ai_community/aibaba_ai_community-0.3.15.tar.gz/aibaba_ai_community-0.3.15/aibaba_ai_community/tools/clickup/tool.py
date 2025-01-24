"""
This tool allows agents to interact with the clickup library
and operate on a Clickup instance.
To use this tool, you must first set as environment variables:
    client_secret
    client_id
    code

Below is a sample script that uses the Clickup tool:

```python
from aibaba_ai_community.agent_toolkits.clickup.toolkit import ClickupToolkit
from aibaba_ai_community.utilities.clickup import ClickupAPIWrapper

clickup = ClickupAPIWrapper()
toolkit = ClickupToolkit.from_clickup_api_wrapper(clickup)
```
"""

from typing import Optional

from alibaba_ai_core.callbacks import CallbackManagerForToolRun
from alibaba_ai_core.tools import BaseTool
from pydantic import Field

from aibaba_ai_community.utilities.clickup import ClickupAPIWrapper


class ClickupAction(BaseTool):  # type: ignore[override]
    """Tool that queries the  Clickup API."""

    api_wrapper: ClickupAPIWrapper = Field(default_factory=ClickupAPIWrapper)
    mode: str
    name: str = ""
    description: str = ""

    def _run(
        self,
        instructions: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the  Clickup API to run an operation."""
        return self.api_wrapper.run(self.mode, instructions)
