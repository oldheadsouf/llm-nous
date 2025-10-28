import llm
from llm.default_plugins.openai_models import Chat

# Try to import AsyncChat, but don't fail if it's not available
try:
    from llm.default_plugins.openai_models import AsyncChat

    HAS_ASYNC = True
except ImportError:
    HAS_ASYNC = False

MODELS = (
    "Hermes-4-405B",
    "Hermes-4-70B"
)


class NousChat(Chat):
    needs_key = "nous"
    key_env_var = "NOUS_API_KEY"

    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=model_name,
            api_base="https://inference-api.nousresearch.com/v1",
        )

    def __str__(self):
        return "Nous: {}".format(self.model_id)


# Only define AsyncChat class if async support is available
if HAS_ASYNC:

    class NousAsyncChat(AsyncChat):
        needs_key = "nous"
        key_env_var = "NOUS_API_KEY"

        def __init__(self, model_name):
            super().__init__(
                model_name=model_name,
                model_id=model_name,
                api_base="https://inference-api.nousresearch.com/v1",
            )

        def __str__(self):
            return "Nous: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "nous", NousChat.key_env_var)
    if not key:
        return
    for model_id in MODELS:
        if HAS_ASYNC:
            register(
                NousChat(model_id),
                NousAsyncChat(model_id),
            )
        else:
            register(NousChat(model_id))
