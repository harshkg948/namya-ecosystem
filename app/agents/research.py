from app.agents.base import BaseAgent
from app.mcp.gateway import MCPToolGateway

class ResearchAgent(BaseAgent):
    def run(self, domain: str):
        search_res = MCPToolGateway.execute_tool("google_search", {"query": domain})
        scholar_res = MCPToolGateway.execute_tool("google_scholar", {"query": domain})
        return {
            "agent": "2. Research & Discovery Agent",
            "status": "Completed",
            "mcp_traces": [search_res, scholar_res]
        }