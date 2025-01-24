"""**Embedding models**  are wrappers around embedding models
from different APIs and services.

**Embedding models** can be LLMs or not.

**Class hierarchy:**

.. code-block::

    Embeddings --> <name>Embeddings  # Examples: OpenAIEmbeddings, HuggingFaceEmbeddings
"""

import importlib
import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.embeddings.aleph_alpha import (
        AlephAlphaAsymmetricSemanticEmbedding,
        AlephAlphaSymmetricSemanticEmbedding,
    )
    from aibaba_ai_community.embeddings.anyscale import (
        AnyscaleEmbeddings,
    )
    from aibaba_ai_community.embeddings.ascend import (
        AscendEmbeddings,
    )
    from aibaba_ai_community.embeddings.awa import (
        AwaEmbeddings,
    )
    from aibaba_ai_community.embeddings.azure_openai import (
        AzureOpenAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.baichuan import (
        BaichuanTextEmbeddings,
    )
    from aibaba_ai_community.embeddings.baidu_qianfan_endpoint import (
        QianfanEmbeddingsEndpoint,
    )
    from aibaba_ai_community.embeddings.bedrock import (
        BedrockEmbeddings,
    )
    from aibaba_ai_community.embeddings.bookend import (
        BookendEmbeddings,
    )
    from aibaba_ai_community.embeddings.clarifai import (
        ClarifaiEmbeddings,
    )
    from aibaba_ai_community.embeddings.clova import (
        ClovaEmbeddings,
    )
    from aibaba_ai_community.embeddings.cohere import (
        CohereEmbeddings,
    )
    from aibaba_ai_community.embeddings.dashscope import (
        DashScopeEmbeddings,
    )
    from aibaba_ai_community.embeddings.databricks import (
        DatabricksEmbeddings,
    )
    from aibaba_ai_community.embeddings.deepinfra import (
        DeepInfraEmbeddings,
    )
    from aibaba_ai_community.embeddings.edenai import (
        EdenAiEmbeddings,
    )
    from aibaba_ai_community.embeddings.elasticsearch import (
        ElasticsearchEmbeddings,
    )
    from aibaba_ai_community.embeddings.embaas import (
        EmbaasEmbeddings,
    )
    from aibaba_ai_community.embeddings.ernie import (
        ErnieEmbeddings,
    )
    from aibaba_ai_community.embeddings.fake import (
        DeterministicFakeEmbedding,
        FakeEmbeddings,
    )
    from aibaba_ai_community.embeddings.fastembed import (
        FastEmbedEmbeddings,
    )
    from aibaba_ai_community.embeddings.gigachat import (
        GigaChatEmbeddings,
    )
    from aibaba_ai_community.embeddings.google_palm import (
        GooglePalmEmbeddings,
    )
    from aibaba_ai_community.embeddings.gpt4all import (
        GPT4AllEmbeddings,
    )
    from aibaba_ai_community.embeddings.gradient_ai import (
        GradientEmbeddings,
    )
    from aibaba_ai_community.embeddings.huggingface import (
        HuggingFaceBgeEmbeddings,
        HuggingFaceEmbeddings,
        HuggingFaceInferenceAPIEmbeddings,
        HuggingFaceInstructEmbeddings,
    )
    from aibaba_ai_community.embeddings.huggingface_hub import (
        HuggingFaceHubEmbeddings,
    )
    from aibaba_ai_community.embeddings.hunyuan import (
        HunyuanEmbeddings,
    )
    from aibaba_ai_community.embeddings.infinity import (
        InfinityEmbeddings,
    )
    from aibaba_ai_community.embeddings.infinity_local import (
        InfinityEmbeddingsLocal,
    )
    from aibaba_ai_community.embeddings.ipex_llm import IpexLLMBgeEmbeddings
    from aibaba_ai_community.embeddings.itrex import (
        QuantizedBgeEmbeddings,
    )
    from aibaba_ai_community.embeddings.javelin_ai_gateway import (
        JavelinAIGatewayEmbeddings,
    )
    from aibaba_ai_community.embeddings.jina import (
        JinaEmbeddings,
    )
    from aibaba_ai_community.embeddings.johnsnowlabs import (
        JohnSnowLabsEmbeddings,
    )
    from aibaba_ai_community.embeddings.laser import (
        LaserEmbeddings,
    )
    from aibaba_ai_community.embeddings.llamacpp import (
        LlamaCppEmbeddings,
    )
    from aibaba_ai_community.embeddings.llamafile import (
        LlamafileEmbeddings,
    )
    from aibaba_ai_community.embeddings.llm_rails import (
        LLMRailsEmbeddings,
    )
    from aibaba_ai_community.embeddings.localai import (
        LocalAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.minimax import (
        MiniMaxEmbeddings,
    )
    from aibaba_ai_community.embeddings.mlflow import (
        MlflowCohereEmbeddings,
        MlflowEmbeddings,
    )
    from aibaba_ai_community.embeddings.mlflow_gateway import (
        MlflowAIGatewayEmbeddings,
    )
    from aibaba_ai_community.embeddings.model2vec import (
        Model2vecEmbeddings,
    )
    from aibaba_ai_community.embeddings.modelscope_hub import (
        ModelScopeEmbeddings,
    )
    from aibaba_ai_community.embeddings.mosaicml import (
        MosaicMLInstructorEmbeddings,
    )
    from aibaba_ai_community.embeddings.naver import (
        ClovaXEmbeddings,
    )
    from aibaba_ai_community.embeddings.nemo import (
        NeMoEmbeddings,
    )
    from aibaba_ai_community.embeddings.nlpcloud import (
        NLPCloudEmbeddings,
    )
    from aibaba_ai_community.embeddings.oci_generative_ai import (
        OCIGenAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.octoai_embeddings import (
        OctoAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.ollama import (
        OllamaEmbeddings,
    )
    from aibaba_ai_community.embeddings.openai import (
        OpenAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.openvino import (
        OpenVINOBgeEmbeddings,
        OpenVINOEmbeddings,
    )
    from aibaba_ai_community.embeddings.optimum_intel import (
        QuantizedBiEncoderEmbeddings,
    )
    from aibaba_ai_community.embeddings.oracleai import (
        OracleEmbeddings,
    )
    from aibaba_ai_community.embeddings.ovhcloud import (
        OVHCloudEmbeddings,
    )
    from aibaba_ai_community.embeddings.premai import (
        PremAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.sagemaker_endpoint import (
        SagemakerEndpointEmbeddings,
    )
    from aibaba_ai_community.embeddings.sambanova import (
        SambaStudioEmbeddings,
    )
    from aibaba_ai_community.embeddings.self_hosted import (
        SelfHostedEmbeddings,
    )
    from aibaba_ai_community.embeddings.self_hosted_hugging_face import (
        SelfHostedHuggingFaceEmbeddings,
        SelfHostedHuggingFaceInstructEmbeddings,
    )
    from aibaba_ai_community.embeddings.sentence_transformer import (
        SentenceTransformerEmbeddings,
    )
    from aibaba_ai_community.embeddings.solar import (
        SolarEmbeddings,
    )
    from aibaba_ai_community.embeddings.spacy_embeddings import (
        SpacyEmbeddings,
    )
    from aibaba_ai_community.embeddings.sparkllm import (
        SparkLLMTextEmbeddings,
    )
    from aibaba_ai_community.embeddings.tensorflow_hub import (
        TensorflowHubEmbeddings,
    )
    from aibaba_ai_community.embeddings.textembed import (
        TextEmbedEmbeddings,
    )
    from aibaba_ai_community.embeddings.titan_takeoff import (
        TitanTakeoffEmbed,
    )
    from aibaba_ai_community.embeddings.vertexai import (
        VertexAIEmbeddings,
    )
    from aibaba_ai_community.embeddings.volcengine import (
        VolcanoEmbeddings,
    )
    from aibaba_ai_community.embeddings.voyageai import (
        VoyageEmbeddings,
    )
    from aibaba_ai_community.embeddings.xinference import (
        XinferenceEmbeddings,
    )
    from aibaba_ai_community.embeddings.yandex import (
        YandexGPTEmbeddings,
    )
    from aibaba_ai_community.embeddings.zhipuai import (
        ZhipuAIEmbeddings,
    )

__all__ = [
    "AlephAlphaAsymmetricSemanticEmbedding",
    "AlephAlphaSymmetricSemanticEmbedding",
    "AnyscaleEmbeddings",
    "AscendEmbeddings",
    "AwaEmbeddings",
    "AzureOpenAIEmbeddings",
    "BaichuanTextEmbeddings",
    "BedrockEmbeddings",
    "BookendEmbeddings",
    "ClarifaiEmbeddings",
    "ClovaEmbeddings",
    "ClovaXEmbeddings",
    "CohereEmbeddings",
    "DashScopeEmbeddings",
    "DatabricksEmbeddings",
    "DeepInfraEmbeddings",
    "DeterministicFakeEmbedding",
    "EdenAiEmbeddings",
    "ElasticsearchEmbeddings",
    "EmbaasEmbeddings",
    "ErnieEmbeddings",
    "FakeEmbeddings",
    "FastEmbedEmbeddings",
    "GPT4AllEmbeddings",
    "GigaChatEmbeddings",
    "GooglePalmEmbeddings",
    "GradientEmbeddings",
    "HuggingFaceBgeEmbeddings",
    "HuggingFaceEmbeddings",
    "HuggingFaceHubEmbeddings",
    "HuggingFaceInferenceAPIEmbeddings",
    "HuggingFaceInstructEmbeddings",
    "InfinityEmbeddings",
    "InfinityEmbeddingsLocal",
    "IpexLLMBgeEmbeddings",
    "JavelinAIGatewayEmbeddings",
    "JinaEmbeddings",
    "JohnSnowLabsEmbeddings",
    "LLMRailsEmbeddings",
    "LaserEmbeddings",
    "LlamaCppEmbeddings",
    "LlamafileEmbeddings",
    "LocalAIEmbeddings",
    "MiniMaxEmbeddings",
    "MlflowAIGatewayEmbeddings",
    "MlflowCohereEmbeddings",
    "MlflowEmbeddings",
    "Model2vecEmbeddings",
    "ModelScopeEmbeddings",
    "MosaicMLInstructorEmbeddings",
    "NLPCloudEmbeddings",
    "NeMoEmbeddings",
    "OCIGenAIEmbeddings",
    "OctoAIEmbeddings",
    "OllamaEmbeddings",
    "OpenAIEmbeddings",
    "OpenVINOBgeEmbeddings",
    "OpenVINOEmbeddings",
    "OracleEmbeddings",
    "OVHCloudEmbeddings",
    "PremAIEmbeddings",
    "QianfanEmbeddingsEndpoint",
    "QuantizedBgeEmbeddings",
    "QuantizedBiEncoderEmbeddings",
    "SagemakerEndpointEmbeddings",
    "SambaStudioEmbeddings",
    "SelfHostedEmbeddings",
    "SelfHostedHuggingFaceEmbeddings",
    "SelfHostedHuggingFaceInstructEmbeddings",
    "SentenceTransformerEmbeddings",
    "SolarEmbeddings",
    "SpacyEmbeddings",
    "SparkLLMTextEmbeddings",
    "TensorflowHubEmbeddings",
    "TextEmbedEmbeddings",
    "TitanTakeoffEmbed",
    "VertexAIEmbeddings",
    "VolcanoEmbeddings",
    "VoyageEmbeddings",
    "XinferenceEmbeddings",
    "YandexGPTEmbeddings",
    "ZhipuAIEmbeddings",
    "HunyuanEmbeddings",
]

_module_lookup = {
    "AlephAlphaAsymmetricSemanticEmbedding": "aibaba_ai_community.embeddings.aleph_alpha",  # noqa: E501
    "AlephAlphaSymmetricSemanticEmbedding": "aibaba_ai_community.embeddings.aleph_alpha",  # noqa: E501
    "AnyscaleEmbeddings": "aibaba_ai_community.embeddings.anyscale",
    "AwaEmbeddings": "aibaba_ai_community.embeddings.awa",
    "AzureOpenAIEmbeddings": "aibaba_ai_community.embeddings.azure_openai",
    "BaichuanTextEmbeddings": "aibaba_ai_community.embeddings.baichuan",
    "BedrockEmbeddings": "aibaba_ai_community.embeddings.bedrock",
    "BookendEmbeddings": "aibaba_ai_community.embeddings.bookend",
    "ClarifaiEmbeddings": "aibaba_ai_community.embeddings.clarifai",
    "ClovaEmbeddings": "aibaba_ai_community.embeddings.clova",
    "ClovaXEmbeddings": "aibaba_ai_community.embeddings.naver",
    "CohereEmbeddings": "aibaba_ai_community.embeddings.cohere",
    "DashScopeEmbeddings": "aibaba_ai_community.embeddings.dashscope",
    "DatabricksEmbeddings": "aibaba_ai_community.embeddings.databricks",
    "DeepInfraEmbeddings": "aibaba_ai_community.embeddings.deepinfra",
    "DeterministicFakeEmbedding": "aibaba_ai_community.embeddings.fake",
    "EdenAiEmbeddings": "aibaba_ai_community.embeddings.edenai",
    "ElasticsearchEmbeddings": "aibaba_ai_community.embeddings.elasticsearch",
    "EmbaasEmbeddings": "aibaba_ai_community.embeddings.embaas",
    "ErnieEmbeddings": "aibaba_ai_community.embeddings.ernie",
    "FakeEmbeddings": "aibaba_ai_community.embeddings.fake",
    "FastEmbedEmbeddings": "aibaba_ai_community.embeddings.fastembed",
    "GPT4AllEmbeddings": "aibaba_ai_community.embeddings.gpt4all",
    "GooglePalmEmbeddings": "aibaba_ai_community.embeddings.google_palm",
    "GradientEmbeddings": "aibaba_ai_community.embeddings.gradient_ai",
    "GigaChatEmbeddings": "aibaba_ai_community.embeddings.gigachat",
    "HuggingFaceBgeEmbeddings": "aibaba_ai_community.embeddings.huggingface",
    "HuggingFaceEmbeddings": "aibaba_ai_community.embeddings.huggingface",
    "HuggingFaceHubEmbeddings": "aibaba_ai_community.embeddings.huggingface_hub",
    "HuggingFaceInferenceAPIEmbeddings": "aibaba_ai_community.embeddings.huggingface",
    "HuggingFaceInstructEmbeddings": "aibaba_ai_community.embeddings.huggingface",
    "InfinityEmbeddings": "aibaba_ai_community.embeddings.infinity",
    "InfinityEmbeddingsLocal": "aibaba_ai_community.embeddings.infinity_local",
    "IpexLLMBgeEmbeddings": "aibaba_ai_community.embeddings.ipex_llm",
    "JavelinAIGatewayEmbeddings": "aibaba_ai_community.embeddings.javelin_ai_gateway",
    "JinaEmbeddings": "aibaba_ai_community.embeddings.jina",
    "JohnSnowLabsEmbeddings": "aibaba_ai_community.embeddings.johnsnowlabs",
    "LLMRailsEmbeddings": "aibaba_ai_community.embeddings.llm_rails",
    "LaserEmbeddings": "aibaba_ai_community.embeddings.laser",
    "LlamaCppEmbeddings": "aibaba_ai_community.embeddings.llamacpp",
    "LlamafileEmbeddings": "aibaba_ai_community.embeddings.llamafile",
    "LocalAIEmbeddings": "aibaba_ai_community.embeddings.localai",
    "MiniMaxEmbeddings": "aibaba_ai_community.embeddings.minimax",
    "MlflowAIGatewayEmbeddings": "aibaba_ai_community.embeddings.mlflow_gateway",
    "MlflowCohereEmbeddings": "aibaba_ai_community.embeddings.mlflow",
    "MlflowEmbeddings": "aibaba_ai_community.embeddings.mlflow",
    "Model2vecEmbeddings": "aibaba_ai_community.embeddings.model2vec",
    "ModelScopeEmbeddings": "aibaba_ai_community.embeddings.modelscope_hub",
    "MosaicMLInstructorEmbeddings": "aibaba_ai_community.embeddings.mosaicml",
    "NLPCloudEmbeddings": "aibaba_ai_community.embeddings.nlpcloud",
    "NeMoEmbeddings": "aibaba_ai_community.embeddings.nemo",
    "OCIGenAIEmbeddings": "aibaba_ai_community.embeddings.oci_generative_ai",
    "OctoAIEmbeddings": "aibaba_ai_community.embeddings.octoai_embeddings",
    "OllamaEmbeddings": "aibaba_ai_community.embeddings.ollama",
    "OpenAIEmbeddings": "aibaba_ai_community.embeddings.openai",
    "OpenVINOEmbeddings": "aibaba_ai_community.embeddings.openvino",
    "OpenVINOBgeEmbeddings": "aibaba_ai_community.embeddings.openvino",
    "QianfanEmbeddingsEndpoint": "aibaba_ai_community.embeddings.baidu_qianfan_endpoint",  # noqa: E501
    "QuantizedBgeEmbeddings": "aibaba_ai_community.embeddings.itrex",
    "QuantizedBiEncoderEmbeddings": "aibaba_ai_community.embeddings.optimum_intel",
    "OracleEmbeddings": "aibaba_ai_community.embeddings.oracleai",
    "OVHCloudEmbeddings": "aibaba_ai_community.embeddings.ovhcloud",
    "SagemakerEndpointEmbeddings": "aibaba_ai_community.embeddings.sagemaker_endpoint",
    "SambaStudioEmbeddings": "aibaba_ai_community.embeddings.sambanova",
    "SelfHostedEmbeddings": "aibaba_ai_community.embeddings.self_hosted",
    "SelfHostedHuggingFaceEmbeddings": "aibaba_ai_community.embeddings.self_hosted_hugging_face",  # noqa: E501
    "SelfHostedHuggingFaceInstructEmbeddings": "aibaba_ai_community.embeddings.self_hosted_hugging_face",  # noqa: E501
    "SentenceTransformerEmbeddings": "aibaba_ai_community.embeddings.sentence_transformer",  # noqa: E501
    "SolarEmbeddings": "aibaba_ai_community.embeddings.solar",
    "SpacyEmbeddings": "aibaba_ai_community.embeddings.spacy_embeddings",
    "SparkLLMTextEmbeddings": "aibaba_ai_community.embeddings.sparkllm",
    "TensorflowHubEmbeddings": "aibaba_ai_community.embeddings.tensorflow_hub",
    "VertexAIEmbeddings": "aibaba_ai_community.embeddings.vertexai",
    "VolcanoEmbeddings": "aibaba_ai_community.embeddings.volcengine",
    "VoyageEmbeddings": "aibaba_ai_community.embeddings.voyageai",
    "XinferenceEmbeddings": "aibaba_ai_community.embeddings.xinference",
    "TextEmbedEmbeddings": "aibaba_ai_community.embeddings.textembed",
    "TitanTakeoffEmbed": "aibaba_ai_community.embeddings.titan_takeoff",
    "PremAIEmbeddings": "aibaba_ai_community.embeddings.premai",
    "YandexGPTEmbeddings": "aibaba_ai_community.embeddings.yandex",
    "AscendEmbeddings": "aibaba_ai_community.embeddings.ascend",
    "ZhipuAIEmbeddings": "aibaba_ai_community.embeddings.zhipuai",
    "HunyuanEmbeddings": "aibaba_ai_community.embeddings.hunyuan",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


logger = logging.getLogger(__name__)


# TODO: this is in here to maintain backwards compatibility
class HypotheticalDocumentEmbedder:
    def __init__(self, *args: Any, **kwargs: Any):
        logger.warning(
            "Using a deprecated class. Please use "
            "`from langchain.chains import HypotheticalDocumentEmbedder` instead"
        )
        from langchain.chains.hyde.base import HypotheticalDocumentEmbedder as H

        return H(*args, **kwargs)  # type: ignore

    @classmethod
    def from_llm(cls, *args: Any, **kwargs: Any) -> Any:
        logger.warning(
            "Using a deprecated class. Please use "
            "`from langchain.chains import HypotheticalDocumentEmbedder` instead"
        )
        from langchain.chains.hyde.base import HypotheticalDocumentEmbedder as H

        return H.from_llm(*args, **kwargs)
