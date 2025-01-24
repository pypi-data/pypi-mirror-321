"""**Vector store** stores embedded data and performs vector search.

One of the most common ways to store and search over unstructured data is to
embed it and store the resulting embedding vectors, and then query the store
and retrieve the data that are 'most similar' to the embedded query.

**Class hierarchy:**

.. code-block::

    VectorStore --> <name>  # Examples: Annoy, FAISS, Milvus

    BaseRetriever --> VectorStoreRetriever --> <name>Retriever  # Example: VespaRetriever

**Main helpers:**

.. code-block::

    Embeddings, Document
"""  # noqa: E501

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from alibaba_ai_core.vectorstores import (
        VectorStore,
    )

    from aibaba_ai_community.vectorstores.aerospike import (
        Aerospike,
    )
    from aibaba_ai_community.vectorstores.alibabacloud_opensearch import (
        AlibabaCloudOpenSearch,
        AlibabaCloudOpenSearchSettings,
    )
    from aibaba_ai_community.vectorstores.analyticdb import (
        AnalyticDB,
    )
    from aibaba_ai_community.vectorstores.annoy import (
        Annoy,
    )
    from aibaba_ai_community.vectorstores.apache_doris import (
        ApacheDoris,
    )
    from aibaba_ai_community.vectorstores.aperturedb import (
        ApertureDB,
    )
    from aibaba_ai_community.vectorstores.astradb import (
        AstraDB,
    )
    from aibaba_ai_community.vectorstores.atlas import (
        AtlasDB,
    )
    from aibaba_ai_community.vectorstores.awadb import (
        AwaDB,
    )
    from aibaba_ai_community.vectorstores.azure_cosmos_db import (
        AzureCosmosDBVectorSearch,
    )
    from aibaba_ai_community.vectorstores.azure_cosmos_db_no_sql import (
        AzureCosmosDBNoSqlVectorSearch,
    )
    from aibaba_ai_community.vectorstores.azuresearch import (
        AzureSearch,
    )
    from aibaba_ai_community.vectorstores.bagel import (
        Bagel,
    )
    from aibaba_ai_community.vectorstores.baiducloud_vector_search import (
        BESVectorStore,
    )
    from aibaba_ai_community.vectorstores.baiduvectordb import (
        BaiduVectorDB,
    )
    from aibaba_ai_community.vectorstores.bigquery_vector_search import (
        BigQueryVectorSearch,
    )
    from aibaba_ai_community.vectorstores.cassandra import (
        Cassandra,
    )
    from aibaba_ai_community.vectorstores.chroma import (
        Chroma,
    )
    from aibaba_ai_community.vectorstores.clarifai import (
        Clarifai,
    )
    from aibaba_ai_community.vectorstores.clickhouse import (
        Clickhouse,
        ClickhouseSettings,
    )
    from aibaba_ai_community.vectorstores.couchbase import (
        CouchbaseVectorStore,
    )
    from aibaba_ai_community.vectorstores.dashvector import (
        DashVector,
    )
    from aibaba_ai_community.vectorstores.databricks_vector_search import (
        DatabricksVectorSearch,
    )
    from aibaba_ai_community.vectorstores.deeplake import (
        DeepLake,
    )
    from aibaba_ai_community.vectorstores.dingo import (
        Dingo,
    )
    from aibaba_ai_community.vectorstores.docarray import (
        DocArrayHnswSearch,
        DocArrayInMemorySearch,
    )
    from aibaba_ai_community.vectorstores.documentdb import (
        DocumentDBVectorSearch,
    )
    from aibaba_ai_community.vectorstores.duckdb import (
        DuckDB,
    )
    from aibaba_ai_community.vectorstores.ecloud_vector_search import (
        EcloudESVectorStore,
    )
    from aibaba_ai_community.vectorstores.elastic_vector_search import (
        ElasticKnnSearch,
        ElasticVectorSearch,
    )
    from aibaba_ai_community.vectorstores.elasticsearch import (
        ElasticsearchStore,
    )
    from aibaba_ai_community.vectorstores.epsilla import (
        Epsilla,
    )
    from aibaba_ai_community.vectorstores.faiss import (
        FAISS,
    )
    from aibaba_ai_community.vectorstores.hanavector import (
        HanaDB,
    )
    from aibaba_ai_community.vectorstores.hologres import (
        Hologres,
    )
    from aibaba_ai_community.vectorstores.infinispanvs import (
        InfinispanVS,
    )
    from aibaba_ai_community.vectorstores.inmemory import (
        InMemoryVectorStore,
    )
    from aibaba_ai_community.vectorstores.kdbai import (
        KDBAI,
    )
    from aibaba_ai_community.vectorstores.kinetica import (
        DistanceStrategy,
        Kinetica,
        KineticaSettings,
    )
    from aibaba_ai_community.vectorstores.lancedb import (
        LanceDB,
    )
    from aibaba_ai_community.vectorstores.lantern import (
        Lantern,
    )
    from aibaba_ai_community.vectorstores.llm_rails import (
        LLMRails,
    )
    from aibaba_ai_community.vectorstores.manticore_search import (
        ManticoreSearch,
        ManticoreSearchSettings,
    )
    from aibaba_ai_community.vectorstores.marqo import (
        Marqo,
    )
    from aibaba_ai_community.vectorstores.matching_engine import (
        MatchingEngine,
    )
    from aibaba_ai_community.vectorstores.meilisearch import (
        Meilisearch,
    )
    from aibaba_ai_community.vectorstores.milvus import (
        Milvus,
    )
    from aibaba_ai_community.vectorstores.momento_vector_index import (
        MomentoVectorIndex,
    )
    from aibaba_ai_community.vectorstores.mongodb_atlas import (
        MongoDBAtlasVectorSearch,
    )
    from aibaba_ai_community.vectorstores.myscale import (
        MyScale,
        MyScaleSettings,
    )
    from aibaba_ai_community.vectorstores.neo4j_vector import (
        Neo4jVector,
    )
    from aibaba_ai_community.vectorstores.opensearch_vector_search import (
        OpenSearchVectorSearch,
    )
    from aibaba_ai_community.vectorstores.oraclevs import (
        OracleVS,
    )
    from aibaba_ai_community.vectorstores.pathway import (
        PathwayVectorClient,
    )
    from aibaba_ai_community.vectorstores.pgembedding import (
        PGEmbedding,
    )
    from aibaba_ai_community.vectorstores.pgvector import (
        PGVector,
    )
    from aibaba_ai_community.vectorstores.pinecone import (
        Pinecone,
    )
    from aibaba_ai_community.vectorstores.qdrant import (
        Qdrant,
    )
    from aibaba_ai_community.vectorstores.redis import (
        Redis,
    )
    from aibaba_ai_community.vectorstores.relyt import (
        Relyt,
    )
    from aibaba_ai_community.vectorstores.rocksetdb import (
        Rockset,
    )
    from aibaba_ai_community.vectorstores.scann import (
        ScaNN,
    )
    from aibaba_ai_community.vectorstores.semadb import (
        SemaDB,
    )
    from aibaba_ai_community.vectorstores.singlestoredb import (
        SingleStoreDB,
    )
    from aibaba_ai_community.vectorstores.sklearn import (
        SKLearnVectorStore,
    )
    from aibaba_ai_community.vectorstores.sqlitevec import (
        SQLiteVec,
    )
    from aibaba_ai_community.vectorstores.sqlitevss import (
        SQLiteVSS,
    )
    from aibaba_ai_community.vectorstores.starrocks import (
        StarRocks,
    )
    from aibaba_ai_community.vectorstores.supabase import (
        SupabaseVectorStore,
    )
    from aibaba_ai_community.vectorstores.surrealdb import (
        SurrealDBStore,
    )
    from aibaba_ai_community.vectorstores.tablestore import (
        TablestoreVectorStore,
    )
    from aibaba_ai_community.vectorstores.tair import (
        Tair,
    )
    from aibaba_ai_community.vectorstores.tencentvectordb import (
        TencentVectorDB,
    )
    from aibaba_ai_community.vectorstores.thirdai_neuraldb import (
        NeuralDBClientVectorStore,
        NeuralDBVectorStore,
    )
    from aibaba_ai_community.vectorstores.tidb_vector import (
        TiDBVectorStore,
    )
    from aibaba_ai_community.vectorstores.tigris import (
        Tigris,
    )
    from aibaba_ai_community.vectorstores.tiledb import (
        TileDB,
    )
    from aibaba_ai_community.vectorstores.timescalevector import (
        TimescaleVector,
    )
    from aibaba_ai_community.vectorstores.typesense import (
        Typesense,
    )
    from aibaba_ai_community.vectorstores.upstash import (
        UpstashVectorStore,
    )
    from aibaba_ai_community.vectorstores.usearch import (
        USearch,
    )
    from aibaba_ai_community.vectorstores.vald import (
        Vald,
    )
    from aibaba_ai_community.vectorstores.vdms import (
        VDMS,
    )
    from aibaba_ai_community.vectorstores.vearch import (
        Vearch,
    )
    from aibaba_ai_community.vectorstores.vectara import (
        Vectara,
    )
    from aibaba_ai_community.vectorstores.vespa import (
        VespaStore,
    )
    from aibaba_ai_community.vectorstores.vlite import (
        VLite,
    )
    from aibaba_ai_community.vectorstores.weaviate import (
        Weaviate,
    )
    from aibaba_ai_community.vectorstores.yellowbrick import (
        Yellowbrick,
    )
    from aibaba_ai_community.vectorstores.zep import (
        ZepVectorStore,
    )
    from aibaba_ai_community.vectorstores.zep_cloud import (
        ZepCloudVectorStore,
    )
    from aibaba_ai_community.vectorstores.zilliz import (
        Zilliz,
    )

__all__ = [
    "Aerospike",
    "AlibabaCloudOpenSearch",
    "AlibabaCloudOpenSearchSettings",
    "AnalyticDB",
    "Annoy",
    "ApacheDoris",
    "ApertureDB",
    "AstraDB",
    "AtlasDB",
    "AwaDB",
    "AzureCosmosDBNoSqlVectorSearch",
    "AzureCosmosDBVectorSearch",
    "AzureSearch",
    "BESVectorStore",
    "Bagel",
    "BaiduVectorDB",
    "BigQueryVectorSearch",
    "Cassandra",
    "Chroma",
    "Clarifai",
    "Clickhouse",
    "ClickhouseSettings",
    "CouchbaseVectorStore",
    "DashVector",
    "DatabricksVectorSearch",
    "DeepLake",
    "Dingo",
    "DistanceStrategy",
    "DocArrayHnswSearch",
    "DocArrayInMemorySearch",
    "DocumentDBVectorSearch",
    "DuckDB",
    "EcloudESVectorStore",
    "ElasticKnnSearch",
    "ElasticVectorSearch",
    "ElasticsearchStore",
    "Epsilla",
    "FAISS",
    "HanaDB",
    "Hologres",
    "InMemoryVectorStore",
    "InfinispanVS",
    "KDBAI",
    "Kinetica",
    "KineticaSettings",
    "LLMRails",
    "LanceDB",
    "Lantern",
    "ManticoreSearch",
    "ManticoreSearchSettings",
    "Marqo",
    "MatchingEngine",
    "Meilisearch",
    "Milvus",
    "MomentoVectorIndex",
    "MongoDBAtlasVectorSearch",
    "MyScale",
    "MyScaleSettings",
    "Neo4jVector",
    "NeuralDBClientVectorStore",
    "NeuralDBVectorStore",
    "OracleVS",
    "OpenSearchVectorSearch",
    "PGEmbedding",
    "PGVector",
    "PathwayVectorClient",
    "Pinecone",
    "Qdrant",
    "Redis",
    "Relyt",
    "Rockset",
    "SKLearnVectorStore",
    "SQLiteVec",
    "SQLiteVSS",
    "ScaNN",
    "SemaDB",
    "SingleStoreDB",
    "StarRocks",
    "SupabaseVectorStore",
    "SurrealDBStore",
    "TablestoreVectorStore",
    "Tair",
    "TencentVectorDB",
    "TiDBVectorStore",
    "Tigris",
    "TileDB",
    "TimescaleVector",
    "Typesense",
    "UpstashVectorStore",
    "USearch",
    "VDMS",
    "Vald",
    "Vearch",
    "Vectara",
    "VectorStore",
    "VespaStore",
    "VLite",
    "Weaviate",
    "Yellowbrick",
    "ZepVectorStore",
    "ZepCloudVectorStore",
    "Zilliz",
]

_module_lookup = {
    "Aerospike": "aibaba_ai_community.vectorstores.aerospike",
    "AlibabaCloudOpenSearch": "aibaba_ai_community.vectorstores.alibabacloud_opensearch",  # noqa: E501
    "AlibabaCloudOpenSearchSettings": "aibaba_ai_community.vectorstores.alibabacloud_opensearch",  # noqa: E501
    "AnalyticDB": "aibaba_ai_community.vectorstores.analyticdb",
    "Annoy": "aibaba_ai_community.vectorstores.annoy",
    "ApacheDoris": "aibaba_ai_community.vectorstores.apache_doris",
    "ApertureDB": "aibaba_ai_community.vectorstores.aperturedb",
    "AstraDB": "aibaba_ai_community.vectorstores.astradb",
    "AtlasDB": "aibaba_ai_community.vectorstores.atlas",
    "AwaDB": "aibaba_ai_community.vectorstores.awadb",
    "AzureCosmosDBNoSqlVectorSearch": "aibaba_ai_community.vectorstores.azure_cosmos_db_no_sql",  # noqa: E501
    "AzureCosmosDBVectorSearch": "aibaba_ai_community.vectorstores.azure_cosmos_db",  # noqa: E501
    "AzureSearch": "aibaba_ai_community.vectorstores.azuresearch",
    "BaiduVectorDB": "aibaba_ai_community.vectorstores.baiduvectordb",
    "BESVectorStore": "aibaba_ai_community.vectorstores.baiducloud_vector_search",
    "Bagel": "aibaba_ai_community.vectorstores.bageldb",
    "BigQueryVectorSearch": "aibaba_ai_community.vectorstores.bigquery_vector_search",
    "Cassandra": "aibaba_ai_community.vectorstores.cassandra",
    "Chroma": "aibaba_ai_community.vectorstores.chroma",
    "Clarifai": "aibaba_ai_community.vectorstores.clarifai",
    "Clickhouse": "aibaba_ai_community.vectorstores.clickhouse",
    "ClickhouseSettings": "aibaba_ai_community.vectorstores.clickhouse",
    "CouchbaseVectorStore": "aibaba_ai_community.vectorstores.couchbase",
    "DashVector": "aibaba_ai_community.vectorstores.dashvector",
    "DatabricksVectorSearch": "aibaba_ai_community.vectorstores.databricks_vector_search",  # noqa: E501
    "DeepLake": "aibaba_ai_community.vectorstores.deeplake",
    "Dingo": "aibaba_ai_community.vectorstores.dingo",
    "DistanceStrategy": "aibaba_ai_community.vectorstores.kinetica",
    "DocArrayHnswSearch": "aibaba_ai_community.vectorstores.docarray",
    "DocArrayInMemorySearch": "aibaba_ai_community.vectorstores.docarray",
    "DocumentDBVectorSearch": "aibaba_ai_community.vectorstores.documentdb",
    "DuckDB": "aibaba_ai_community.vectorstores.duckdb",
    "EcloudESVectorStore": "aibaba_ai_community.vectorstores.ecloud_vector_search",
    "ElasticKnnSearch": "aibaba_ai_community.vectorstores.elastic_vector_search",
    "ElasticVectorSearch": "aibaba_ai_community.vectorstores.elastic_vector_search",
    "ElasticsearchStore": "aibaba_ai_community.vectorstores.elasticsearch",
    "Epsilla": "aibaba_ai_community.vectorstores.epsilla",
    "FAISS": "aibaba_ai_community.vectorstores.faiss",
    "HanaDB": "aibaba_ai_community.vectorstores.hanavector",
    "Hologres": "aibaba_ai_community.vectorstores.hologres",
    "InfinispanVS": "aibaba_ai_community.vectorstores.infinispanvs",
    "InMemoryVectorStore": "aibaba_ai_community.vectorstores.inmemory",
    "KDBAI": "aibaba_ai_community.vectorstores.kdbai",
    "Kinetica": "aibaba_ai_community.vectorstores.kinetica",
    "KineticaSettings": "aibaba_ai_community.vectorstores.kinetica",
    "LLMRails": "aibaba_ai_community.vectorstores.llm_rails",
    "LanceDB": "aibaba_ai_community.vectorstores.lancedb",
    "Lantern": "aibaba_ai_community.vectorstores.lantern",
    "ManticoreSearch": "aibaba_ai_community.vectorstores.manticore_search",
    "ManticoreSearchSettings": "aibaba_ai_community.vectorstores.manticore_search",
    "Marqo": "aibaba_ai_community.vectorstores.marqo",
    "MatchingEngine": "aibaba_ai_community.vectorstores.matching_engine",
    "Meilisearch": "aibaba_ai_community.vectorstores.meilisearch",
    "Milvus": "aibaba_ai_community.vectorstores.milvus",
    "MomentoVectorIndex": "aibaba_ai_community.vectorstores.momento_vector_index",
    "MongoDBAtlasVectorSearch": "aibaba_ai_community.vectorstores.mongodb_atlas",
    "MyScale": "aibaba_ai_community.vectorstores.myscale",
    "MyScaleSettings": "aibaba_ai_community.vectorstores.myscale",
    "Neo4jVector": "aibaba_ai_community.vectorstores.neo4j_vector",
    "NeuralDBClientVectorStore": "aibaba_ai_community.vectorstores.thirdai_neuraldb",
    "NeuralDBVectorStore": "aibaba_ai_community.vectorstores.thirdai_neuraldb",
    "OpenSearchVectorSearch": "aibaba_ai_community.vectorstores.opensearch_vector_search",  # noqa: E501
    "OracleVS": "aibaba_ai_community.vectorstores.oraclevs",
    "PathwayVectorClient": "aibaba_ai_community.vectorstores.pathway",
    "PGEmbedding": "aibaba_ai_community.vectorstores.pgembedding",
    "PGVector": "aibaba_ai_community.vectorstores.pgvector",
    "Pinecone": "aibaba_ai_community.vectorstores.pinecone",
    "Qdrant": "aibaba_ai_community.vectorstores.qdrant",
    "Redis": "aibaba_ai_community.vectorstores.redis",
    "Relyt": "aibaba_ai_community.vectorstores.relyt",
    "Rockset": "aibaba_ai_community.vectorstores.rocksetdb",
    "SKLearnVectorStore": "aibaba_ai_community.vectorstores.sklearn",
    "SQLiteVec": "aibaba_ai_community.vectorstores.sqlitevec",
    "SQLiteVSS": "aibaba_ai_community.vectorstores.sqlitevss",
    "ScaNN": "aibaba_ai_community.vectorstores.scann",
    "SemaDB": "aibaba_ai_community.vectorstores.semadb",
    "SingleStoreDB": "aibaba_ai_community.vectorstores.singlestoredb",
    "StarRocks": "aibaba_ai_community.vectorstores.starrocks",
    "SupabaseVectorStore": "aibaba_ai_community.vectorstores.supabase",
    "SurrealDBStore": "aibaba_ai_community.vectorstores.surrealdb",
    "TablestoreVectorStore": "aibaba_ai_community.vectorstores.tablestore",
    "Tair": "aibaba_ai_community.vectorstores.tair",
    "TencentVectorDB": "aibaba_ai_community.vectorstores.tencentvectordb",
    "TiDBVectorStore": "aibaba_ai_community.vectorstores.tidb_vector",
    "Tigris": "aibaba_ai_community.vectorstores.tigris",
    "TileDB": "aibaba_ai_community.vectorstores.tiledb",
    "TimescaleVector": "aibaba_ai_community.vectorstores.timescalevector",
    "Typesense": "aibaba_ai_community.vectorstores.typesense",
    "UpstashVectorStore": "aibaba_ai_community.vectorstores.upstash",
    "USearch": "aibaba_ai_community.vectorstores.usearch",
    "Vald": "aibaba_ai_community.vectorstores.vald",
    "VDMS": "aibaba_ai_community.vectorstores.vdms",
    "Vearch": "aibaba_ai_community.vectorstores.vearch",
    "Vectara": "aibaba_ai_community.vectorstores.vectara",
    "VectorStore": "alibaba_ai_core.vectorstores",
    "VespaStore": "aibaba_ai_community.vectorstores.vespa",
    "VLite": "aibaba_ai_community.vectorstores.vlite",
    "Weaviate": "aibaba_ai_community.vectorstores.weaviate",
    "Yellowbrick": "aibaba_ai_community.vectorstores.yellowbrick",
    "ZepVectorStore": "aibaba_ai_community.vectorstores.zep",
    "ZepCloudVectorStore": "aibaba_ai_community.vectorstores.zep_cloud",
    "Zilliz": "aibaba_ai_community.vectorstores.zilliz",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
