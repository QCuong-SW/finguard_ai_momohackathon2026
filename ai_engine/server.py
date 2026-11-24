"""
FinGuard AI Engine - Internal FastAPI Microservice
Được gọi từ NestJS Backend qua AiBridgeService
"""
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import (
    ScamAnalyzeRequest, ScamAnalyzeResponse,
    RagAnalyzeRequest, RagAnalyzeResponse,
    AdvisorRequest, AdvisorResponse
)
from pipelines.scam_analyzer import ScamAnalyzer
from pipelines.rag_engine import RAGEngine
from pipelines.persona_advisor import PersonaAdvisor
from pipelines.ocr_pipeline import OCRPipeline

app = FastAPI(
    title="FinGuard AI Engine",
    description="Microservice xử lý AI (NLP, LLM, RAG, Anomaly Detection, XAI) cho FinGuard AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Khởi tạo các pipeline
scam_analyzer = ScamAnalyzer()
rag_engine = RAGEngine()
persona_advisor = PersonaAdvisor()
ocr_pipeline = OCRPipeline()

@app.get("/")
def health_check():
    return {"status": "ok", "service": "FinGuard AI Engine", "ready": True}

# 1. Endpoint Scam Analyzer & XAI
@app.post("/api/v1/ai/scam/analyze", response_model=ScamAnalyzeResponse)
def analyze_scam(req: ScamAnalyzeRequest):
    result = scam_analyzer.analyze(content=req.content, input_type=req.type, context=req.context)
    return result

# 2. Endpoint RAG Document Analyzer
@app.post("/api/v1/ai/rag/analyze-doc", response_model=RagAnalyzeResponse)
def analyze_document(req: RagAnalyzeRequest):
    result = rag_engine.analyze_document_traps(doc_name=req.doc_name, text=req.text or "")
    return result

# 3. Endpoint Persona Decision Advisor
@app.post("/api/v1/ai/advisor/recommend", response_model=AdvisorResponse)
def recommend_advice(req: AdvisorRequest):
    result = persona_advisor.recommend(action=req.action, persona=req.persona)
    return result

if __name__ == "__main__":
    port = int(os.getenv("AI_ENGINE_PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
