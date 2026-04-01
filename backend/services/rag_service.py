from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Tuple
import os
from config import CHROMA_DB_DIR, EMBEDDING_MODEL


class RAGService:
    def __init__(self):
        self.embeddings = None  # Lazy load on first use
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        self.vectorstore = None
    
    def _init_embeddings(self):
        """Lazy initialize embeddings model"""
        if self.embeddings is None:
            self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    def create_vectorstore(self, marking_scheme_text: str, persist_dir: str):
        """Create vector store from marking scheme"""
        try:
            self._init_embeddings()  # Initialize embeddings on first use
            chunks = self.text_splitter.split_text(marking_scheme_text)
            self.vectorstore = Chroma.from_texts(
                texts=chunks,
                embedding=self.embeddings,
                persist_directory=persist_dir
            )
            return self.vectorstore
        except Exception as e:
            raise Exception(f"RAG Service Error: {str(e)}")

    def load_vectorstore(self, persist_dir: str):
        """Load existing vector store"""
        try:
            self._init_embeddings()  # Initialize embeddings on first use
            self.vectorstore = Chroma(
                persist_directory=persist_dir,
                embedding_function=self.embeddings
            )
            return self.vectorstore
        except Exception as e:
            raise Exception(f"RAG Service Error: {str(e)}")

    def retrieve_relevant_criteria(self, query: str, k: int = 3) -> List[str]:
        """Retrieve relevant marking criteria based on query"""
        if not self.vectorstore:
            raise Exception("Vector store not initialized")
        
        try:
            results = self.vectorstore.similarity_search(query, k=k)
            return [result.page_content for result in results]
        except Exception as e:
            raise Exception(f"Retrieval Error: {str(e)}")

    def get_context_for_evaluation(self, answer_text: str, k: int = 5) -> str:
        """Get relevant marking criteria context for answer evaluation"""
        criteria = self.retrieve_relevant_criteria(answer_text, k=k)
        return "\n".join(criteria)
