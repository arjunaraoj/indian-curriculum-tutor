from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from .config import Config

config = Config()

class VectorStoreManager:
    @staticmethod
    def create_store(documents):
        embeddings = HuggingFaceEmbeddings(
            model_name=config.embedding_model,
            model_kwargs={"device": config.device},
            encode_kwargs={"normalize_embeddings": True}
        )
        return FAISS.from_documents(documents, embeddings)