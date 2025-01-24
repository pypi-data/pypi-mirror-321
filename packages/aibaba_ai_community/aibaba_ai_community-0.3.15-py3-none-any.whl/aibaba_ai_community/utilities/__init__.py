"""**Utilities** are the integrations with third-part systems and packages.

Other Aibaba AI classes use **Utilities** to interact with third-part systems
and packages.
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.utilities.alpha_vantage import (
        AlphaVantageAPIWrapper,
    )
    from aibaba_ai_community.utilities.apify import (
        ApifyWrapper,
    )
    from aibaba_ai_community.utilities.arcee import (
        ArceeWrapper,
    )
    from aibaba_ai_community.utilities.arxiv import (
        ArxivAPIWrapper,
    )
    from aibaba_ai_community.utilities.asknews import (
        AskNewsAPIWrapper,
    )
    from aibaba_ai_community.utilities.awslambda import (
        LambdaWrapper,
    )
    from aibaba_ai_community.utilities.bibtex import (
        BibtexparserWrapper,
    )
    from aibaba_ai_community.utilities.bing_search import (
        BingSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.brave_search import (
        BraveSearchWrapper,
    )
    from aibaba_ai_community.utilities.dataherald import DataheraldAPIWrapper
    from aibaba_ai_community.utilities.dria_index import (
        DriaAPIWrapper,
    )
    from aibaba_ai_community.utilities.duckduckgo_search import (
        DuckDuckGoSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.golden_query import (
        GoldenQueryAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_books import (
        GoogleBooksAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_finance import (
        GoogleFinanceAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_jobs import (
        GoogleJobsAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_lens import (
        GoogleLensAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_places_api import (
        GooglePlacesAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_scholar import (
        GoogleScholarAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_search import (
        GoogleSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_serper import (
        GoogleSerperAPIWrapper,
    )
    from aibaba_ai_community.utilities.google_trends import (
        GoogleTrendsAPIWrapper,
    )
    from aibaba_ai_community.utilities.graphql import (
        GraphQLAPIWrapper,
    )
    from aibaba_ai_community.utilities.infobip import (
        InfobipAPIWrapper,
    )
    from aibaba_ai_community.utilities.jira import (
        JiraAPIWrapper,
    )
    from aibaba_ai_community.utilities.max_compute import (
        MaxComputeAPIWrapper,
    )
    from aibaba_ai_community.utilities.merriam_webster import (
        MerriamWebsterAPIWrapper,
    )
    from aibaba_ai_community.utilities.metaphor_search import (
        MetaphorSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.mojeek_search import (
        MojeekSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.nasa import (
        NasaAPIWrapper,
    )
    from aibaba_ai_community.utilities.nvidia_riva import (
        AudioStream,
        NVIDIARivaASR,
        NVIDIARivaStream,
        NVIDIARivaTTS,
        RivaASR,
        RivaTTS,
    )
    from aibaba_ai_community.utilities.openweathermap import (
        OpenWeatherMapAPIWrapper,
    )
    from aibaba_ai_community.utilities.oracleai import (
        OracleSummary,
    )
    from aibaba_ai_community.utilities.outline import (
        OutlineAPIWrapper,
    )
    from aibaba_ai_community.utilities.passio_nutrition_ai import (
        NutritionAIAPI,
    )
    from aibaba_ai_community.utilities.portkey import (
        Portkey,
    )
    from aibaba_ai_community.utilities.powerbi import (
        PowerBIDataset,
    )
    from aibaba_ai_community.utilities.pubmed import (
        PubMedAPIWrapper,
    )
    from aibaba_ai_community.utilities.rememberizer import RememberizerAPIWrapper
    from aibaba_ai_community.utilities.requests import (
        Requests,
        RequestsWrapper,
        TextRequestsWrapper,
    )
    from aibaba_ai_community.utilities.scenexplain import (
        SceneXplainAPIWrapper,
    )
    from aibaba_ai_community.utilities.searchapi import (
        SearchApiAPIWrapper,
    )
    from aibaba_ai_community.utilities.searx_search import (
        SearxSearchWrapper,
    )
    from aibaba_ai_community.utilities.serpapi import (
        SerpAPIWrapper,
    )
    from aibaba_ai_community.utilities.spark_sql import (
        SparkSQL,
    )
    from aibaba_ai_community.utilities.sql_database import (
        SQLDatabase,
    )
    from aibaba_ai_community.utilities.stackexchange import (
        StackExchangeAPIWrapper,
    )
    from aibaba_ai_community.utilities.steam import (
        SteamWebAPIWrapper,
    )
    from aibaba_ai_community.utilities.tensorflow_datasets import (
        TensorflowDatasets,
    )
    from aibaba_ai_community.utilities.twilio import (
        TwilioAPIWrapper,
    )
    from aibaba_ai_community.utilities.wikipedia import (
        WikipediaAPIWrapper,
    )
    from aibaba_ai_community.utilities.wolfram_alpha import (
        WolframAlphaAPIWrapper,
    )
    from aibaba_ai_community.utilities.you import (
        YouSearchAPIWrapper,
    )
    from aibaba_ai_community.utilities.zapier import (
        ZapierNLAWrapper,
    )

__all__ = [
    "AlphaVantageAPIWrapper",
    "ApifyWrapper",
    "ArceeWrapper",
    "ArxivAPIWrapper",
    "AskNewsAPIWrapper",
    "AudioStream",
    "BibtexparserWrapper",
    "BingSearchAPIWrapper",
    "BraveSearchWrapper",
    "DataheraldAPIWrapper",
    "DriaAPIWrapper",
    "DuckDuckGoSearchAPIWrapper",
    "GoldenQueryAPIWrapper",
    "GoogleBooksAPIWrapper",
    "GoogleFinanceAPIWrapper",
    "GoogleJobsAPIWrapper",
    "GoogleLensAPIWrapper",
    "GooglePlacesAPIWrapper",
    "GoogleScholarAPIWrapper",
    "GoogleSearchAPIWrapper",
    "GoogleSerperAPIWrapper",
    "GoogleTrendsAPIWrapper",
    "GraphQLAPIWrapper",
    "InfobipAPIWrapper",
    "JiraAPIWrapper",
    "LambdaWrapper",
    "MaxComputeAPIWrapper",
    "MerriamWebsterAPIWrapper",
    "MetaphorSearchAPIWrapper",
    "MojeekSearchAPIWrapper",
    "NVIDIARivaASR",
    "NVIDIARivaStream",
    "NVIDIARivaTTS",
    "NasaAPIWrapper",
    "NutritionAIAPI",
    "OpenWeatherMapAPIWrapper",
    "OracleSummary",
    "OutlineAPIWrapper",
    "Portkey",
    "PowerBIDataset",
    "PubMedAPIWrapper",
    "RememberizerAPIWrapper",
    "Requests",
    "RequestsWrapper",
    "RivaASR",
    "RivaTTS",
    "SceneXplainAPIWrapper",
    "SearchApiAPIWrapper",
    "SQLDatabase",
    "SearxSearchWrapper",
    "SerpAPIWrapper",
    "SparkSQL",
    "StackExchangeAPIWrapper",
    "SteamWebAPIWrapper",
    "TensorflowDatasets",
    "TextRequestsWrapper",
    "TwilioAPIWrapper",
    "WikipediaAPIWrapper",
    "WolframAlphaAPIWrapper",
    "YouSearchAPIWrapper",
    "ZapierNLAWrapper",
]

_module_lookup = {
    "AlphaVantageAPIWrapper": "aibaba_ai_community.utilities.alpha_vantage",
    "ApifyWrapper": "aibaba_ai_community.utilities.apify",
    "ArceeWrapper": "aibaba_ai_community.utilities.arcee",
    "ArxivAPIWrapper": "aibaba_ai_community.utilities.arxiv",
    "AskNewsAPIWrapper": "aibaba_ai_community.utilities.asknews",
    "AudioStream": "aibaba_ai_community.utilities.nvidia_riva",
    "BibtexparserWrapper": "aibaba_ai_community.utilities.bibtex",
    "BingSearchAPIWrapper": "aibaba_ai_community.utilities.bing_search",
    "BraveSearchWrapper": "aibaba_ai_community.utilities.brave_search",
    "DataheraldAPIWrapper": "aibaba_ai_community.utilities.dataherald",
    "DriaAPIWrapper": "aibaba_ai_community.utilities.dria_index",
    "DuckDuckGoSearchAPIWrapper": "aibaba_ai_community.utilities.duckduckgo_search",
    "GoldenQueryAPIWrapper": "aibaba_ai_community.utilities.golden_query",
    "GoogleBooksAPIWrapper": "aibaba_ai_community.utilities.google_books",
    "GoogleFinanceAPIWrapper": "aibaba_ai_community.utilities.google_finance",
    "GoogleJobsAPIWrapper": "aibaba_ai_community.utilities.google_jobs",
    "GoogleLensAPIWrapper": "aibaba_ai_community.utilities.google_lens",
    "GooglePlacesAPIWrapper": "aibaba_ai_community.utilities.google_places_api",
    "GoogleScholarAPIWrapper": "aibaba_ai_community.utilities.google_scholar",
    "GoogleSearchAPIWrapper": "aibaba_ai_community.utilities.google_search",
    "GoogleSerperAPIWrapper": "aibaba_ai_community.utilities.google_serper",
    "GoogleTrendsAPIWrapper": "aibaba_ai_community.utilities.google_trends",
    "GraphQLAPIWrapper": "aibaba_ai_community.utilities.graphql",
    "InfobipAPIWrapper": "aibaba_ai_community.utilities.infobip",
    "JiraAPIWrapper": "aibaba_ai_community.utilities.jira",
    "LambdaWrapper": "aibaba_ai_community.utilities.awslambda",
    "MaxComputeAPIWrapper": "aibaba_ai_community.utilities.max_compute",
    "MerriamWebsterAPIWrapper": "aibaba_ai_community.utilities.merriam_webster",
    "MetaphorSearchAPIWrapper": "aibaba_ai_community.utilities.metaphor_search",
    "MojeekSearchAPIWrapper": "aibaba_ai_community.utilities.mojeek_search",
    "NVIDIARivaASR": "aibaba_ai_community.utilities.nvidia_riva",
    "NVIDIARivaStream": "aibaba_ai_community.utilities.nvidia_riva",
    "NVIDIARivaTTS": "aibaba_ai_community.utilities.nvidia_riva",
    "NasaAPIWrapper": "aibaba_ai_community.utilities.nasa",
    "NutritionAIAPI": "aibaba_ai_community.utilities.passio_nutrition_ai",
    "OpenWeatherMapAPIWrapper": "aibaba_ai_community.utilities.openweathermap",
    "OracleSummary": "aibaba_ai_community.utilities.oracleai",
    "OutlineAPIWrapper": "aibaba_ai_community.utilities.outline",
    "Portkey": "aibaba_ai_community.utilities.portkey",
    "PowerBIDataset": "aibaba_ai_community.utilities.powerbi",
    "PubMedAPIWrapper": "aibaba_ai_community.utilities.pubmed",
    "RememberizerAPIWrapper": "aibaba_ai_community.utilities.rememberizer",
    "Requests": "aibaba_ai_community.utilities.requests",
    "RequestsWrapper": "aibaba_ai_community.utilities.requests",
    "RivaASR": "aibaba_ai_community.utilities.nvidia_riva",
    "RivaTTS": "aibaba_ai_community.utilities.nvidia_riva",
    "SQLDatabase": "aibaba_ai_community.utilities.sql_database",
    "SceneXplainAPIWrapper": "aibaba_ai_community.utilities.scenexplain",
    "SearchApiAPIWrapper": "aibaba_ai_community.utilities.searchapi",
    "SearxSearchWrapper": "aibaba_ai_community.utilities.searx_search",
    "SerpAPIWrapper": "aibaba_ai_community.utilities.serpapi",
    "SparkSQL": "aibaba_ai_community.utilities.spark_sql",
    "StackExchangeAPIWrapper": "aibaba_ai_community.utilities.stackexchange",
    "SteamWebAPIWrapper": "aibaba_ai_community.utilities.steam",
    "TensorflowDatasets": "aibaba_ai_community.utilities.tensorflow_datasets",
    "TextRequestsWrapper": "aibaba_ai_community.utilities.requests",
    "TwilioAPIWrapper": "aibaba_ai_community.utilities.twilio",
    "WikipediaAPIWrapper": "aibaba_ai_community.utilities.wikipedia",
    "WolframAlphaAPIWrapper": "aibaba_ai_community.utilities.wolfram_alpha",
    "YouSearchAPIWrapper": "aibaba_ai_community.utilities.you",
    "ZapierNLAWrapper": "aibaba_ai_community.utilities.zapier",
}

REMOVED = {
    "PythonREPL": (
        "PythonREPL has been deprecated from aibaba_ai_community "
        "due to being flagged by security scanners. See: "
        "https://github.com/aibaba-ai/aibaba-ai/issues/14345 "
        "If you need to use it, please use the version "
        "from langchain_experimental. "
        "from langchain_experimental.utilities.python import PythonREPL."
    )
}


def __getattr__(name: str) -> Any:
    if name in REMOVED:
        raise AssertionError(REMOVED[name])
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
