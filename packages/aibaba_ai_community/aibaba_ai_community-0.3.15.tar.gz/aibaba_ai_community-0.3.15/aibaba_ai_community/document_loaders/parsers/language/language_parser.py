from __future__ import annotations

from typing import Any, Dict, Iterator, Literal, Optional

from alibaba_ai_core.documents import Document

from aibaba_ai_community.document_loaders.base import BaseBlobParser
from aibaba_ai_community.document_loaders.blob_loaders import Blob
from aibaba_ai_community.document_loaders.parsers.language.c import CSegmenter
from aibaba_ai_community.document_loaders.parsers.language.cobol import CobolSegmenter
from aibaba_ai_community.document_loaders.parsers.language.cpp import CPPSegmenter
from aibaba_ai_community.document_loaders.parsers.language.csharp import CSharpSegmenter
from aibaba_ai_community.document_loaders.parsers.language.elixir import ElixirSegmenter
from aibaba_ai_community.document_loaders.parsers.language.go import GoSegmenter
from aibaba_ai_community.document_loaders.parsers.language.java import JavaSegmenter
from aibaba_ai_community.document_loaders.parsers.language.javascript import (
    JavaScriptSegmenter,
)
from aibaba_ai_community.document_loaders.parsers.language.kotlin import KotlinSegmenter
from aibaba_ai_community.document_loaders.parsers.language.lua import LuaSegmenter
from aibaba_ai_community.document_loaders.parsers.language.perl import PerlSegmenter
from aibaba_ai_community.document_loaders.parsers.language.php import PHPSegmenter
from aibaba_ai_community.document_loaders.parsers.language.python import PythonSegmenter
from aibaba_ai_community.document_loaders.parsers.language.ruby import RubySegmenter
from aibaba_ai_community.document_loaders.parsers.language.rust import RustSegmenter
from aibaba_ai_community.document_loaders.parsers.language.scala import ScalaSegmenter
from aibaba_ai_community.document_loaders.parsers.language.sql import SQLSegmenter
from aibaba_ai_community.document_loaders.parsers.language.typescript import (
    TypeScriptSegmenter,
)

LANGUAGE_EXTENSIONS: Dict[str, str] = {
    "py": "python",
    "js": "js",
    "cobol": "cobol",
    "c": "c",
    "cpp": "cpp",
    "cs": "csharp",
    "rb": "ruby",
    "scala": "scala",
    "rs": "rust",
    "go": "go",
    "kt": "kotlin",
    "lua": "lua",
    "pl": "perl",
    "ts": "ts",
    "java": "java",
    "php": "php",
    "ex": "elixir",
    "exs": "elixir",
    "sql": "sql",
}

LANGUAGE_SEGMENTERS: Dict[str, Any] = {
    "python": PythonSegmenter,
    "js": JavaScriptSegmenter,
    "cobol": CobolSegmenter,
    "c": CSegmenter,
    "cpp": CPPSegmenter,
    "csharp": CSharpSegmenter,
    "ruby": RubySegmenter,
    "rust": RustSegmenter,
    "scala": ScalaSegmenter,
    "go": GoSegmenter,
    "kotlin": KotlinSegmenter,
    "lua": LuaSegmenter,
    "perl": PerlSegmenter,
    "ts": TypeScriptSegmenter,
    "java": JavaSegmenter,
    "php": PHPSegmenter,
    "elixir": ElixirSegmenter,
    "sql": SQLSegmenter,
}

Language = Literal[
    "cpp",
    "go",
    "java",
    "kotlin",
    "js",
    "ts",
    "php",
    "proto",
    "python",
    "rst",
    "ruby",
    "rust",
    "scala",
    "markdown",
    "latex",
    "html",
    "sol",
    "csharp",
    "cobol",
    "c",
    "lua",
    "perl",
    "elixir",
    "sql",
]


class LanguageParser(BaseBlobParser):
    """Parse using the respective programming language syntax.

    Each top-level function and class in the code is loaded into separate documents.
    Furthermore, an extra document is generated, containing the remaining top-level code
    that excludes the already segmented functions and classes.

    This approach can potentially improve the accuracy of QA models over source code.

    The supported languages for code parsing are:

    - C: "c" (*)
    - C++: "cpp" (*)
    - C#: "csharp" (*)
    - COBOL: "cobol"
    - Elixir: "elixir"
    - Go: "go" (*)
    - Java: "java" (*)
    - JavaScript: "js" (requires package `esprima`)
    - Kotlin: "kotlin" (*)
    - Lua: "lua" (*)
    - Perl: "perl" (*)
    - Python: "python"
    - Ruby: "ruby" (*)
    - Rust: "rust" (*)
    - Scala: "scala" (*)
    - SQL: "sql" (*)
    - TypeScript: "ts" (*)

    Items marked with (*) require the packages `tree_sitter` and
    `tree_sitter_languages`. It is straightforward to add support for additional
    languages using `tree_sitter`, although this currently requires modifying Aibaba AI.

    The language used for parsing can be configured, along with the minimum number of
    lines required to activate the splitting based on syntax.

    If a language is not explicitly specified, `LanguageParser` will infer one from
    filename extensions, if present.

    Examples:

       .. code-block:: python

            from aibaba_ai_community.document_loaders.generic import GenericLoader
            from aibaba_ai_community.document_loaders.parsers import LanguageParser

            loader = GenericLoader.from_filesystem(
                "./code",
                glob="**/*",
                suffixes=[".py", ".js"],
                parser=LanguageParser()
            )
            docs = loader.load()

        Example instantiations to manually select the language:

        .. code-block:: python


            loader = GenericLoader.from_filesystem(
                "./code",
                glob="**/*",
                suffixes=[".py"],
                parser=LanguageParser(language="python")
            )

        Example instantiations to set number of lines threshold:

        .. code-block:: python

            loader = GenericLoader.from_filesystem(
                "./code",
                glob="**/*",
                suffixes=[".py"],
                parser=LanguageParser(parser_threshold=200)
            )
    """

    def __init__(self, language: Optional[Language] = None, parser_threshold: int = 0):
        """
        Language parser that split code using the respective language syntax.

        Args:
            language: If None (default), it will try to infer language from source.
            parser_threshold: Minimum lines needed to activate parsing (0 by default).
        """
        if language and language not in LANGUAGE_SEGMENTERS:
            raise Exception(f"No parser available for {language}")
        self.language = language
        self.parser_threshold = parser_threshold

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        code = blob.as_string()

        language = self.language or (
            LANGUAGE_EXTENSIONS.get(blob.source.rsplit(".", 1)[-1])
            if isinstance(blob.source, str)
            else None
        )

        if language is None:
            yield Document(
                page_content=code,
                metadata={
                    "source": blob.source,
                },
            )
            return

        if self.parser_threshold >= len(code.splitlines()):
            yield Document(
                page_content=code,
                metadata={
                    "source": blob.source,
                    "language": language,
                },
            )
            return

        self.Segmenter = LANGUAGE_SEGMENTERS[language]
        segmenter = self.Segmenter(blob.as_string())
        if not segmenter.is_valid():
            yield Document(
                page_content=code,
                metadata={
                    "source": blob.source,
                },
            )
            return

        for functions_classes in segmenter.extract_functions_classes():
            yield Document(
                page_content=functions_classes,
                metadata={
                    "source": blob.source,
                    "content_type": "functions_classes",
                    "language": language,
                },
            )
        yield Document(
            page_content=segmenter.simplify_code(),
            metadata={
                "source": blob.source,
                "content_type": "simplified_code",
                "language": language,
            },
        )
