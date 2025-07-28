import os
from dotenv import load_dotenv
import torch

load_dotenv()

class Config:
    def __init__(self):
        self.pdf_path = os.getenv("PDF_PATH", "data/iemh101.pdf")
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.api_provider = os.getenv("API_PROVIDER", "openai").lower()
        self.model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
        self._validate()

    def _validate(self):
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF not found at: {self.pdf_path}")
        if self.api_provider == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
            raise ValueError("Missing OPENROUTER_API_KEY in .env")