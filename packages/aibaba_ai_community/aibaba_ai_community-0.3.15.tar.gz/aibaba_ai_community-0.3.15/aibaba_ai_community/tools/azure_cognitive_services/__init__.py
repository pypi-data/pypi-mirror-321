"""Azure Cognitive Services Tools."""

from aibaba_ai_community.tools.azure_cognitive_services.form_recognizer import (
    AzureCogsFormRecognizerTool,
)
from aibaba_ai_community.tools.azure_cognitive_services.image_analysis import (
    AzureCogsImageAnalysisTool,
)
from aibaba_ai_community.tools.azure_cognitive_services.speech2text import (
    AzureCogsSpeech2TextTool,
)
from aibaba_ai_community.tools.azure_cognitive_services.text2speech import (
    AzureCogsText2SpeechTool,
)
from aibaba_ai_community.tools.azure_cognitive_services.text_analytics_health import (
    AzureCogsTextAnalyticsHealthTool,
)

__all__ = [
    "AzureCogsImageAnalysisTool",
    "AzureCogsFormRecognizerTool",
    "AzureCogsSpeech2TextTool",
    "AzureCogsText2SpeechTool",
    "AzureCogsTextAnalyticsHealthTool",
]
