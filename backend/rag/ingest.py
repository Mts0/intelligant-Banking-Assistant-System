from pathlib import Path
from langchain_community.document_loaders import (PyPDFLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import (FAISS)
from backend.services.embeddings import (embeddings)


PDF_FOLDER = "docs/policies"

VECTOR_DB_PATH = (
    "backend/rag/vector_store"
)


def load_documents():

    documents = []

    pdf_files = Path(PDF_FOLDER).glob("*.pdf")

    for pdf in pdf_files:

        loader = PyPDFLoader(
            str(pdf)
        )

        documents.extend(
            loader.load()
        )

    return documents


def split_documents(documents):

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )

    return splitter.split_documents(
        documents
    )


def build_vector_db():

    docs = load_documents()

    chunks = split_documents(
        docs
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(
        VECTOR_DB_PATH
    )

    print(
        f"Indexed {len(chunks)} chunks"
    )


if __name__ == "__main__":
    build_vector_db()