from langchain_openai import ChatOpenAI
from .config import Config
import os

config = Config()

class LLMConnector:
    @staticmethod
    def initialize():
        if config.api_provider == "openrouter":
            return ChatOpenAI(
                model=config.model_name,
                temperature=0.3,
                max_tokens=800,
                openai_api_key=os.getenv("OPENROUTER_API_KEY"),
                openai_api_base="https://openrouter.ai/api/v1"
            )
        return ChatOpenAI(
            model=config.model_name,
            temperature=0.3,
            max_tokens=800,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )