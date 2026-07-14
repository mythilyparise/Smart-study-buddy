from langchain_chroma import Chroma
from utils.embeddings import get_embeddings


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
