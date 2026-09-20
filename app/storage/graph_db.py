class KnowledgeGraphDB:
    def query_graph(self, concept: str):
        return {
            "graph_db": "Neo4j / Nebula DB", 
            "nodes_traversed": [concept, "Related_Domain", "Prerequisite_Module"]
        }