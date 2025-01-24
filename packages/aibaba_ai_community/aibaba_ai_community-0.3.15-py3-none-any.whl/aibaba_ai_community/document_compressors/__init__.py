import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.document_compressors.dashscope_rerank import (
        DashScopeRerank,
    )
    from aibaba_ai_community.document_compressors.flashrank_rerank import (
        FlashrankRerank,
    )
    from aibaba_ai_community.document_compressors.infinity_rerank import (
        InfinityRerank,
    )
    from aibaba_ai_community.document_compressors.jina_rerank import (
        JinaRerank,
    )
    from aibaba_ai_community.document_compressors.llmlingua_filter import (
        LLMLinguaCompressor,
    )
    from aibaba_ai_community.document_compressors.openvino_rerank import (
        OpenVINOReranker,
    )
    from aibaba_ai_community.document_compressors.rankllm_rerank import (
        RankLLMRerank,
    )
    from aibaba_ai_community.document_compressors.volcengine_rerank import (
        VolcengineRerank,
    )

_module_lookup = {
    "LLMLinguaCompressor": "aibaba_ai_community.document_compressors.llmlingua_filter",
    "OpenVINOReranker": "aibaba_ai_community.document_compressors.openvino_rerank",
    "JinaRerank": "aibaba_ai_community.document_compressors.jina_rerank",
    "RankLLMRerank": "aibaba_ai_community.document_compressors.rankllm_rerank",
    "FlashrankRerank": "aibaba_ai_community.document_compressors.flashrank_rerank",
    "DashScopeRerank": "aibaba_ai_community.document_compressors.dashscope_rerank",
    "VolcengineRerank": "aibaba_ai_community.document_compressors.volcengine_rerank",
    "InfinityRerank": "aibaba_ai_community.document_compressors.infinity_rerank",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "LLMLinguaCompressor",
    "OpenVINOReranker",
    "FlashrankRerank",
    "JinaRerank",
    "RankLLMRerank",
    "DashScopeRerank",
    "VolcengineRerank",
    "InfinityRerank",
]
