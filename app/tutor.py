from .pdf_processor import PDFProcessor
from .vector_store import VectorStoreManager
from .llm_connector import LLMConnector

class IndianCurriculumTutor:
    def __init__(self):
        self.documents = PDFProcessor.load_and_chunk()
        self.vector_store = VectorStoreManager.create_store(self.documents)
        self.llm = LLMConnector.initialize()
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

    def answer_question(self, question: str) -> str:
        try:
            docs = self.retriever.get_relevant_documents(question)
            context = "\n\n".join(d.page_content for d in docs)
            prompt = f"""You are an expert Indian curriculum tutor. Guidelines:
1. Use only the provided context
2. Answer in simple English/Hindi
3. Provide examples
4. Be academically precise

Context:
{context}

Question: {question}
Answer:"""
            return self.llm.invoke(prompt).content
        except Exception as e:
            return f"Error: {str(e)}"