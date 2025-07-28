from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .config import Config

config = Config()

class PDFProcessor:
    @staticmethod
    def load_and_chunk():
        loader = PyPDFLoader(config.pdf_path)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n\n", "\n", "।", "•", "॥", " ", ""]
        )
        return loader.load_and_split(splitter)