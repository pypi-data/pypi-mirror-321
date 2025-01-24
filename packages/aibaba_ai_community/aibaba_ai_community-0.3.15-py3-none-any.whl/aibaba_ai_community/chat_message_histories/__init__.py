"""**Chat message history** stores a history of the message interactions in a chat.


**Class hierarchy:**

.. code-block::

    BaseChatMessageHistory --> <name>ChatMessageHistory  # Examples: FileChatMessageHistory, PostgresChatMessageHistory

**Main helpers:**

.. code-block::

    AIMessage, HumanMessage, BaseMessage

"""  # noqa: E501

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.chat_message_histories.astradb import (
        AstraDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.cassandra import (
        CassandraChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.cosmos_db import (
        CosmosDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.dynamodb import (
        DynamoDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.elasticsearch import (
        ElasticsearchChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.file import (
        FileChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.firestore import (
        FirestoreChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.in_memory import (
        ChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.kafka import (
        KafkaChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.momento import (
        MomentoChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.mongodb import (
        MongoDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.neo4j import (
        Neo4jChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.postgres import (
        PostgresChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.redis import (
        RedisChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.rocksetdb import (
        RocksetChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.singlestoredb import (
        SingleStoreDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.sql import (
        SQLChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.streamlit import (
        StreamlitChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.tidb import (
        TiDBChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.upstash_redis import (
        UpstashRedisChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.xata import (
        XataChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.zep import (
        ZepChatMessageHistory,
    )
    from aibaba_ai_community.chat_message_histories.zep_cloud import (
        ZepCloudChatMessageHistory,
    )

__all__ = [
    "AstraDBChatMessageHistory",
    "CassandraChatMessageHistory",
    "ChatMessageHistory",
    "CosmosDBChatMessageHistory",
    "DynamoDBChatMessageHistory",
    "ElasticsearchChatMessageHistory",
    "FileChatMessageHistory",
    "FirestoreChatMessageHistory",
    "MomentoChatMessageHistory",
    "MongoDBChatMessageHistory",
    "Neo4jChatMessageHistory",
    "PostgresChatMessageHistory",
    "RedisChatMessageHistory",
    "RocksetChatMessageHistory",
    "SQLChatMessageHistory",
    "SingleStoreDBChatMessageHistory",
    "StreamlitChatMessageHistory",
    "TiDBChatMessageHistory",
    "UpstashRedisChatMessageHistory",
    "XataChatMessageHistory",
    "ZepChatMessageHistory",
    "ZepCloudChatMessageHistory",
    "KafkaChatMessageHistory",
]

_module_lookup = {
    "AstraDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.astradb",
    "CassandraChatMessageHistory": "aibaba_ai_community.chat_message_histories.cassandra",  # noqa: E501
    "ChatMessageHistory": "aibaba_ai_community.chat_message_histories.in_memory",
    "CosmosDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.cosmos_db",  # noqa: E501
    "DynamoDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.dynamodb",
    "ElasticsearchChatMessageHistory": "aibaba_ai_community.chat_message_histories.elasticsearch",  # noqa: E501
    "FileChatMessageHistory": "aibaba_ai_community.chat_message_histories.file",
    "FirestoreChatMessageHistory": "aibaba_ai_community.chat_message_histories.firestore",  # noqa: E501
    "MomentoChatMessageHistory": "aibaba_ai_community.chat_message_histories.momento",
    "MongoDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.mongodb",
    "Neo4jChatMessageHistory": "aibaba_ai_community.chat_message_histories.neo4j",
    "PostgresChatMessageHistory": "aibaba_ai_community.chat_message_histories.postgres",
    "RedisChatMessageHistory": "aibaba_ai_community.chat_message_histories.redis",
    "RocksetChatMessageHistory": "aibaba_ai_community.chat_message_histories.rocksetdb",
    "SQLChatMessageHistory": "aibaba_ai_community.chat_message_histories.sql",
    "SingleStoreDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.singlestoredb",  # noqa: E501
    "StreamlitChatMessageHistory": "aibaba_ai_community.chat_message_histories.streamlit",  # noqa: E501
    "TiDBChatMessageHistory": "aibaba_ai_community.chat_message_histories.tidb",
    "UpstashRedisChatMessageHistory": "aibaba_ai_community.chat_message_histories.upstash_redis",  # noqa: E501
    "XataChatMessageHistory": "aibaba_ai_community.chat_message_histories.xata",
    "ZepChatMessageHistory": "aibaba_ai_community.chat_message_histories.zep",
    "ZepCloudChatMessageHistory": "aibaba_ai_community.chat_message_histories.zep_cloud",  # noqa: E501
    "KafkaChatMessageHistory": "aibaba_ai_community.chat_message_histories.kafka",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
