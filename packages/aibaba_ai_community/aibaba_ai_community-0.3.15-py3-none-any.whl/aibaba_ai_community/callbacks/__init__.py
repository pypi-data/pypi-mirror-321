"""**Callback handlers** allow listening to events in Aibaba AI.

**Class hierarchy:**

.. code-block::

    BaseCallbackHandler --> <name>CallbackHandler  # Example: AimCallbackHandler
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.callbacks.aim_callback import (
        AimCallbackHandler,
    )
    from aibaba_ai_community.callbacks.argilla_callback import (
        ArgillaCallbackHandler,
    )
    from aibaba_ai_community.callbacks.arize_callback import (
        ArizeCallbackHandler,
    )
    from aibaba_ai_community.callbacks.arthur_callback import (
        ArthurCallbackHandler,
    )
    from aibaba_ai_community.callbacks.clearml_callback import (
        ClearMLCallbackHandler,
    )
    from aibaba_ai_community.callbacks.comet_ml_callback import (
        CometCallbackHandler,
    )
    from aibaba_ai_community.callbacks.context_callback import (
        ContextCallbackHandler,
    )
    from aibaba_ai_community.callbacks.fiddler_callback import (
        FiddlerCallbackHandler,
    )
    from aibaba_ai_community.callbacks.flyte_callback import (
        FlyteCallbackHandler,
    )
    from aibaba_ai_community.callbacks.human import (
        HumanApprovalCallbackHandler,
    )
    from aibaba_ai_community.callbacks.infino_callback import (
        InfinoCallbackHandler,
    )
    from aibaba_ai_community.callbacks.labelstudio_callback import (
        LabelStudioCallbackHandler,
    )
    from aibaba_ai_community.callbacks.llmonitor_callback import (
        LLMonitorCallbackHandler,
    )
    from aibaba_ai_community.callbacks.manager import (
        get_openai_callback,
        wandb_tracing_enabled,
    )
    from aibaba_ai_community.callbacks.mlflow_callback import (
        MlflowCallbackHandler,
    )
    from aibaba_ai_community.callbacks.openai_info import (
        OpenAICallbackHandler,
    )
    from aibaba_ai_community.callbacks.promptlayer_callback import (
        PromptLayerCallbackHandler,
    )
    from aibaba_ai_community.callbacks.sagemaker_callback import (
        SageMakerCallbackHandler,
    )
    from aibaba_ai_community.callbacks.streamlit import (
        LLMThoughtLabeler,
        StreamlitCallbackHandler,
    )
    from aibaba_ai_community.callbacks.trubrics_callback import (
        TrubricsCallbackHandler,
    )
    from aibaba_ai_community.callbacks.upstash_ratelimit_callback import (
        UpstashRatelimitError,
        UpstashRatelimitHandler,  # noqa: F401
    )
    from aibaba_ai_community.callbacks.uptrain_callback import (
        UpTrainCallbackHandler,
    )
    from aibaba_ai_community.callbacks.wandb_callback import (
        WandbCallbackHandler,
    )
    from aibaba_ai_community.callbacks.whylabs_callback import (
        WhyLabsCallbackHandler,
    )


_module_lookup = {
    "AimCallbackHandler": "aibaba_ai_community.callbacks.aim_callback",
    "ArgillaCallbackHandler": "aibaba_ai_community.callbacks.argilla_callback",
    "ArizeCallbackHandler": "aibaba_ai_community.callbacks.arize_callback",
    "ArthurCallbackHandler": "aibaba_ai_community.callbacks.arthur_callback",
    "ClearMLCallbackHandler": "aibaba_ai_community.callbacks.clearml_callback",
    "CometCallbackHandler": "aibaba_ai_community.callbacks.comet_ml_callback",
    "ContextCallbackHandler": "aibaba_ai_community.callbacks.context_callback",
    "FiddlerCallbackHandler": "aibaba_ai_community.callbacks.fiddler_callback",
    "FlyteCallbackHandler": "aibaba_ai_community.callbacks.flyte_callback",
    "HumanApprovalCallbackHandler": "aibaba_ai_community.callbacks.human",
    "InfinoCallbackHandler": "aibaba_ai_community.callbacks.infino_callback",
    "LLMThoughtLabeler": "aibaba_ai_community.callbacks.streamlit",
    "LLMonitorCallbackHandler": "aibaba_ai_community.callbacks.llmonitor_callback",
    "LabelStudioCallbackHandler": "aibaba_ai_community.callbacks.labelstudio_callback",
    "MlflowCallbackHandler": "aibaba_ai_community.callbacks.mlflow_callback",
    "OpenAICallbackHandler": "aibaba_ai_community.callbacks.openai_info",
    "PromptLayerCallbackHandler": "aibaba_ai_community.callbacks.promptlayer_callback",
    "SageMakerCallbackHandler": "aibaba_ai_community.callbacks.sagemaker_callback",
    "StreamlitCallbackHandler": "aibaba_ai_community.callbacks.streamlit",
    "TrubricsCallbackHandler": "aibaba_ai_community.callbacks.trubrics_callback",
    "UpstashRatelimitError": "aibaba_ai_community.callbacks.upstash_ratelimit_callback",
    "UpstashRatelimitHandler": "aibaba_ai_community.callbacks.upstash_ratelimit_callback",  # noqa
    "UpTrainCallbackHandler": "aibaba_ai_community.callbacks.uptrain_callback",
    "WandbCallbackHandler": "aibaba_ai_community.callbacks.wandb_callback",
    "WhyLabsCallbackHandler": "aibaba_ai_community.callbacks.whylabs_callback",
    "get_openai_callback": "aibaba_ai_community.callbacks.manager",
    "wandb_tracing_enabled": "aibaba_ai_community.callbacks.manager",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "AimCallbackHandler",
    "ArgillaCallbackHandler",
    "ArizeCallbackHandler",
    "ArthurCallbackHandler",
    "ClearMLCallbackHandler",
    "CometCallbackHandler",
    "ContextCallbackHandler",
    "FiddlerCallbackHandler",
    "FlyteCallbackHandler",
    "HumanApprovalCallbackHandler",
    "InfinoCallbackHandler",
    "LLMThoughtLabeler",
    "LLMonitorCallbackHandler",
    "LabelStudioCallbackHandler",
    "MlflowCallbackHandler",
    "OpenAICallbackHandler",
    "PromptLayerCallbackHandler",
    "SageMakerCallbackHandler",
    "StreamlitCallbackHandler",
    "TrubricsCallbackHandler",
    "UpstashRatelimitError",
    "UpstashRatelimitHandler",
    "UpTrainCallbackHandler",
    "WandbCallbackHandler",
    "WhyLabsCallbackHandler",
    "get_openai_callback",
    "wandb_tracing_enabled",
]
