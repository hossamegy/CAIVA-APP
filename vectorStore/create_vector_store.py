from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, JSONLoader
from langchain_community.vectorstores import FAISS

class VectorStoreCreator:
    """
    A class to streamline the process of creating a FAISS vector store from various document formats.

    Methods:
        __call__(paths, embeddings, loader_type='pdf'): 
            Orchestrates the document loading, splitting, and vector store creation process.

        load_documents(paths: list, loader_type: str) -> list: 
            Loads documents from the specified paths based on the document type.

        documents_splitter(documents: list) -> list: 
            Splits loaded documents into smaller chunks for vectorization.

        create_vector_store(chunks: list, embeddings): 
            Creates and returns a FAISS vector store from document chunks.
    """

    def __call__(self, paths: list, embeddings, loader_type: str = 'pdf'):
        """
        Facilitates the creation of a FAISS vector store from the provided document paths.

        Args:
            paths (list): List of document file paths.
            embeddings: Pre-trained embeddings model for vectorization.
            loader_type (str): Type of documents to load, e.g., 'pdf' or 'json'. Defaults to 'pdf'.

        Returns:
            FAISS: A FAISS vector store instance containing document embeddings.
        """
        documents = self.load_documents(paths, loader_type)
        document_chunks = self.documents_splitter(documents)
        vector_store = self.create_vector_store(document_chunks, embeddings)
        return vector_store

    def load_documents(self, paths: list, loader_type: str) -> list:
        """
        Loads documents from specified paths using appropriate loaders based on document type.

        Args:
            paths (list): A list of file paths to be loaded.
            loader_type (str): The type of documents to load ('pdf' or 'json').

        Returns:
            list: A list of documents loaded from the specified paths.
        
        Raises:
            ValueError: If an unsupported loader_type is provided.
        """
        loaded_documents = []
        for path in paths:
            if loader_type == 'pdf':
                loader = PyPDFLoader(path)
            elif loader_type == 'json':
                loader = JSONLoader(
                    file_path=path,
                    jq_schema=".user_information[]",
                    text_content=False
                )
            else:
                raise ValueError(f"Unsupported loader_type: {loader_type}")
            
            documents = loader.load()
            loaded_documents.extend(documents)
        
        return loaded_documents

    def documents_splitter(self, documents: list) -> list:
        """
        Splits documents into smaller chunks to facilitate better vectorization.

        Args:
            documents (list): A list of loaded documents to be split.

        Returns:
            list: A list of document chunks suitable for vectorization.
        """
        splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=1000)
        chunks = splitter.split_documents(documents)
        return chunks

    def create_vector_store(self, chunks: list, embeddings):
        """
        Creates a FAISS vector store from the given document chunks and embeddings.

        Args:
            chunks (list): A list of document chunks.
            embeddings: The embeddings model used to generate document vectors.

        Returns:
            FAISS: A FAISS vector store containing the document vectors.
        """
        vector_store = FAISS.from_documents(
            chunks,
            embeddings,
        )
        
        return vector_store
