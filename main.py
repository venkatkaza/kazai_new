from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ARRAY, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = FastAPI()
DATABASE_URL = "postgresql://user:password@localhost/kazai_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Insight(Base):
    __tablename__ = "insight_log"
    id = Column(Integer, primary_key=True, index=True)
    user_prompt = Column(Text, nullable=False)
    final_output = Column(Text, nullable=False)
    embedding = Column(ARRAY(Float))
    tip_score = Column(Float)
    cdf_score = Column(Float)
    mive_score = Column(Float)
    primary_agent = Column(String)
    archetype = Column(String)
    version = Column(String)
    domain = Column(String)
    tags = Column(ARRAY(String))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    agent_trace = Column(JSON)

Base.metadata.create_all(bind=engine)

class InsightInput(BaseModel):
    user_prompt: str
    final_output: str
    embedding: Optional[List[float]] = None
    tip_score: Optional[float]
    cdf_score: Optional[float]
    mive_score: Optional[float]
    primary_agent: Optional[str]
    archetype: Optional[str]
    version: Optional[str]
    domain: Optional[str]
    tags: Optional[List[str]] = []
    agent_trace: Optional[dict]

@app.post("/store_insight")
def store_insight(insight: InsightInput):
    db = SessionLocal()
    try:
        new_entry = Insight(**insight.dict())
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return {"message": "Insight stored", "id": new_entry.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
