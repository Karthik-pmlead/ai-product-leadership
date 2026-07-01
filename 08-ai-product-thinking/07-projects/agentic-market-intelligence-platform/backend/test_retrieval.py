from services.retrieval_service import RetrievalService

retriever = RetrievalService()

results = retriever.retrieve(
    "Tesla competition"
)

for r in results:

    print(
        r["source"]
    )
