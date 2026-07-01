import os
import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)


class RetrievalService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.documents = []
        self.metadata = []

        self.index = None

        self._load_documents()
        self._build_index()

    def chunk_text(
        self,
        text,
        chunk_size=250
    ):

        words = text.split()

        chunks = []

        for i in range(
            0,
            len(words),
            chunk_size
        ):

            chunk = " ".join(
                words[
                    i:i + chunk_size
                ]
            )

            chunks.append(chunk)

        return chunks

    def _load_documents(self):

        base_dir = "data"

        for root, _, files in os.walk(
            base_dir
        ):

            for file in files:

                if not file.endswith(
                    ".txt"
                ):
                    continue

                path = os.path.join(
                    root,
                    file
                )

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        chunks = (
                            self.chunk_text(
                                content
                            )
                        )

                        for chunk in chunks:

                            self.documents.append(
                                chunk
                            )

                            self.metadata.append(
                                {
                                    "source": path
                                }
                            )

                except Exception as e:

                    print(
                        f"Failed loading {path}: {e}"
                    )

    def _build_index(self):

        if not self.documents:

            raise Exception(
                "No documents loaded."
            )

        embeddings = (
            self.model.encode(
                self.documents,
                convert_to_numpy=True
            )
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings.astype(
                np.float32
            )
        )

        print(
            f"[Retriever] Indexed "
            f"{len(self.documents)} chunks"
        )

    def retrieve(
        self,
        query,
        top_k=3
    ):

        query_embedding = (
            self.model.encode(
                [query],
                convert_to_numpy=True
            )
        )

        distances, indices = (
            self.index.search(
                query_embedding.astype(
                    np.float32
                ),
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            results.append(
                {
                    "content":
                        self.documents[idx],
                    "source":
                        self.metadata[idx][
                            "source"
                        ]
                }
            )

        return results

    def retrieve_context(
        self,
        query,
        top_k=3
    ):

        docs = self.retrieve(
            query,
            top_k
        )

        context = "\n\n".join(
            [
                doc["content"]
                for doc in docs
            ]
        )

        sources = list(
            set(
                [
                    doc["source"]
                    for doc in docs
                ]
            )
        )

        return {
            "context": context,
            "sources": sources
        }
