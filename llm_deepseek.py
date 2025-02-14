import llm
from llm.default_plugins.openai_models import Chat

# Try to import AsyncChat, but don't fail if it's not available
try:
    from llm.default_plugins.openai_models import AsyncChat

    HAS_ASYNC = True
except ImportError:
    HAS_ASYNC = False

MODELS = (
    "deepseek-chat",
    "deepseek-coder",
    "deepseek-reasoner",
)


class DeepSeekChat(Chat):
    needs_key = "deepseek"

    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=model_name,
            api_base="https://api.deepseek.com",
        )

    def __str__(self):
        return "DeepSeek: {}".format(self.model_id)


# Only define AsyncChat class if async support is available
if HAS_ASYNC:

    class DeepSeekAsyncChat(AsyncChat):
        needs_key = "deepseek"

        def __init__(self, model_name):
            super().__init__(
                model_name=model_name,
                model_id=model_name,
                api_base="https://api.deepseek.com",
            )

        def __str__(self):
            return "DeepSeek: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "deepseek", "LLM_DEEPSEEK_KEY")
    if not key:
        return
    for model_id in MODELS:
        if HAS_ASYNC:
            register(
                DeepSeekChat(model_id),
                DeepSeekAsyncChat(model_id),
            )
        else:
            register(DeepSeekChat(model_id))
