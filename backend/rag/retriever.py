from langchain_community.vectorstores import (FAISS)
from backend.services.embeddings import (embeddings)


VECTOR_DB_PATH = (
    "backend/rag/vector_store"
)

db = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 4})