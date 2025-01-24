"""**Retriever** class returns Documents given a text **query**.

It is more general than a vector store. A retriever does not need to be able to
store documents, only to return (or retrieve) it. Vector stores can be used as
the backbone of a retriever, but there are other types of retrievers as well.

**Class hierarchy:**

.. code-block::

    BaseRetriever --> <name>Retriever  # Examples: ArxivRetriever, MergerRetriever

**Main helpers:**

.. code-block::

    Document, Serializable, Callbacks,
    CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.retrievers.arcee import (
        ArceeRetriever,
    )
    from aibaba_ai_community.retrievers.arxiv import (
        ArxivRetriever,
    )
    from aibaba_ai_community.retrievers.asknews import (
        AskNewsRetriever,
    )
    from aibaba_ai_community.retrievers.azure_ai_search import (
        AzureAISearchRetriever,
        AzureCognitiveSearchRetriever,
    )
    from aibaba_ai_community.retrievers.bedrock import (
        AmazonKnowledgeBasesRetriever,
    )
    from aibaba_ai_community.retrievers.bm25 import (
        BM25Retriever,
    )
    from aibaba_ai_community.retrievers.breebs import (
        BreebsRetriever,
    )
    from aibaba_ai_community.retrievers.chaindesk import (
        ChaindeskRetriever,
    )
    from aibaba_ai_community.retrievers.chatgpt_plugin_retriever import (
        ChatGPTPluginRetriever,
    )
    from aibaba_ai_community.retrievers.cohere_rag_retriever import (
        CohereRagRetriever,
    )
    from aibaba_ai_community.retrievers.docarray import (
        DocArrayRetriever,
    )
    from aibaba_ai_community.retrievers.dria_index import (
        DriaRetriever,
    )
    from aibaba_ai_community.retrievers.elastic_search_bm25 import (
        ElasticSearchBM25Retriever,
    )
    from aibaba_ai_community.retrievers.embedchain import (
        EmbedchainRetriever,
    )
    from aibaba_ai_community.retrievers.google_cloud_documentai_warehouse import (
        GoogleDocumentAIWarehouseRetriever,
    )
    from aibaba_ai_community.retrievers.google_vertex_ai_search import (
        GoogleCloudEnterpriseSearchRetriever,
        GoogleVertexAIMultiTurnSearchRetriever,
        GoogleVertexAISearchRetriever,
    )
    from aibaba_ai_community.retrievers.kay import (
        KayAiRetriever,
    )
    from aibaba_ai_community.retrievers.kendra import (
        AmazonKendraRetriever,
    )
    from aibaba_ai_community.retrievers.knn import (
        KNNRetriever,
    )
    from aibaba_ai_community.retrievers.llama_index import (
        LlamaIndexGraphRetriever,
        LlamaIndexRetriever,
    )
    from aibaba_ai_community.retrievers.metal import (
        MetalRetriever,
    )
    from aibaba_ai_community.retrievers.milvus import (
        MilvusRetriever,
    )
    from aibaba_ai_community.retrievers.nanopq import NanoPQRetriever
    from aibaba_ai_community.retrievers.needle import NeedleRetriever
    from aibaba_ai_community.retrievers.outline import (
        OutlineRetriever,
    )
    from aibaba_ai_community.retrievers.pinecone_hybrid_search import (
        PineconeHybridSearchRetriever,
    )
    from aibaba_ai_community.retrievers.pubmed import (
        PubMedRetriever,
    )
    from aibaba_ai_community.retrievers.qdrant_sparse_vector_retriever import (
        QdrantSparseVectorRetriever,
    )
    from aibaba_ai_community.retrievers.rememberizer import (
        RememberizerRetriever,
    )
    from aibaba_ai_community.retrievers.remote_retriever import (
        RemoteAI Agents ForceRetriever,
    )
    from aibaba_ai_community.retrievers.svm import (
        SVMRetriever,
    )
    from aibaba_ai_community.retrievers.tavily_search_api import (
        TavilySearchAPIRetriever,
    )
    from aibaba_ai_community.retrievers.tfidf import (
        TFIDFRetriever,
    )
    from aibaba_ai_community.retrievers.thirdai_neuraldb import NeuralDBRetriever
    from aibaba_ai_community.retrievers.vespa_retriever import (
        VespaRetriever,
    )
    from aibaba_ai_community.retrievers.weaviate_hybrid_search import (
        WeaviateHybridSearchRetriever,
    )
    from aibaba_ai_community.retrievers.web_research import WebResearchRetriever
    from aibaba_ai_community.retrievers.wikipedia import (
        WikipediaRetriever,
    )
    from aibaba_ai_community.retrievers.you import (
        YouRetriever,
    )
    from aibaba_ai_community.retrievers.zep import (
        ZepRetriever,
    )
    from aibaba_ai_community.retrievers.zep_cloud import (
        ZepCloudRetriever,
    )
    from aibaba_ai_community.retrievers.zilliz import (
        ZillizRetriever,
    )


_module_lookup = {
    "AmazonKendraRetriever": "aibaba_ai_community.retrievers.kendra",
    "AmazonKnowledgeBasesRetriever": "aibaba_ai_community.retrievers.bedrock",
    "ArceeRetriever": "aibaba_ai_community.retrievers.arcee",
    "ArxivRetriever": "aibaba_ai_community.retrievers.arxiv",
    "AskNewsRetriever": "aibaba_ai_community.retrievers.asknews",
    "AzureAISearchRetriever": "aibaba_ai_community.retrievers.azure_ai_search",
    "AzureCognitiveSearchRetriever": "aibaba_ai_community.retrievers.azure_ai_search",
    "BM25Retriever": "aibaba_ai_community.retrievers.bm25",
    "BreebsRetriever": "aibaba_ai_community.retrievers.breebs",
    "ChaindeskRetriever": "aibaba_ai_community.retrievers.chaindesk",
    "ChatGPTPluginRetriever": "aibaba_ai_community.retrievers.chatgpt_plugin_retriever",
    "CohereRagRetriever": "aibaba_ai_community.retrievers.cohere_rag_retriever",
    "DocArrayRetriever": "aibaba_ai_community.retrievers.docarray",
    "DriaRetriever": "aibaba_ai_community.retrievers.dria_index",
    "ElasticSearchBM25Retriever": "aibaba_ai_community.retrievers.elastic_search_bm25",
    "EmbedchainRetriever": "aibaba_ai_community.retrievers.embedchain",
    "GoogleCloudEnterpriseSearchRetriever": "aibaba_ai_community.retrievers.google_vertex_ai_search",  # noqa: E501
    "GoogleDocumentAIWarehouseRetriever": "aibaba_ai_community.retrievers.google_cloud_documentai_warehouse",  # noqa: E501
    "GoogleVertexAIMultiTurnSearchRetriever": "aibaba_ai_community.retrievers.google_vertex_ai_search",  # noqa: E501
    "GoogleVertexAISearchRetriever": "aibaba_ai_community.retrievers.google_vertex_ai_search",  # noqa: E501
    "KNNRetriever": "aibaba_ai_community.retrievers.knn",
    "KayAiRetriever": "aibaba_ai_community.retrievers.kay",
    "LlamaIndexGraphRetriever": "aibaba_ai_community.retrievers.llama_index",
    "LlamaIndexRetriever": "aibaba_ai_community.retrievers.llama_index",
    "MetalRetriever": "aibaba_ai_community.retrievers.metal",
    "MilvusRetriever": "aibaba_ai_community.retrievers.milvus",
    "NanoPQRetriever": "aibaba_ai_community.retrievers.nanopq",
    "NeedleRetriever": "aibaba_ai_community.retrievers.needle",
    "OutlineRetriever": "aibaba_ai_community.retrievers.outline",
    "PineconeHybridSearchRetriever": "aibaba_ai_community.retrievers.pinecone_hybrid_search",  # noqa: E501
    "PubMedRetriever": "aibaba_ai_community.retrievers.pubmed",
    "QdrantSparseVectorRetriever": "aibaba_ai_community.retrievers.qdrant_sparse_vector_retriever",  # noqa: E501
    "RememberizerRetriever": "aibaba_ai_community.retrievers.rememberizer",
    "RemoteAI Agents ForceRetriever": "aibaba_ai_community.retrievers.remote_retriever",
    "SVMRetriever": "aibaba_ai_community.retrievers.svm",
    "TFIDFRetriever": "aibaba_ai_community.retrievers.tfidf",
    "TavilySearchAPIRetriever": "aibaba_ai_community.retrievers.tavily_search_api",
    "VespaRetriever": "aibaba_ai_community.retrievers.vespa_retriever",
    "WeaviateHybridSearchRetriever": "aibaba_ai_community.retrievers.weaviate_hybrid_search",  # noqa: E501
    "WebResearchRetriever": "aibaba_ai_community.retrievers.web_research",
    "WikipediaRetriever": "aibaba_ai_community.retrievers.wikipedia",
    "YouRetriever": "aibaba_ai_community.retrievers.you",
    "ZepRetriever": "aibaba_ai_community.retrievers.zep",
    "ZepCloudRetriever": "aibaba_ai_community.retrievers.zep_cloud",
    "ZillizRetriever": "aibaba_ai_community.retrievers.zilliz",
    "NeuralDBRetriever": "aibaba_ai_community.retrievers.thirdai_neuraldb",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "AmazonKendraRetriever",
    "AmazonKnowledgeBasesRetriever",
    "ArceeRetriever",
    "ArxivRetriever",
    "AskNewsRetriever",
    "AzureAISearchRetriever",
    "AzureCognitiveSearchRetriever",
    "BM25Retriever",
    "BreebsRetriever",
    "ChaindeskRetriever",
    "ChatGPTPluginRetriever",
    "CohereRagRetriever",
    "DocArrayRetriever",
    "DriaRetriever",
    "ElasticSearchBM25Retriever",
    "EmbedchainRetriever",
    "GoogleCloudEnterpriseSearchRetriever",
    "GoogleDocumentAIWarehouseRetriever",
    "GoogleVertexAIMultiTurnSearchRetriever",
    "GoogleVertexAISearchRetriever",
    "KayAiRetriever",
    "KNNRetriever",
    "LlamaIndexGraphRetriever",
    "LlamaIndexRetriever",
    "MetalRetriever",
    "MilvusRetriever",
    "NanoPQRetriever",
    "NeedleRetriever",
    "NeuralDBRetriever",
    "OutlineRetriever",
    "PineconeHybridSearchRetriever",
    "PubMedRetriever",
    "QdrantSparseVectorRetriever",
    "RememberizerRetriever",
    "RemoteAI Agents ForceRetriever",
    "SVMRetriever",
    "TavilySearchAPIRetriever",
    "TFIDFRetriever",
    "VespaRetriever",
    "WeaviateHybridSearchRetriever",
    "WebResearchRetriever",
    "WikipediaRetriever",
    "YouRetriever",
    "ZepRetriever",
    "ZepCloudRetriever",
    "ZillizRetriever",
]
