"""**Toolkits** are sets of tools that can be used to interact with
various services and APIs.
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.agent_toolkits.ainetwork.toolkit import (
        AINetworkToolkit,
    )
    from aibaba_ai_community.agent_toolkits.amadeus.toolkit import (
        AmadeusToolkit,
    )
    from aibaba_ai_community.agent_toolkits.azure_ai_services import (
        AzureAiServicesToolkit,
    )
    from aibaba_ai_community.agent_toolkits.azure_cognitive_services import (
        AzureCognitiveServicesToolkit,
    )
    from aibaba_ai_community.agent_toolkits.cassandra_database.toolkit import (
        CassandraDatabaseToolkit,  # noqa: F401
    )
    from aibaba_ai_community.agent_toolkits.cogniswitch.toolkit import (
        CogniswitchToolkit,
    )
    from aibaba_ai_community.agent_toolkits.connery import (
        ConneryToolkit,
    )
    from aibaba_ai_community.agent_toolkits.file_management.toolkit import (
        FileManagementToolkit,
    )
    from aibaba_ai_community.agent_toolkits.gmail.toolkit import (
        GmailToolkit,
    )
    from aibaba_ai_community.agent_toolkits.jira.toolkit import (
        JiraToolkit,
    )
    from aibaba_ai_community.agent_toolkits.json.base import (
        create_json_agent,
    )
    from aibaba_ai_community.agent_toolkits.json.toolkit import (
        JsonToolkit,
    )
    from aibaba_ai_community.agent_toolkits.multion.toolkit import (
        MultionToolkit,
    )
    from aibaba_ai_community.agent_toolkits.nasa.toolkit import (
        NasaToolkit,
    )
    from aibaba_ai_community.agent_toolkits.nla.toolkit import (
        NLAToolkit,
    )
    from aibaba_ai_community.agent_toolkits.office365.toolkit import (
        O365Toolkit,
    )
    from aibaba_ai_community.agent_toolkits.openapi.base import (
        create_openapi_agent,
    )
    from aibaba_ai_community.agent_toolkits.openapi.toolkit import (
        OpenAPIToolkit,
    )
    from aibaba_ai_community.agent_toolkits.playwright.toolkit import (
        PlayWrightBrowserToolkit,
    )
    from aibaba_ai_community.agent_toolkits.polygon.toolkit import (
        PolygonToolkit,
    )
    from aibaba_ai_community.agent_toolkits.powerbi.base import (
        create_pbi_agent,
    )
    from aibaba_ai_community.agent_toolkits.powerbi.chat_base import (
        create_pbi_chat_agent,
    )
    from aibaba_ai_community.agent_toolkits.powerbi.toolkit import (
        PowerBIToolkit,
    )
    from aibaba_ai_community.agent_toolkits.slack.toolkit import (
        SlackToolkit,
    )
    from aibaba_ai_community.agent_toolkits.spark_sql.base import (
        create_spark_sql_agent,
    )
    from aibaba_ai_community.agent_toolkits.spark_sql.toolkit import (
        SparkSQLToolkit,
    )
    from aibaba_ai_community.agent_toolkits.sql.base import (
        create_sql_agent,
    )
    from aibaba_ai_community.agent_toolkits.sql.toolkit import (
        SQLDatabaseToolkit,
    )
    from aibaba_ai_community.agent_toolkits.steam.toolkit import (
        SteamToolkit,
    )
    from aibaba_ai_community.agent_toolkits.zapier.toolkit import (
        ZapierToolkit,
    )

__all__ = [
    "AINetworkToolkit",
    "AmadeusToolkit",
    "AzureAiServicesToolkit",
    "AzureCognitiveServicesToolkit",
    "CogniswitchToolkit",
    "ConneryToolkit",
    "FileManagementToolkit",
    "GmailToolkit",
    "JiraToolkit",
    "JsonToolkit",
    "MultionToolkit",
    "NLAToolkit",
    "NasaToolkit",
    "O365Toolkit",
    "OpenAPIToolkit",
    "PlayWrightBrowserToolkit",
    "PolygonToolkit",
    "PowerBIToolkit",
    "SQLDatabaseToolkit",
    "SlackToolkit",
    "SparkSQLToolkit",
    "SteamToolkit",
    "ZapierToolkit",
    "create_json_agent",
    "create_openapi_agent",
    "create_pbi_agent",
    "create_pbi_chat_agent",
    "create_spark_sql_agent",
    "create_sql_agent",
]


_module_lookup = {
    "AINetworkToolkit": "aibaba_ai_community.agent_toolkits.ainetwork.toolkit",
    "AmadeusToolkit": "aibaba_ai_community.agent_toolkits.amadeus.toolkit",
    "AzureAiServicesToolkit": "aibaba_ai_community.agent_toolkits.azure_ai_services",
    "AzureCognitiveServicesToolkit": "aibaba_ai_community.agent_toolkits.azure_cognitive_services",  # noqa: E501
    "CogniswitchToolkit": "aibaba_ai_community.agent_toolkits.cogniswitch.toolkit",
    "ConneryToolkit": "aibaba_ai_community.agent_toolkits.connery",
    "FileManagementToolkit": "aibaba_ai_community.agent_toolkits.file_management.toolkit",  # noqa: E501
    "GmailToolkit": "aibaba_ai_community.agent_toolkits.gmail.toolkit",
    "JiraToolkit": "aibaba_ai_community.agent_toolkits.jira.toolkit",
    "JsonToolkit": "aibaba_ai_community.agent_toolkits.json.toolkit",
    "MultionToolkit": "aibaba_ai_community.agent_toolkits.multion.toolkit",
    "NLAToolkit": "aibaba_ai_community.agent_toolkits.nla.toolkit",
    "NasaToolkit": "aibaba_ai_community.agent_toolkits.nasa.toolkit",
    "O365Toolkit": "aibaba_ai_community.agent_toolkits.office365.toolkit",
    "OpenAPIToolkit": "aibaba_ai_community.agent_toolkits.openapi.toolkit",
    "PlayWrightBrowserToolkit": "aibaba_ai_community.agent_toolkits.playwright.toolkit",
    "PolygonToolkit": "aibaba_ai_community.agent_toolkits.polygon.toolkit",
    "PowerBIToolkit": "aibaba_ai_community.agent_toolkits.powerbi.toolkit",
    "SQLDatabaseToolkit": "aibaba_ai_community.agent_toolkits.sql.toolkit",
    "SlackToolkit": "aibaba_ai_community.agent_toolkits.slack.toolkit",
    "SparkSQLToolkit": "aibaba_ai_community.agent_toolkits.spark_sql.toolkit",
    "SteamToolkit": "aibaba_ai_community.agent_toolkits.steam.toolkit",
    "ZapierToolkit": "aibaba_ai_community.agent_toolkits.zapier.toolkit",
    "create_json_agent": "aibaba_ai_community.agent_toolkits.json.base",
    "create_openapi_agent": "aibaba_ai_community.agent_toolkits.openapi.base",
    "create_pbi_agent": "aibaba_ai_community.agent_toolkits.powerbi.base",
    "create_pbi_chat_agent": "aibaba_ai_community.agent_toolkits.powerbi.chat_base",
    "create_spark_sql_agent": "aibaba_ai_community.agent_toolkits.spark_sql.base",
    "create_sql_agent": "aibaba_ai_community.agent_toolkits.sql.base",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
