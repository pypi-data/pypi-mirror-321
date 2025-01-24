"""**Document Transformers** are classes to transform Documents.

**Document Transformers** usually used to transform a lot of Documents in a single run.

**Class hierarchy:**

.. code-block::

    BaseDocumentTransformer --> <name>  # Examples: DoctranQATransformer, DoctranTextTranslator

**Main helpers:**

.. code-block::

    Document
"""  # noqa: E501

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.document_transformers.beautiful_soup_transformer import (
        BeautifulSoupTransformer,
    )
    from aibaba_ai_community.document_transformers.doctran_text_extract import (
        DoctranPropertyExtractor,
    )
    from aibaba_ai_community.document_transformers.doctran_text_qa import (
        DoctranQATransformer,
    )
    from aibaba_ai_community.document_transformers.doctran_text_translate import (
        DoctranTextTranslator,
    )
    from aibaba_ai_community.document_transformers.embeddings_redundant_filter import (
        EmbeddingsClusteringFilter,
        EmbeddingsRedundantFilter,
        get_stateful_documents,
    )
    from aibaba_ai_community.document_transformers.google_translate import (
        GoogleTranslateTransformer,
    )
    from aibaba_ai_community.document_transformers.html2text import (
        Html2TextTransformer,
    )
    from aibaba_ai_community.document_transformers.long_context_reorder import (
        LongContextReorder,
    )
    from aibaba_ai_community.document_transformers.markdownify import (
        MarkdownifyTransformer,
    )
    from aibaba_ai_community.document_transformers.nuclia_text_transform import (
        NucliaTextTransformer,
    )
    from aibaba_ai_community.document_transformers.openai_functions import (
        OpenAIMetadataTagger,
    )

__all__ = [
    "BeautifulSoupTransformer",
    "DoctranPropertyExtractor",
    "DoctranQATransformer",
    "DoctranTextTranslator",
    "EmbeddingsClusteringFilter",
    "EmbeddingsRedundantFilter",
    "GoogleTranslateTransformer",
    "Html2TextTransformer",
    "LongContextReorder",
    "MarkdownifyTransformer",
    "NucliaTextTransformer",
    "OpenAIMetadataTagger",
    "get_stateful_documents",
]

_module_lookup = {
    "BeautifulSoupTransformer": "aibaba_ai_community.document_transformers.beautiful_soup_transformer",  # noqa: E501
    "DoctranPropertyExtractor": "aibaba_ai_community.document_transformers.doctran_text_extract",  # noqa: E501
    "DoctranQATransformer": "aibaba_ai_community.document_transformers.doctran_text_qa",
    "DoctranTextTranslator": "aibaba_ai_community.document_transformers.doctran_text_translate",  # noqa: E501
    "EmbeddingsClusteringFilter": "aibaba_ai_community.document_transformers.embeddings_redundant_filter",  # noqa: E501
    "EmbeddingsRedundantFilter": "aibaba_ai_community.document_transformers.embeddings_redundant_filter",  # noqa: E501
    "GoogleTranslateTransformer": "aibaba_ai_community.document_transformers.google_translate",  # noqa: E501
    "Html2TextTransformer": "aibaba_ai_community.document_transformers.html2text",
    "LongContextReorder": "aibaba_ai_community.document_transformers.long_context_reorder",  # noqa: E501
    "MarkdownifyTransformer": "aibaba_ai_community.document_transformers.markdownify",
    "NucliaTextTransformer": "aibaba_ai_community.document_transformers.nuclia_text_transform",  # noqa: E501
    "OpenAIMetadataTagger": "aibaba_ai_community.document_transformers.openai_functions",  # noqa: E501
    "get_stateful_documents": "aibaba_ai_community.document_transformers.embeddings_redundant_filter",  # noqa: E501
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
