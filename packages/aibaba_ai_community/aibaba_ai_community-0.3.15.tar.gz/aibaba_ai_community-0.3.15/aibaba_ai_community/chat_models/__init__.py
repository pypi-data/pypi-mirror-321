"""**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose
is a bit different. Rather than expose a "text in, text out" API, they expose
an interface where "chat messages" are the inputs and outputs.

**Class hierarchy:**

.. code-block::

    BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.chat_models.anthropic import (
        ChatAnthropic,
    )
    from aibaba_ai_community.chat_models.anyscale import (
        ChatAnyscale,
    )
    from aibaba_ai_community.chat_models.azure_openai import (
        AzureChatOpenAI,
    )
    from aibaba_ai_community.chat_models.baichuan import (
        ChatBaichuan,
    )
    from aibaba_ai_community.chat_models.baidu_qianfan_endpoint import (
        QianfanChatEndpoint,
    )
    from aibaba_ai_community.chat_models.bedrock import (
        BedrockChat,
    )
    from aibaba_ai_community.chat_models.cohere import (
        ChatCohere,
    )
    from aibaba_ai_community.chat_models.coze import (
        ChatCoze,
    )
    from aibaba_ai_community.chat_models.databricks import (
        ChatDatabricks,
    )
    from aibaba_ai_community.chat_models.deepinfra import (
        ChatDeepInfra,
    )
    from aibaba_ai_community.chat_models.edenai import ChatEdenAI
    from aibaba_ai_community.chat_models.ernie import (
        ErnieBotChat,
    )
    from aibaba_ai_community.chat_models.everlyai import (
        ChatEverlyAI,
    )
    from aibaba_ai_community.chat_models.fake import (
        FakeListChatModel,
    )
    from aibaba_ai_community.chat_models.fireworks import (
        ChatFireworks,
    )
    from aibaba_ai_community.chat_models.friendli import (
        ChatFriendli,
    )
    from aibaba_ai_community.chat_models.gigachat import (
        GigaChat,
    )
    from aibaba_ai_community.chat_models.google_palm import (
        ChatGooglePalm,
    )
    from aibaba_ai_community.chat_models.gpt_router import (
        GPTRouter,
    )
    from aibaba_ai_community.chat_models.huggingface import (
        ChatHuggingFace,
    )
    from aibaba_ai_community.chat_models.human import (
        HumanInputChatModel,
    )
    from aibaba_ai_community.chat_models.hunyuan import (
        ChatHunyuan,
    )
    from aibaba_ai_community.chat_models.javelin_ai_gateway import (
        ChatJavelinAIGateway,
    )
    from aibaba_ai_community.chat_models.jinachat import (
        JinaChat,
    )
    from aibaba_ai_community.chat_models.kinetica import (
        ChatKinetica,
    )
    from aibaba_ai_community.chat_models.konko import (
        ChatKonko,
    )
    from aibaba_ai_community.chat_models.litellm import (
        ChatLiteLLM,
    )
    from aibaba_ai_community.chat_models.litellm_router import (
        ChatLiteLLMRouter,
    )
    from aibaba_ai_community.chat_models.llama_edge import (
        LlamaEdgeChatService,
    )
    from aibaba_ai_community.chat_models.llamacpp import ChatLlamaCpp
    from aibaba_ai_community.chat_models.maritalk import (
        ChatMaritalk,
    )
    from aibaba_ai_community.chat_models.minimax import (
        MiniMaxChat,
    )
    from aibaba_ai_community.chat_models.mlflow import (
        ChatMlflow,
    )
    from aibaba_ai_community.chat_models.mlflow_ai_gateway import (
        ChatMLflowAIGateway,
    )
    from aibaba_ai_community.chat_models.mlx import (
        ChatMLX,
    )
    from aibaba_ai_community.chat_models.moonshot import (
        MoonshotChat,
    )
    from aibaba_ai_community.chat_models.naver import (
        ChatClovaX,
    )
    from aibaba_ai_community.chat_models.oci_data_science import (
        ChatOCIModelDeployment,
        ChatOCIModelDeploymentTGI,
        ChatOCIModelDeploymentVLLM,
    )
    from aibaba_ai_community.chat_models.oci_generative_ai import (
        ChatOCIGenAI,  # noqa: F401
    )
    from aibaba_ai_community.chat_models.octoai import ChatOctoAI
    from aibaba_ai_community.chat_models.ollama import (
        ChatOllama,
    )
    from aibaba_ai_community.chat_models.openai import (
        ChatOpenAI,
    )
    from aibaba_ai_community.chat_models.outlines import ChatOutlines
    from aibaba_ai_community.chat_models.pai_eas_endpoint import (
        PaiEasChatEndpoint,
    )
    from aibaba_ai_community.chat_models.perplexity import (
        ChatPerplexity,
    )
    from aibaba_ai_community.chat_models.premai import (
        ChatPremAI,
    )
    from aibaba_ai_community.chat_models.promptlayer_openai import (
        PromptLayerChatOpenAI,
    )
    from aibaba_ai_community.chat_models.reka import (
        ChatReka,
    )
    from aibaba_ai_community.chat_models.sambanova import (
        ChatSambaNovaCloud,
        ChatSambaStudio,
    )
    from aibaba_ai_community.chat_models.snowflake import (
        ChatSnowflakeCortex,
    )
    from aibaba_ai_community.chat_models.solar import (
        SolarChat,
    )
    from aibaba_ai_community.chat_models.sparkllm import (
        ChatSparkLLM,
    )
    from aibaba_ai_community.chat_models.symblai_nebula import ChatNebula
    from aibaba_ai_community.chat_models.tongyi import (
        ChatTongyi,
    )
    from aibaba_ai_community.chat_models.vertexai import (
        ChatVertexAI,
    )
    from aibaba_ai_community.chat_models.volcengine_maas import (
        VolcEngineMaasChat,
    )
    from aibaba_ai_community.chat_models.yandex import (
        ChatYandexGPT,
    )
    from aibaba_ai_community.chat_models.yi import (
        ChatYi,
    )
    from aibaba_ai_community.chat_models.yuan2 import (
        ChatYuan2,
    )
    from aibaba_ai_community.chat_models.zhipuai import (
        ChatZhipuAI,
    )
__all__ = [
    "AzureChatOpenAI",
    "BedrockChat",
    "ChatAnthropic",
    "ChatAnyscale",
    "ChatBaichuan",
    "ChatClovaX",
    "ChatCohere",
    "ChatCoze",
    "ChatOctoAI",
    "ChatDatabricks",
    "ChatDeepInfra",
    "ChatEdenAI",
    "ChatEverlyAI",
    "ChatFireworks",
    "ChatFriendli",
    "ChatGooglePalm",
    "ChatHuggingFace",
    "ChatHunyuan",
    "ChatJavelinAIGateway",
    "ChatKinetica",
    "ChatKonko",
    "ChatLiteLLM",
    "ChatLiteLLMRouter",
    "ChatMLX",
    "ChatMLflowAIGateway",
    "ChatMaritalk",
    "ChatMlflow",
    "ChatNebula",
    "ChatOCIGenAI",
    "ChatOCIModelDeployment",
    "ChatOCIModelDeploymentVLLM",
    "ChatOCIModelDeploymentTGI",
    "ChatOllama",
    "ChatOpenAI",
    "ChatOutlines",
    "ChatPerplexity",
    "ChatReka",
    "ChatPremAI",
    "ChatSambaNovaCloud",
    "ChatSambaStudio",
    "ChatSparkLLM",
    "ChatSnowflakeCortex",
    "ChatTongyi",
    "ChatVertexAI",
    "ChatYandexGPT",
    "ChatYuan2",
    "ChatZhipuAI",
    "ChatLlamaCpp",
    "ErnieBotChat",
    "FakeListChatModel",
    "GPTRouter",
    "GigaChat",
    "HumanInputChatModel",
    "JinaChat",
    "LlamaEdgeChatService",
    "MiniMaxChat",
    "MoonshotChat",
    "PaiEasChatEndpoint",
    "PromptLayerChatOpenAI",
    "QianfanChatEndpoint",
    "SolarChat",
    "VolcEngineMaasChat",
    "ChatYi",
]


_module_lookup = {
    "AzureChatOpenAI": "aibaba_ai_community.chat_models.azure_openai",
    "BedrockChat": "aibaba_ai_community.chat_models.bedrock",
    "ChatAnthropic": "aibaba_ai_community.chat_models.anthropic",
    "ChatAnyscale": "aibaba_ai_community.chat_models.anyscale",
    "ChatBaichuan": "aibaba_ai_community.chat_models.baichuan",
    "ChatClovaX": "aibaba_ai_community.chat_models.naver",
    "ChatCohere": "aibaba_ai_community.chat_models.cohere",
    "ChatCoze": "aibaba_ai_community.chat_models.coze",
    "ChatDatabricks": "aibaba_ai_community.chat_models.databricks",
    "ChatDeepInfra": "aibaba_ai_community.chat_models.deepinfra",
    "ChatEverlyAI": "aibaba_ai_community.chat_models.everlyai",
    "ChatEdenAI": "aibaba_ai_community.chat_models.edenai",
    "ChatFireworks": "aibaba_ai_community.chat_models.fireworks",
    "ChatFriendli": "aibaba_ai_community.chat_models.friendli",
    "ChatGooglePalm": "aibaba_ai_community.chat_models.google_palm",
    "ChatHuggingFace": "aibaba_ai_community.chat_models.huggingface",
    "ChatHunyuan": "aibaba_ai_community.chat_models.hunyuan",
    "ChatJavelinAIGateway": "aibaba_ai_community.chat_models.javelin_ai_gateway",
    "ChatKinetica": "aibaba_ai_community.chat_models.kinetica",
    "ChatKonko": "aibaba_ai_community.chat_models.konko",
    "ChatLiteLLM": "aibaba_ai_community.chat_models.litellm",
    "ChatLiteLLMRouter": "aibaba_ai_community.chat_models.litellm_router",
    "ChatMLflowAIGateway": "aibaba_ai_community.chat_models.mlflow_ai_gateway",
    "ChatMLX": "aibaba_ai_community.chat_models.mlx",
    "ChatMaritalk": "aibaba_ai_community.chat_models.maritalk",
    "ChatMlflow": "aibaba_ai_community.chat_models.mlflow",
    "ChatNebula": "aibaba_ai_community.chat_models.symblai_nebula",
    "ChatOctoAI": "aibaba_ai_community.chat_models.octoai",
    "ChatOCIGenAI": "aibaba_ai_community.chat_models.oci_generative_ai",
    "ChatOCIModelDeployment": "aibaba_ai_community.chat_models.oci_data_science",
    "ChatOCIModelDeploymentVLLM": "aibaba_ai_community.chat_models.oci_data_science",
    "ChatOCIModelDeploymentTGI": "aibaba_ai_community.chat_models.oci_data_science",
    "ChatOllama": "aibaba_ai_community.chat_models.ollama",
    "ChatOpenAI": "aibaba_ai_community.chat_models.openai",
    "ChatOutlines": "aibaba_ai_community.chat_models.outlines",
    "ChatReka": "aibaba_ai_community.chat_models.reka",
    "ChatPerplexity": "aibaba_ai_community.chat_models.perplexity",
    "ChatSambaNovaCloud": "aibaba_ai_community.chat_models.sambanova",
    "ChatSambaStudio": "aibaba_ai_community.chat_models.sambanova",
    "ChatSnowflakeCortex": "aibaba_ai_community.chat_models.snowflake",
    "ChatSparkLLM": "aibaba_ai_community.chat_models.sparkllm",
    "ChatTongyi": "aibaba_ai_community.chat_models.tongyi",
    "ChatVertexAI": "aibaba_ai_community.chat_models.vertexai",
    "ChatYandexGPT": "aibaba_ai_community.chat_models.yandex",
    "ChatYuan2": "aibaba_ai_community.chat_models.yuan2",
    "ChatZhipuAI": "aibaba_ai_community.chat_models.zhipuai",
    "ErnieBotChat": "aibaba_ai_community.chat_models.ernie",
    "FakeListChatModel": "aibaba_ai_community.chat_models.fake",
    "GPTRouter": "aibaba_ai_community.chat_models.gpt_router",
    "GigaChat": "aibaba_ai_community.chat_models.gigachat",
    "HumanInputChatModel": "aibaba_ai_community.chat_models.human",
    "JinaChat": "aibaba_ai_community.chat_models.jinachat",
    "LlamaEdgeChatService": "aibaba_ai_community.chat_models.llama_edge",
    "MiniMaxChat": "aibaba_ai_community.chat_models.minimax",
    "MoonshotChat": "aibaba_ai_community.chat_models.moonshot",
    "PaiEasChatEndpoint": "aibaba_ai_community.chat_models.pai_eas_endpoint",
    "PromptLayerChatOpenAI": "aibaba_ai_community.chat_models.promptlayer_openai",
    "SolarChat": "aibaba_ai_community.chat_models.solar",
    "QianfanChatEndpoint": "aibaba_ai_community.chat_models.baidu_qianfan_endpoint",
    "VolcEngineMaasChat": "aibaba_ai_community.chat_models.volcengine_maas",
    "ChatPremAI": "aibaba_ai_community.chat_models.premai",
    "ChatLlamaCpp": "aibaba_ai_community.chat_models.llamacpp",
    "ChatYi": "aibaba_ai_community.chat_models.yi",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
