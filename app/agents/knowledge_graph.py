from app.agents.base import BaseAgent
from app.storage.graph_db import KnowledgeGraphDB
from app.storage.vector_store import VectorStoreRAG

class KnowledgeGraphAgent(BaseAgent):
    def run(self, domain: str):
        graph_res = KnowledgeGraphDB().query_graph(domain)
        rag_res = VectorStoreRAG().search_embeddings(domain)
        return {
            "agent": "3. Knowledge Graph Agent",
            "status": "Completed",
            "graph_mapping": graph_res,
            "vector_rag": rag_res
        }