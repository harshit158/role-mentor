from typing import Any, Dict, List, Optional
from langchain_core.messages import BaseMessage
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.chat_models import BaseChatModel
import lmstudio as lms

class LocalLlama(BaseChatModel):
    def _generate(self, 
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,) -> str:
        
        model = lms.llm("meta-llama-3.1-8b-instruct")
        result = model.respond(messages)
        return result
    
    @property
    def _llm_type(self) -> str:
        return "local-llama"