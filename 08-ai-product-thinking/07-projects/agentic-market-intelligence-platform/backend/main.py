from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

import json
import time

from models.schemas import AnalysisRequest, AnalysisResponse

from agents.router_agent import RouterAgent
from agents.risk_agent import RiskAgent
from agents.opportunity_agent import OpportunityAgent
from agents.recommendation_agent import RecommendationAgent
from agents.competitor_agent import CompetitorAgent

from agents.dynamic_planner import DynamicPlanner

from utils.telemetry import Telemetry
from utils.evaluator import Evaluator
from utils.memory import MemoryStore


app = FastAPI(title="Agentic Market Intelligence Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------------------------
# INIT SYSTEM COMPONENTS
# -------------------------

router_agent = RouterAgent()

dynamic_planner = DynamicPlanner()

risk_agent = RiskAgent()
opportunity_agent = OpportunityAgent()
recommendation_agent = RecommendationAgent()
competitor_agent = CompetitorAgent()

telemetry = Telemetry()
evaluator = Evaluator()
memory = MemoryStore()


# -------------------------
# SSE helper
# -------------------------

def sse(event: dict):
    return "data: " + json.dumps(event) + "\n\n"


# -------------------------
# HEALTH
# -------------------------

@app.get("/")
def root():
    return {
        "status": "running",
        "system": "Agentic Market Intelligence Platform"
    }


# -------------------------
# STREAM ENGINE
# -------------------------

def stream_engine(query: str):

    # =========================
    # 1. ROUTER
    # =========================

    t_router = telemetry.start("RouterAgent")

    router_result = router_agent.route(query)

    trace_router = telemetry.end(
        t_router,
        input_data=query,
        prompt="Classify intent and extract entities",
        context="Router layer",
        output=router_result
    )

    yield sse({
        "agent": "Router",
        "status": "done",
        "trace": trace_router
    })

    time.sleep(0.2)

    intent = router_result["intent"]
    company = router_result.get("company")
    secondary_company = router_result.get("secondary_company")

    # =========================
    # 2. LOAD MEMORY
    # =========================

    past_context = memory.get(company)

    # =========================
    # 3. DYNAMIC PLAN (GRAPH)
    # =========================

    plan = dynamic_planner.create_plan(intent)

    yield sse({
        "agent": "Planner",
        "status": "done",
        "plan": plan
    })

    time.sleep(0.2)

    # =========================
    # COMPETITOR FLOW
    # =========================

    if "competitor" in plan:

        t_comp = telemetry.start("CompetitorAgent")

        comp_result = competitor_agent.analyze(
            company,
            secondary_company
        )

        trace_comp = telemetry.end(
            t_comp,
            input_data={"a": company, "b": secondary_company},
            prompt="Compare two companies",
            context="Competitive intelligence dataset",
            output=comp_result
        )

        yield sse({
            "agent": "Competitor",
            "status": "done",
            "trace": trace_comp
        })

        time.sleep(0.2)

    # =========================
    # 4. RISK
    # =========================

    if "risk" in plan:

        t_risk = telemetry.start("RiskAgent")

        risk_prompt = f"""
        Company: {company}
        Past context: {past_context}
        Identify key risks.
        """

        risk_result = risk_agent.analyze(company)

        trace_risk = telemetry.end(
            t_risk,
            input_data=company,
            prompt=risk_prompt,
            context="Risk knowledge base + RAG",
            output=risk_result
        )

        risk_eval = evaluator.score_risks(risk_result["risks"])

        yield sse({
            "agent": "Risk",
            "status": "done",
            "evaluation": risk_eval,
            "trace": trace_risk
        })

        time.sleep(0.2)

    # =========================
    # 5. OPPORTUNITY
    # =========================

    if "opportunity" in plan:

        t_opp = telemetry.start("OpportunityAgent")

        opp_prompt = f"""
        Company: {company}
        Past context: {past_context}
        Identify growth opportunities.
        """

        opportunity_result = opportunity_agent.analyze(company)

        trace_opp = telemetry.end(
            t_opp,
            input_data=company,
            prompt=opp_prompt,
            context="Market expansion signals",
            output=opportunity_result
        )

        opp_eval = evaluator.score_opportunities(
            opportunity_result["opportunities"]
        )

        yield sse({
            "agent": "Opportunity",
            "status": "done",
            "evaluation": opp_eval,
            "trace": trace_opp
        })

        time.sleep(0.2)

    # =========================
    # 6. RECOMMENDATION
    # =========================

    if "recommendation" in plan:

        t_rec = telemetry.start("RecommendationAgent")

        recommendations = recommendation_agent.generate(
            company,
            risk_result.get("risks", []),
            opportunity_result.get("opportunities", [])
        )

        trace_rec = telemetry.end(
            t_rec,
            input_data=company,
            prompt="Generate strategic recommendations",
            context="Risk + Opportunity synthesis",
            output=recommendations
        )

        rec_eval = evaluator.score_recommendations(recommendations)

        yield sse({
            "agent": "Recommendation",
            "status": "done",
            "evaluation": rec_eval,
            "trace": trace_rec
        })

        time.sleep(0.2)

    # =========================
    # 7. SAVE MEMORY
    # =========================

    memory.save(company, {
        "risks": risk_result.get("risks", []),
        "opportunities": opportunity_result.get("opportunities", []),
        "recommendations": recommendations
    })

    # =========================
    # 8. FINAL SUMMARY
    # =========================

    yield sse({
        "agent": "Complete",
        "intent": intent,
        "risks": risk_result.get("risks", []),
        "opportunities": opportunity_result.get("opportunities", []),
        "recommendations": recommendations,
        "trace": [],
        "memory_used": past_context
    })


# -------------------------
# STREAM ENDPOINT
# -------------------------

@app.get("/stream-analyze")
def stream_analyze(query: str):

    return StreamingResponse(
        stream_engine(query),
        media_type="text/event-stream"
    )


# -------------------------
# REST fallback
# -------------------------

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest):

    return {
        "intent": "use_stream_endpoint",
        "summary": "Use /stream-analyze for full dynamic agent execution",
        "risks": [],
        "opportunities": [],
        "recommendations": [],
        "trace": [],
        "evaluation": {},
        "memory": {}
    }
