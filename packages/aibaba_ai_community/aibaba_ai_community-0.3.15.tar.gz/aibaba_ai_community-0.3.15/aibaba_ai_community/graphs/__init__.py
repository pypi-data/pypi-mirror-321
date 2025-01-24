"""**Graphs** provide a natural language interface to graph databases."""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.graphs.arangodb_graph import (
        ArangoGraph,
    )
    from aibaba_ai_community.graphs.falkordb_graph import (
        FalkorDBGraph,
    )
    from aibaba_ai_community.graphs.gremlin_graph import (
        GremlinGraph,
    )
    from aibaba_ai_community.graphs.hugegraph import (
        HugeGraph,
    )
    from aibaba_ai_community.graphs.kuzu_graph import (
        KuzuGraph,
    )
    from aibaba_ai_community.graphs.memgraph_graph import (
        MemgraphGraph,
    )
    from aibaba_ai_community.graphs.nebula_graph import (
        NebulaGraph,
    )
    from aibaba_ai_community.graphs.neo4j_graph import (
        Neo4jGraph,
    )
    from aibaba_ai_community.graphs.neptune_graph import (
        BaseNeptuneGraph,
        NeptuneAnalyticsGraph,
        NeptuneGraph,
    )
    from aibaba_ai_community.graphs.neptune_rdf_graph import (
        NeptuneRdfGraph,
    )
    from aibaba_ai_community.graphs.networkx_graph import (
        NetworkxEntityGraph,
    )
    from aibaba_ai_community.graphs.ontotext_graphdb_graph import (
        OntotextGraphDBGraph,
    )
    from aibaba_ai_community.graphs.rdf_graph import (
        RdfGraph,
    )
    from aibaba_ai_community.graphs.tigergraph_graph import (
        TigerGraph,
    )

__all__ = [
    "ArangoGraph",
    "FalkorDBGraph",
    "GremlinGraph",
    "HugeGraph",
    "KuzuGraph",
    "BaseNeptuneGraph",
    "MemgraphGraph",
    "NebulaGraph",
    "Neo4jGraph",
    "NeptuneGraph",
    "NeptuneRdfGraph",
    "NeptuneAnalyticsGraph",
    "NetworkxEntityGraph",
    "OntotextGraphDBGraph",
    "RdfGraph",
    "TigerGraph",
]

_module_lookup = {
    "ArangoGraph": "aibaba_ai_community.graphs.arangodb_graph",
    "FalkorDBGraph": "aibaba_ai_community.graphs.falkordb_graph",
    "GremlinGraph": "aibaba_ai_community.graphs.gremlin_graph",
    "HugeGraph": "aibaba_ai_community.graphs.hugegraph",
    "KuzuGraph": "aibaba_ai_community.graphs.kuzu_graph",
    "MemgraphGraph": "aibaba_ai_community.graphs.memgraph_graph",
    "NebulaGraph": "aibaba_ai_community.graphs.nebula_graph",
    "Neo4jGraph": "aibaba_ai_community.graphs.neo4j_graph",
    "BaseNeptuneGraph": "aibaba_ai_community.graphs.neptune_graph",
    "NeptuneAnalyticsGraph": "aibaba_ai_community.graphs.neptune_graph",
    "NeptuneGraph": "aibaba_ai_community.graphs.neptune_graph",
    "NeptuneRdfGraph": "aibaba_ai_community.graphs.neptune_rdf_graph",
    "NetworkxEntityGraph": "aibaba_ai_community.graphs.networkx_graph",
    "OntotextGraphDBGraph": "aibaba_ai_community.graphs.ontotext_graphdb_graph",
    "RdfGraph": "aibaba_ai_community.graphs.rdf_graph",
    "TigerGraph": "aibaba_ai_community.graphs.tigergraph_graph",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
