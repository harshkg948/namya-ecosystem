from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.task_planner import TaskPlannerAgent
from app.agents.research import ResearchAgent
from app.agents.knowledge_graph import KnowledgeGraphAgent
from app.agents.verification import VerificationAgent
from app.agents.analysis import AnalysisAgent
from app.agents.decision_planner import DecisionPlannerAgent
import os
import uvicorn
app = FastAPI(
    title="NAMYA - AI Technology & Product Design Agent Ecosystem",
    version="3.0",
    description="Enterprise-grade Multi-Agent Orchestrator with MCP Gateway & Knowledge Layer"
)

class ProjectInput(BaseModel):
    goal: str
    domain: str
    constraints: str

@app.get("/")
def health_check():
    return {
        "status": "NAMYA Ecosystem Fully Operational",
        "orchestrator": "Lead Architect Agent (Google AOK Orchestrator & State Engine)"
    }

@app.post("/run-pipeline")
def execute_ecosystem_pipeline(data: ProjectInput):
    try:
        planner = TaskPlannerAgent()
        tasks = planner.run(data.goal)

        researcher = ResearchAgent()
        research_data = researcher.run(data.domain)

        kg_agent = KnowledgeGraphAgent()
        kg_mapping = kg_agent.run(data.domain)

        verifier = VerificationAgent()
        verification_status = verifier.run(kg_mapping, data.constraints)

        analyzer = AnalysisAgent()
        analysis_insights = analyzer.run(verification_status)

        decision_agent = DecisionPlannerAgent()
        final_roadmap = decision_agent.run(analysis_insights)

        return {
            "status": "Success",
            "orchestrator_state": "Completed successfully under Lead Architect control",
            "execution_traces": {
                "1_task_planner": tasks,
                "2_research": research_data,
                "3_knowledge_graph": kg_mapping,
                "4_verification": verification_status,
                "5_analysis": analysis_insights,
                "6_decision_and_planning": final_roadmap
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)    