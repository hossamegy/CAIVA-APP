from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS


class CreateVectorStore:
    """
    Manages the creation of a vector store from PDF documents using LangChain.

    Attributes:
        paths (list): File paths to PDF documents.
        embeddings (object): Embedding model instance.
        list_of_docs (list): Raw documents loaded from paths.
        formatted_docs (list): Documents with updated metadata.
        chunks (list): Document chunks after splitting.
        vectorstore (FAISS): Resulting FAISS vector store.
    """

    def __init__(self, paths, embeddings):
        """
        Initializes with document paths and embeddings.

        Args:
            paths (list): PDF document file paths.
            embeddings (object): Embedding model instance.
        """
        self.paths = paths
        self.embeddings = embeddings
        self.list_of_docs = self.load_documents(self.paths)
        self.chunks = self.documents_splitter(self.list_of_docs)
        self.vectorstore = self.create_vector_store()

    def __call__(self):
        """
        Returns the created FAISS vector store.

        Returns:
            FAISS: The FAISS vector store instance.
        """
        return self.vectorstore

    def load_documents(self, paths: list) -> list:
        """
        Loads PDF documents from specified paths.

        Args:
            paths (list): PDF document file paths.

        Returns:
            list: List of loaded documents.
        """
        list_of_docs = []
        for path in paths:
            loader = PyPDFLoader(path)
            docs = loader.load()
            list_of_docs.extend(docs)
        return list_of_docs

    def documents_splitter(self, documents: list) -> list:
        """
        Splits documents into chunks.

        Args:
            documents (list): List of documents to be split.

        Returns:
            list: List of document chunks.
        """
        splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=1000)
        chunks = splitter.split_documents(documents)
        return chunks

    def create_vector_store(self):
        """
        Creates a FAISS vector store from document chunks.

        Returns:
            FAISS: The created FAISS vector store.
        """
        vectorstore = FAISS.from_documents(self.chunks, self.embeddings)
        return vectorstore
