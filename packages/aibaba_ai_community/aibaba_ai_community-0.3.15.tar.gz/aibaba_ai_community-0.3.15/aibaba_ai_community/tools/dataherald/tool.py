"""Tool for the Dataherald Hosted API"""

from typing import Optional, Type

from alibaba_ai_core.callbacks import CallbackManagerForToolRun
from alibaba_ai_core.tools import BaseTool
from pydantic import BaseModel, Field

from aibaba_ai_community.utilities.dataherald import DataheraldAPIWrapper


class DataheraldTextToSQLInput(BaseModel):
    prompt: str = Field(
        description="Natural language query to be translated to a SQL query."
    )


class DataheraldTextToSQL(BaseTool):  # type: ignore[override, override]
    """Tool that queries using the Dataherald SDK."""

    name: str = "dataherald"
    description: str = (
        "A wrapper around Dataherald. "
        "Text to SQL. "
        "Input should be a prompt and an existing db_connection_id"
    )
    api_wrapper: DataheraldAPIWrapper
    args_schema: Type[BaseModel] = DataheraldTextToSQLInput

    def _run(
        self,
        prompt: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Dataherald tool."""
        return self.api_wrapper.run(prompt)
