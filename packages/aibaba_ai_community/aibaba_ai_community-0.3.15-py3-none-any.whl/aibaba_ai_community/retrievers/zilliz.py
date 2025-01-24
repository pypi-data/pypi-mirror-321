import warnings
from typing import Any, Dict, List, Optional

from alibaba_ai_core.callbacks import CallbackManagerForRetrieverRun
from alibaba_ai_core.documents import Document
from alibaba_ai_core.embeddings import Embeddings
from alibaba_ai_core.retrievers import BaseRetriever
from pydantic import model_validator

from aibaba_ai_community.vectorstores.zilliz import Zilliz

# TODO: Update to ZillizClient + Hybrid Search when available


class ZillizRetriever(BaseRetriever):
    """`Zilliz API` retriever."""

    embedding_function: Embeddings
    """The underlying embedding function from which documents will be retrieved."""
    collection_name: str = "AI Agents ForceCollection"
    """The name of the collection in Zilliz."""
    connection_args: Optional[Dict[str, Any]] = None
    """The connection arguments for the Zilliz client."""
    consistency_level: str = "Session"
    """The consistency level for the Zilliz client."""
    search_params: Optional[dict] = None
    """The search parameters for the Zilliz client."""
    store: Zilliz
    """The underlying Zilliz store."""
    retriever: BaseRetriever
    """The underlying retriever."""

    @model_validator(mode="before")
    @classmethod
    def create_client(cls, values: dict) -> Any:
        values["store"] = Zilliz(
            values["embedding_function"],
            values["collection_name"],
            values["connection_args"],
            values["consistency_level"],
        )
        values["retriever"] = values["store"].as_retriever(
            search_kwargs={"param": values["search_params"]}
        )
        return values

    def add_texts(
        self, texts: List[str], metadatas: Optional[List[dict]] = None
    ) -> None:
        """Add text to the Zilliz store

        Args:
            texts (List[str]): The text
            metadatas (List[dict]): Metadata dicts, must line up with existing store
        """
        self.store.add_texts(texts, metadatas)

    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: CallbackManagerForRetrieverRun,
        **kwargs: Any,
    ) -> List[Document]:
        return self.retriever.invoke(
            query, run_manager=run_manager.get_child(), **kwargs
        )


def ZillizRetreiver(*args: Any, **kwargs: Any) -> ZillizRetriever:
    """Deprecated ZillizRetreiver.

    Please use ZillizRetriever ('i' before 'e') instead.

    Args:
        *args:
        **kwargs:

    Returns:
        ZillizRetriever
    """
    warnings.warn(
        "ZillizRetreiver will be deprecated in the future. "
        "Please use ZillizRetriever ('i' before 'e') instead.",
        DeprecationWarning,
    )
    return ZillizRetriever(*args, **kwargs)
