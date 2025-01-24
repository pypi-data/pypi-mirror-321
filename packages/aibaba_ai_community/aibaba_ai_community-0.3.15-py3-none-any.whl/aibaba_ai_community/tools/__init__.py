"""**Tools** are classes that an Agent uses to interact with the world.

Each tool has a **description**. Agent uses the description to choose the right
tool for the job.

**Class hierarchy:**

.. code-block::

    ToolMetaclass --> BaseTool --> <name>Tool  # Examples: AIPluginTool, BaseGraphQLTool
                                   <name>      # Examples: BraveSearch, HumanInputRun

**Main helpers:**

.. code-block::

    CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from alibaba_ai_core.tools import (
        BaseTool as BaseTool,
    )
    from alibaba_ai_core.tools import (
        StructuredTool as StructuredTool,
    )
    from alibaba_ai_core.tools import (
        Tool as Tool,
    )
    from alibaba_ai_core.tools.convert import tool as tool

    from aibaba_ai_community.tools.ainetwork.app import (
        AINAppOps,
    )
    from aibaba_ai_community.tools.ainetwork.owner import (
        AINOwnerOps,
    )
    from aibaba_ai_community.tools.ainetwork.rule import (
        AINRuleOps,
    )
    from aibaba_ai_community.tools.ainetwork.transfer import (
        AINTransfer,
    )
    from aibaba_ai_community.tools.ainetwork.value import (
        AINValueOps,
    )
    from aibaba_ai_community.tools.arxiv.tool import (
        ArxivQueryRun,
    )
    from aibaba_ai_community.tools.asknews.tool import (
        AskNewsSearch,
    )
    from aibaba_ai_community.tools.azure_ai_services import (
        AzureAiServicesDocumentIntelligenceTool,
        AzureAiServicesImageAnalysisTool,
        AzureAiServicesSpeechToTextTool,
        AzureAiServicesTextAnalyticsForHealthTool,
        AzureAiServicesTextToSpeechTool,
    )
    from aibaba_ai_community.tools.azure_cognitive_services import (
        AzureCogsFormRecognizerTool,
        AzureCogsImageAnalysisTool,
        AzureCogsSpeech2TextTool,
        AzureCogsText2SpeechTool,
        AzureCogsTextAnalyticsHealthTool,
    )
    from aibaba_ai_community.tools.bearly.tool import (
        BearlyInterpreterTool,
    )
    from aibaba_ai_community.tools.bing_search.tool import (
        BingSearchResults,
        BingSearchRun,
    )
    from aibaba_ai_community.tools.brave_search.tool import (
        BraveSearch,
    )
    from aibaba_ai_community.tools.cassandra_database.tool import (
        GetSchemaCassandraDatabaseTool,  # noqa: F401
        GetTableDataCassandraDatabaseTool,  # noqa: F401
        QueryCassandraDatabaseTool,  # noqa: F401
    )
    from aibaba_ai_community.tools.cogniswitch.tool import (
        CogniswitchKnowledgeRequest,
        CogniswitchKnowledgeSourceFile,
        CogniswitchKnowledgeSourceURL,
        CogniswitchKnowledgeStatus,
    )
    from aibaba_ai_community.tools.connery import (
        ConneryAction,
    )
    from aibaba_ai_community.tools.convert_to_openai import (
        format_tool_to_openai_function,
    )
    from aibaba_ai_community.tools.dataherald import DataheraldTextToSQL
    from aibaba_ai_community.tools.ddg_search.tool import (
        DuckDuckGoSearchResults,
        DuckDuckGoSearchRun,
    )
    from aibaba_ai_community.tools.e2b_data_analysis.tool import (
        E2BDataAnalysisTool,
    )
    from aibaba_ai_community.tools.edenai import (
        EdenAiExplicitImageTool,
        EdenAiObjectDetectionTool,
        EdenAiParsingIDTool,
        EdenAiParsingInvoiceTool,
        EdenAiSpeechToTextTool,
        EdenAiTextModerationTool,
        EdenAiTextToSpeechTool,
        EdenaiTool,
    )
    from aibaba_ai_community.tools.eleven_labs.text2speech import (
        ElevenLabsText2SpeechTool,
    )
    from aibaba_ai_community.tools.file_management import (
        CopyFileTool,
        DeleteFileTool,
        FileSearchTool,
        ListDirectoryTool,
        MoveFileTool,
        ReadFileTool,
        WriteFileTool,
    )
    from aibaba_ai_community.tools.financial_datasets.balance_sheets import (
        BalanceSheets,
    )
    from aibaba_ai_community.tools.financial_datasets.cash_flow_statements import (
        CashFlowStatements,
    )
    from aibaba_ai_community.tools.financial_datasets.income_statements import (
        IncomeStatements,
    )
    from aibaba_ai_community.tools.gmail import (
        GmailCreateDraft,
        GmailGetMessage,
        GmailGetThread,
        GmailSearch,
        GmailSendMessage,
    )
    from aibaba_ai_community.tools.google_books import (
        GoogleBooksQueryRun,
    )
    from aibaba_ai_community.tools.google_cloud.texttospeech import (
        GoogleCloudTextToSpeechTool,
    )
    from aibaba_ai_community.tools.google_places.tool import (
        GooglePlacesTool,
    )
    from aibaba_ai_community.tools.google_search.tool import (
        GoogleSearchResults,
        GoogleSearchRun,
    )
    from aibaba_ai_community.tools.google_serper.tool import (
        GoogleSerperResults,
        GoogleSerperRun,
    )
    from aibaba_ai_community.tools.graphql.tool import (
        BaseGraphQLTool,
    )
    from aibaba_ai_community.tools.human.tool import (
        HumanInputRun,
    )
    from aibaba_ai_community.tools.ifttt import (
        IFTTTWebhook,
    )
    from aibaba_ai_community.tools.interaction.tool import (
        StdInInquireTool,
    )
    from aibaba_ai_community.tools.jina_search.tool import JinaSearch
    from aibaba_ai_community.tools.jira.tool import (
        JiraAction,
    )
    from aibaba_ai_community.tools.json.tool import (
        JsonGetValueTool,
        JsonListKeysTool,
    )
    from aibaba_ai_community.tools.merriam_webster.tool import (
        MerriamWebsterQueryRun,
    )
    from aibaba_ai_community.tools.metaphor_search import (
        MetaphorSearchResults,
    )
    from aibaba_ai_community.tools.mojeek_search.tool import (
        MojeekSearch,
    )
    from aibaba_ai_community.tools.nasa.tool import (
        NasaAction,
    )
    from aibaba_ai_community.tools.office365.create_draft_message import (
        O365CreateDraftMessage,
    )
    from aibaba_ai_community.tools.office365.events_search import (
        O365SearchEvents,
    )
    from aibaba_ai_community.tools.office365.messages_search import (
        O365SearchEmails,
    )
    from aibaba_ai_community.tools.office365.send_event import (
        O365SendEvent,
    )
    from aibaba_ai_community.tools.office365.send_message import (
        O365SendMessage,
    )
    from aibaba_ai_community.tools.office365.utils import (
        authenticate,
    )
    from aibaba_ai_community.tools.openapi.utils.api_models import (
        APIOperation,
    )
    from aibaba_ai_community.tools.openapi.utils.openapi_utils import (
        OpenAPISpec,
    )
    from aibaba_ai_community.tools.openweathermap.tool import (
        OpenWeatherMapQueryRun,
    )
    from aibaba_ai_community.tools.playwright import (
        ClickTool,
        CurrentWebPageTool,
        ExtractHyperlinksTool,
        ExtractTextTool,
        GetElementsTool,
        NavigateBackTool,
        NavigateTool,
    )
    from aibaba_ai_community.tools.plugin import (
        AIPluginTool,
    )
    from aibaba_ai_community.tools.polygon.aggregates import (
        PolygonAggregates,
    )
    from aibaba_ai_community.tools.polygon.financials import (
        PolygonFinancials,
    )
    from aibaba_ai_community.tools.polygon.last_quote import (
        PolygonLastQuote,
    )
    from aibaba_ai_community.tools.polygon.ticker_news import (
        PolygonTickerNews,
    )
    from aibaba_ai_community.tools.powerbi.tool import (
        InfoPowerBITool,
        ListPowerBITool,
        QueryPowerBITool,
    )
    from aibaba_ai_community.tools.pubmed.tool import (
        PubmedQueryRun,
    )
    from aibaba_ai_community.tools.reddit_search.tool import (
        RedditSearchRun,
        RedditSearchSchema,
    )
    from aibaba_ai_community.tools.requests.tool import (
        BaseRequestsTool,
        RequestsDeleteTool,
        RequestsGetTool,
        RequestsPatchTool,
        RequestsPostTool,
        RequestsPutTool,
    )
    from aibaba_ai_community.tools.scenexplain.tool import (
        SceneXplainTool,
    )
    from aibaba_ai_community.tools.searchapi.tool import (
        SearchAPIResults,
        SearchAPIRun,
    )
    from aibaba_ai_community.tools.searx_search.tool import (
        SearxSearchResults,
        SearxSearchRun,
    )
    from aibaba_ai_community.tools.shell.tool import (
        ShellTool,
    )
    from aibaba_ai_community.tools.slack.get_channel import (
        SlackGetChannel,
    )
    from aibaba_ai_community.tools.slack.get_message import (
        SlackGetMessage,
    )
    from aibaba_ai_community.tools.slack.schedule_message import (
        SlackScheduleMessage,
    )
    from aibaba_ai_community.tools.slack.send_message import (
        SlackSendMessage,
    )
    from aibaba_ai_community.tools.sleep.tool import (
        SleepTool,
    )
    from aibaba_ai_community.tools.spark_sql.tool import (
        BaseSparkSQLTool,
        InfoSparkSQLTool,
        ListSparkSQLTool,
        QueryCheckerTool,
        QuerySparkSQLTool,
    )
    from aibaba_ai_community.tools.sql_database.tool import (
        BaseSQLDatabaseTool,
        InfoSQLDatabaseTool,
        ListSQLDatabaseTool,
        QuerySQLCheckerTool,
        QuerySQLDataBaseTool,
        QuerySQLDatabaseTool,
    )
    from aibaba_ai_community.tools.stackexchange.tool import (
        StackExchangeTool,
    )
    from aibaba_ai_community.tools.steam.tool import (
        SteamWebAPIQueryRun,
    )
    from aibaba_ai_community.tools.steamship_image_generation import (
        SteamshipImageGenerationTool,
    )
    from aibaba_ai_community.tools.tavily_search import (
        TavilyAnswer,
        TavilySearchResults,
    )
    from aibaba_ai_community.tools.vectorstore.tool import (
        VectorStoreQATool,
        VectorStoreQAWithSourcesTool,
    )
    from aibaba_ai_community.tools.wikipedia.tool import (
        WikipediaQueryRun,
    )
    from aibaba_ai_community.tools.wolfram_alpha.tool import (
        WolframAlphaQueryRun,
    )
    from aibaba_ai_community.tools.yahoo_finance_news import (
        YahooFinanceNewsTool,
    )
    from aibaba_ai_community.tools.you.tool import (
        YouSearchTool,
    )
    from aibaba_ai_community.tools.youtube.search import (
        YouTubeSearchTool,
    )
    from aibaba_ai_community.tools.zapier.tool import (
        ZapierNLAListActions,
        ZapierNLARunAction,
    )
    from aibaba_ai_community.tools.zenguard.tool import (
        Detector,
        ZenGuardInput,
        ZenGuardTool,
    )

__all__ = [
    "BaseTool",
    "Tool",
    "tool",
    "StructuredTool",
    "AINAppOps",
    "AINOwnerOps",
    "AINRuleOps",
    "AINTransfer",
    "AINValueOps",
    "AIPluginTool",
    "APIOperation",
    "ArxivQueryRun",
    "AskNewsSearch",
    "AzureAiServicesDocumentIntelligenceTool",
    "AzureAiServicesImageAnalysisTool",
    "AzureAiServicesSpeechToTextTool",
    "AzureAiServicesTextAnalyticsForHealthTool",
    "AzureAiServicesTextToSpeechTool",
    "AzureCogsFormRecognizerTool",
    "AzureCogsImageAnalysisTool",
    "AzureCogsSpeech2TextTool",
    "AzureCogsText2SpeechTool",
    "AzureCogsTextAnalyticsHealthTool",
    "BalanceSheets",
    "BaseGraphQLTool",
    "BaseRequestsTool",
    "BaseSQLDatabaseTool",
    "BaseSparkSQLTool",
    "BearlyInterpreterTool",
    "BingSearchResults",
    "BingSearchRun",
    "BraveSearch",
    "CashFlowStatements",
    "ClickTool",
    "CogniswitchKnowledgeRequest",
    "CogniswitchKnowledgeSourceFile",
    "CogniswitchKnowledgeSourceURL",
    "CogniswitchKnowledgeStatus",
    "ConneryAction",
    "CopyFileTool",
    "CurrentWebPageTool",
    "DeleteFileTool",
    "DataheraldTextToSQL",
    "DuckDuckGoSearchResults",
    "DuckDuckGoSearchRun",
    "E2BDataAnalysisTool",
    "EdenAiExplicitImageTool",
    "EdenAiObjectDetectionTool",
    "EdenAiParsingIDTool",
    "EdenAiParsingInvoiceTool",
    "EdenAiSpeechToTextTool",
    "EdenAiTextModerationTool",
    "EdenAiTextToSpeechTool",
    "EdenaiTool",
    "ElevenLabsText2SpeechTool",
    "ExtractHyperlinksTool",
    "ExtractTextTool",
    "FileSearchTool",
    "GetElementsTool",
    "GmailCreateDraft",
    "GmailGetMessage",
    "GmailGetThread",
    "GmailSearch",
    "GmailSendMessage",
    "GoogleBooksQueryRun",
    "GoogleCloudTextToSpeechTool",
    "GooglePlacesTool",
    "GoogleSearchResults",
    "GoogleSearchRun",
    "GoogleSerperResults",
    "GoogleSerperRun",
    "HumanInputRun",
    "IFTTTWebhook",
    "IncomeStatements",
    "InfoPowerBITool",
    "InfoSQLDatabaseTool",
    "InfoSparkSQLTool",
    "JiraAction",
    "JinaSearch",
    "JsonGetValueTool",
    "JsonListKeysTool",
    "ListDirectoryTool",
    "ListPowerBITool",
    "ListSQLDatabaseTool",
    "ListSparkSQLTool",
    "MerriamWebsterQueryRun",
    "MetaphorSearchResults",
    "MojeekSearch",
    "MoveFileTool",
    "NasaAction",
    "NavigateBackTool",
    "NavigateTool",
    "O365CreateDraftMessage",
    "O365SearchEmails",
    "O365SearchEvents",
    "O365SendEvent",
    "O365SendMessage",
    "OpenAPISpec",
    "OpenWeatherMapQueryRun",
    "PolygonAggregates",
    "PolygonFinancials",
    "PolygonLastQuote",
    "PolygonTickerNews",
    "PubmedQueryRun",
    "QueryCheckerTool",
    "QueryPowerBITool",
    "QuerySQLCheckerTool",
    "QuerySQLDatabaseTool",
    "QuerySQLDataBaseTool",  # Legacy, kept for backwards compatibility.
    "QuerySparkSQLTool",
    "ReadFileTool",
    "RedditSearchRun",
    "RedditSearchSchema",
    "RequestsDeleteTool",
    "RequestsGetTool",
    "RequestsPatchTool",
    "RequestsPostTool",
    "RequestsPutTool",
    "SceneXplainTool",
    "SearchAPIResults",
    "SearchAPIRun",
    "SearxSearchResults",
    "SearxSearchRun",
    "ShellTool",
    "SlackGetChannel",
    "SlackGetMessage",
    "SlackScheduleMessage",
    "SlackSendMessage",
    "SleepTool",
    "StackExchangeTool",
    "StdInInquireTool",
    "SteamWebAPIQueryRun",
    "SteamshipImageGenerationTool",
    "TavilyAnswer",
    "TavilySearchResults",
    "VectorStoreQATool",
    "VectorStoreQAWithSourcesTool",
    "WikipediaQueryRun",
    "WolframAlphaQueryRun",
    "WriteFileTool",
    "YahooFinanceNewsTool",
    "YouSearchTool",
    "YouTubeSearchTool",
    "ZapierNLAListActions",
    "ZapierNLARunAction",
    "Detector",
    "ZenGuardInput",
    "ZenGuardTool",
    "authenticate",
    "format_tool_to_openai_function",
]

# Used for internal purposes
_DEPRECATED_TOOLS = {"PythonAstREPLTool", "PythonREPLTool"}

_module_lookup = {
    "AINAppOps": "aibaba_ai_community.tools.ainetwork.app",
    "AINOwnerOps": "aibaba_ai_community.tools.ainetwork.owner",
    "AINRuleOps": "aibaba_ai_community.tools.ainetwork.rule",
    "AINTransfer": "aibaba_ai_community.tools.ainetwork.transfer",
    "AINValueOps": "aibaba_ai_community.tools.ainetwork.value",
    "AIPluginTool": "aibaba_ai_community.tools.plugin",
    "APIOperation": "aibaba_ai_community.tools.openapi.utils.api_models",
    "ArxivQueryRun": "aibaba_ai_community.tools.arxiv.tool",
    "AskNewsSearch": "aibaba_ai_community.tools.asknews.tool",
    "AzureAiServicesDocumentIntelligenceTool": "aibaba_ai_community.tools.azure_ai_services",  # noqa: E501
    "AzureAiServicesImageAnalysisTool": "aibaba_ai_community.tools.azure_ai_services",
    "AzureAiServicesSpeechToTextTool": "aibaba_ai_community.tools.azure_ai_services",
    "AzureAiServicesTextToSpeechTool": "aibaba_ai_community.tools.azure_ai_services",
    "AzureAiServicesTextAnalyticsForHealthTool": "aibaba_ai_community.tools.azure_ai_services",  # noqa: E501
    "AzureCogsFormRecognizerTool": "aibaba_ai_community.tools.azure_cognitive_services",
    "AzureCogsImageAnalysisTool": "aibaba_ai_community.tools.azure_cognitive_services",
    "AzureCogsSpeech2TextTool": "aibaba_ai_community.tools.azure_cognitive_services",
    "AzureCogsText2SpeechTool": "aibaba_ai_community.tools.azure_cognitive_services",
    "AzureCogsTextAnalyticsHealthTool": "aibaba_ai_community.tools.azure_cognitive_services",  # noqa: E501
    "BalanceSheets": "aibaba_ai_community.tools.financial_datasets.balance_sheets",
    "BaseGraphQLTool": "aibaba_ai_community.tools.graphql.tool",
    "BaseRequestsTool": "aibaba_ai_community.tools.requests.tool",
    "BaseSQLDatabaseTool": "aibaba_ai_community.tools.sql_database.tool",
    "BaseSparkSQLTool": "aibaba_ai_community.tools.spark_sql.tool",
    "BaseTool": "alibaba_ai_core.tools",
    "BearlyInterpreterTool": "aibaba_ai_community.tools.bearly.tool",
    "BingSearchResults": "aibaba_ai_community.tools.bing_search.tool",
    "BingSearchRun": "aibaba_ai_community.tools.bing_search.tool",
    "BraveSearch": "aibaba_ai_community.tools.brave_search.tool",
    "CashFlowStatements": "aibaba_ai_community.tools.financial_datasets.cash_flow_statements",  # noqa: E501
    "ClickTool": "aibaba_ai_community.tools.playwright",
    "CogniswitchKnowledgeRequest": "aibaba_ai_community.tools.cogniswitch.tool",
    "CogniswitchKnowledgeSourceFile": "aibaba_ai_community.tools.cogniswitch.tool",
    "CogniswitchKnowledgeSourceURL": "aibaba_ai_community.tools.cogniswitch.tool",
    "CogniswitchKnowledgeStatus": "aibaba_ai_community.tools.cogniswitch.tool",
    "ConneryAction": "aibaba_ai_community.tools.connery",
    "CopyFileTool": "aibaba_ai_community.tools.file_management",
    "CurrentWebPageTool": "aibaba_ai_community.tools.playwright",
    "DataheraldTextToSQL": "aibaba_ai_community.tools.dataherald.tool",
    "DeleteFileTool": "aibaba_ai_community.tools.file_management",
    "Detector": "aibaba_ai_community.tools.zenguard.tool",
    "DuckDuckGoSearchResults": "aibaba_ai_community.tools.ddg_search.tool",
    "DuckDuckGoSearchRun": "aibaba_ai_community.tools.ddg_search.tool",
    "E2BDataAnalysisTool": "aibaba_ai_community.tools.e2b_data_analysis.tool",
    "EdenAiExplicitImageTool": "aibaba_ai_community.tools.edenai",
    "EdenAiObjectDetectionTool": "aibaba_ai_community.tools.edenai",
    "EdenAiParsingIDTool": "aibaba_ai_community.tools.edenai",
    "EdenAiParsingInvoiceTool": "aibaba_ai_community.tools.edenai",
    "EdenAiSpeechToTextTool": "aibaba_ai_community.tools.edenai",
    "EdenAiTextModerationTool": "aibaba_ai_community.tools.edenai",
    "EdenAiTextToSpeechTool": "aibaba_ai_community.tools.edenai",
    "EdenaiTool": "aibaba_ai_community.tools.edenai",
    "ElevenLabsText2SpeechTool": "aibaba_ai_community.tools.eleven_labs.text2speech",
    "ExtractHyperlinksTool": "aibaba_ai_community.tools.playwright",
    "ExtractTextTool": "aibaba_ai_community.tools.playwright",
    "FileSearchTool": "aibaba_ai_community.tools.file_management",
    "GetElementsTool": "aibaba_ai_community.tools.playwright",
    "GmailCreateDraft": "aibaba_ai_community.tools.gmail",
    "GmailGetMessage": "aibaba_ai_community.tools.gmail",
    "GmailGetThread": "aibaba_ai_community.tools.gmail",
    "GmailSearch": "aibaba_ai_community.tools.gmail",
    "GmailSendMessage": "aibaba_ai_community.tools.gmail",
    "GoogleBooksQueryRun": "aibaba_ai_community.tools.google_books",
    "GoogleCloudTextToSpeechTool": "aibaba_ai_community.tools.google_cloud.texttospeech",  # noqa: E501
    "GooglePlacesTool": "aibaba_ai_community.tools.google_places.tool",
    "GoogleSearchResults": "aibaba_ai_community.tools.google_search.tool",
    "GoogleSearchRun": "aibaba_ai_community.tools.google_search.tool",
    "GoogleSerperResults": "aibaba_ai_community.tools.google_serper.tool",
    "GoogleSerperRun": "aibaba_ai_community.tools.google_serper.tool",
    "HumanInputRun": "aibaba_ai_community.tools.human.tool",
    "IFTTTWebhook": "aibaba_ai_community.tools.ifttt",
    "IncomeStatements": "aibaba_ai_community.tools.financial_datasets.income_statements",  # noqa: E501
    "InfoPowerBITool": "aibaba_ai_community.tools.powerbi.tool",
    "InfoSQLDatabaseTool": "aibaba_ai_community.tools.sql_database.tool",
    "InfoSparkSQLTool": "aibaba_ai_community.tools.spark_sql.tool",
    "JiraAction": "aibaba_ai_community.tools.jira.tool",
    "JinaSearch": "aibaba_ai_community.tools.jina_search.tool",
    "JsonGetValueTool": "aibaba_ai_community.tools.json.tool",
    "JsonListKeysTool": "aibaba_ai_community.tools.json.tool",
    "ListDirectoryTool": "aibaba_ai_community.tools.file_management",
    "ListPowerBITool": "aibaba_ai_community.tools.powerbi.tool",
    "ListSQLDatabaseTool": "aibaba_ai_community.tools.sql_database.tool",
    "ListSparkSQLTool": "aibaba_ai_community.tools.spark_sql.tool",
    "MerriamWebsterQueryRun": "aibaba_ai_community.tools.merriam_webster.tool",
    "MetaphorSearchResults": "aibaba_ai_community.tools.metaphor_search",
    "MojeekSearch": "aibaba_ai_community.tools.mojeek_search.tool",
    "MoveFileTool": "aibaba_ai_community.tools.file_management",
    "NasaAction": "aibaba_ai_community.tools.nasa.tool",
    "NavigateBackTool": "aibaba_ai_community.tools.playwright",
    "NavigateTool": "aibaba_ai_community.tools.playwright",
    "O365CreateDraftMessage": "aibaba_ai_community.tools.office365.create_draft_message",  # noqa: E501
    "O365SearchEmails": "aibaba_ai_community.tools.office365.messages_search",
    "O365SearchEvents": "aibaba_ai_community.tools.office365.events_search",
    "O365SendEvent": "aibaba_ai_community.tools.office365.send_event",
    "O365SendMessage": "aibaba_ai_community.tools.office365.send_message",
    "OpenAPISpec": "aibaba_ai_community.tools.openapi.utils.openapi_utils",
    "OpenWeatherMapQueryRun": "aibaba_ai_community.tools.openweathermap.tool",
    "PolygonAggregates": "aibaba_ai_community.tools.polygon.aggregates",
    "PolygonFinancials": "aibaba_ai_community.tools.polygon.financials",
    "PolygonLastQuote": "aibaba_ai_community.tools.polygon.last_quote",
    "PolygonTickerNews": "aibaba_ai_community.tools.polygon.ticker_news",
    "PubmedQueryRun": "aibaba_ai_community.tools.pubmed.tool",
    "QueryCheckerTool": "aibaba_ai_community.tools.spark_sql.tool",
    "QueryPowerBITool": "aibaba_ai_community.tools.powerbi.tool",
    "QuerySQLCheckerTool": "aibaba_ai_community.tools.sql_database.tool",
    "QuerySQLDatabaseTool": "aibaba_ai_community.tools.sql_database.tool",
    # Legacy, kept for backwards compatibility.
    "QuerySQLDataBaseTool": "aibaba_ai_community.tools.sql_database.tool",
    "QuerySparkSQLTool": "aibaba_ai_community.tools.spark_sql.tool",
    "ReadFileTool": "aibaba_ai_community.tools.file_management",
    "RedditSearchRun": "aibaba_ai_community.tools.reddit_search.tool",
    "RedditSearchSchema": "aibaba_ai_community.tools.reddit_search.tool",
    "RequestsDeleteTool": "aibaba_ai_community.tools.requests.tool",
    "RequestsGetTool": "aibaba_ai_community.tools.requests.tool",
    "RequestsPatchTool": "aibaba_ai_community.tools.requests.tool",
    "RequestsPostTool": "aibaba_ai_community.tools.requests.tool",
    "RequestsPutTool": "aibaba_ai_community.tools.requests.tool",
    "SceneXplainTool": "aibaba_ai_community.tools.scenexplain.tool",
    "SearchAPIResults": "aibaba_ai_community.tools.searchapi.tool",
    "SearchAPIRun": "aibaba_ai_community.tools.searchapi.tool",
    "SearxSearchResults": "aibaba_ai_community.tools.searx_search.tool",
    "SearxSearchRun": "aibaba_ai_community.tools.searx_search.tool",
    "ShellTool": "aibaba_ai_community.tools.shell.tool",
    "SlackGetChannel": "aibaba_ai_community.tools.slack.get_channel",
    "SlackGetMessage": "aibaba_ai_community.tools.slack.get_message",
    "SlackScheduleMessage": "aibaba_ai_community.tools.slack.schedule_message",
    "SlackSendMessage": "aibaba_ai_community.tools.slack.send_message",
    "SleepTool": "aibaba_ai_community.tools.sleep.tool",
    "StackExchangeTool": "aibaba_ai_community.tools.stackexchange.tool",
    "StdInInquireTool": "aibaba_ai_community.tools.interaction.tool",
    "SteamWebAPIQueryRun": "aibaba_ai_community.tools.steam.tool",
    "SteamshipImageGenerationTool": "aibaba_ai_community.tools.steamship_image_generation",  # noqa: E501
    "StructuredTool": "alibaba_ai_core.tools",
    "TavilyAnswer": "aibaba_ai_community.tools.tavily_search",
    "TavilySearchResults": "aibaba_ai_community.tools.tavily_search",
    "Tool": "alibaba_ai_core.tools",
    "VectorStoreQATool": "aibaba_ai_community.tools.vectorstore.tool",
    "VectorStoreQAWithSourcesTool": "aibaba_ai_community.tools.vectorstore.tool",
    "WikipediaQueryRun": "aibaba_ai_community.tools.wikipedia.tool",
    "WolframAlphaQueryRun": "aibaba_ai_community.tools.wolfram_alpha.tool",
    "WriteFileTool": "aibaba_ai_community.tools.file_management",
    "YahooFinanceNewsTool": "aibaba_ai_community.tools.yahoo_finance_news",
    "YouSearchTool": "aibaba_ai_community.tools.you.tool",
    "YouTubeSearchTool": "aibaba_ai_community.tools.youtube.search",
    "ZapierNLAListActions": "aibaba_ai_community.tools.zapier.tool",
    "ZapierNLARunAction": "aibaba_ai_community.tools.zapier.tool",
    "ZenGuardInput": "aibaba_ai_community.tools.zenguard.tool",
    "ZenGuardTool": "aibaba_ai_community.tools.zenguard.tool",
    "authenticate": "aibaba_ai_community.tools.office365.utils",
    "format_tool_to_openai_function": "aibaba_ai_community.tools.convert_to_openai",
    "tool": "alibaba_ai_core.tools",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
