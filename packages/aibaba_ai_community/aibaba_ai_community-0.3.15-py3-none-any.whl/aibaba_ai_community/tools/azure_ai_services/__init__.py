"""Azure AI Services Tools."""

from aibaba_ai_community.tools.azure_ai_services.document_intelligence import (
    AzureAiServicesDocumentIntelligenceTool,
)
from aibaba_ai_community.tools.azure_ai_services.image_analysis import (
    AzureAiServicesImageAnalysisTool,
)
from aibaba_ai_community.tools.azure_ai_services.speech_to_text import (
    AzureAiServicesSpeechToTextTool,
)
from aibaba_ai_community.tools.azure_ai_services.text_analytics_for_health import (
    AzureAiServicesTextAnalyticsForHealthTool,
)
from aibaba_ai_community.tools.azure_ai_services.text_to_speech import (
    AzureAiServicesTextToSpeechTool,
)

__all__ = [
    "AzureAiServicesDocumentIntelligenceTool",
    "AzureAiServicesImageAnalysisTool",
    "AzureAiServicesSpeechToTextTool",
    "AzureAiServicesTextToSpeechTool",
    "AzureAiServicesTextAnalyticsForHealthTool",
]
