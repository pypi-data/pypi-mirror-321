import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.document_loaders.parsers.audio import (
        OpenAIWhisperParser,
    )
    from aibaba_ai_community.document_loaders.parsers.doc_intelligence import (
        AzureAIDocumentIntelligenceParser,
    )
    from aibaba_ai_community.document_loaders.parsers.docai import (
        DocAIParser,
    )
    from aibaba_ai_community.document_loaders.parsers.grobid import (
        GrobidParser,
    )
    from aibaba_ai_community.document_loaders.parsers.html import (
        BS4HTMLParser,
    )
    from aibaba_ai_community.document_loaders.parsers.language import (
        LanguageParser,
    )
    from aibaba_ai_community.document_loaders.parsers.pdf import (
        PDFMinerParser,
        PDFPlumberParser,
        PyMuPDFParser,
        PyPDFium2Parser,
        PyPDFParser,
    )
    from aibaba_ai_community.document_loaders.parsers.vsdx import (
        VsdxParser,
    )


_module_lookup = {
    "AzureAIDocumentIntelligenceParser": "aibaba_ai_community.document_loaders.parsers.doc_intelligence",  # noqa: E501
    "BS4HTMLParser": "aibaba_ai_community.document_loaders.parsers.html",
    "DocAIParser": "aibaba_ai_community.document_loaders.parsers.docai",
    "GrobidParser": "aibaba_ai_community.document_loaders.parsers.grobid",
    "LanguageParser": "aibaba_ai_community.document_loaders.parsers.language",
    "OpenAIWhisperParser": "aibaba_ai_community.document_loaders.parsers.audio",
    "PDFMinerParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PDFPlumberParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PyMuPDFParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PyPDFParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PyPDFium2Parser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "VsdxParser": "aibaba_ai_community.document_loaders.parsers.vsdx",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "AzureAIDocumentIntelligenceParser",
    "BS4HTMLParser",
    "DocAIParser",
    "GrobidParser",
    "LanguageParser",
    "OpenAIWhisperParser",
    "PDFMinerParser",
    "PDFPlumberParser",
    "PyMuPDFParser",
    "PyPDFParser",
    "PyPDFium2Parser",
    "VsdxParser",
]
