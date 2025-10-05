from langchain_core.language_models.chat_models import BaseChatModel

class BaseLLM(BaseChatModel):
    def _generate(self, prompt: str) -> str:
        raise NotImplementedError

    @property
    def _llm_type():
        