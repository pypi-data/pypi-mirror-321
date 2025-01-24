"""**Storage** is an implementation of key-value store.

Storage module provides implementations of various key-value stores that conform
to a simple key-value interface.

The primary goal of these storages is to support caching.


**Class hierarchy:**

.. code-block::

    BaseStore --> <name>Store  # Examples: MongoDBStore, RedisStore

"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.storage.astradb import (
        AstraDBByteStore,
        AstraDBStore,
    )
    from aibaba_ai_community.storage.cassandra import (
        CassandraByteStore,
    )
    from aibaba_ai_community.storage.mongodb import MongoDBByteStore, MongoDBStore
    from aibaba_ai_community.storage.redis import (
        RedisStore,
    )
    from aibaba_ai_community.storage.sql import (
        SQLStore,
    )
    from aibaba_ai_community.storage.upstash_redis import (
        UpstashRedisByteStore,
        UpstashRedisStore,
    )

__all__ = [
    "AstraDBByteStore",
    "AstraDBStore",
    "CassandraByteStore",
    "MongoDBStore",
    "MongoDBByteStore",
    "RedisStore",
    "SQLStore",
    "UpstashRedisByteStore",
    "UpstashRedisStore",
]

_module_lookup = {
    "AstraDBByteStore": "aibaba_ai_community.storage.astradb",
    "AstraDBStore": "aibaba_ai_community.storage.astradb",
    "CassandraByteStore": "aibaba_ai_community.storage.cassandra",
    "MongoDBStore": "aibaba_ai_community.storage.mongodb",
    "MongoDBByteStore": "aibaba_ai_community.storage.mongodb",
    "RedisStore": "aibaba_ai_community.storage.redis",
    "SQLStore": "aibaba_ai_community.storage.sql",
    "UpstashRedisByteStore": "aibaba_ai_community.storage.upstash_redis",
    "UpstashRedisStore": "aibaba_ai_community.storage.upstash_redis",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
