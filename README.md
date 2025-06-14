# kazai_new
# 🧠 KAZAI 5.0 – Unified Agentic Architecture (LangGraph + AutoGen + CRADLE + Dynamic RAG)

## 🚀 Overview
KAZAI 5.0 is a cognitive engine that transforms abstract prompts into structured, creative, and validated insights using a multi-agent architecture. It integrates:
- **LangGraph**: For deterministic agent flow
- **AutoGen**: For critique, reflection, and persona dialogues
- **CRADLE**: For disruptive leap detection via TIP/DIF
- **ChromaDB**: For vector memory with metadata filtering (supports Dynamic RAG)

---

## 🧠 Architecture Layers

1. **LICEE** – SONAR/LCM embeddings for latent abstraction  
2. **GSSA** – Graph-stochastic self-attention  
3. **MoM** – Manifold of Meaning to track conceptual drift  
4. **IPF** – Insight potential scoring (entropy/abstraction)  
5. **CDF Loss** – Conceptual divergence scoring  
6. **MIVE** – Math Insight Validation (SymPy + Z3)  
7. **CRADLE** – Leap engine using TIP (Total Interference Potential)  
8. **RCR** – Recursive Cognitive Resonance via AutoGen agents  
9. **LangMem** – Persistent vector memory (FAISS or ChromaDB)  
10. **Darwinian Agent Evolution** – Adaptive learning roles  
11. **Langfuse** – Observability and trace logging  
12. **Insight Control Panel** – User sliders for Novelty, Risk, Metaphor, etc.

---

## 🔄 Agent-to-Framework Coordination

| Agent Role             | Framework   |
|------------------------|-------------|
| Perception Agent       | LangGraph   |
| Imaginator             | LangGraph   |
| Diverger               | LangGraph   |
| CRADLE Discovery Node  | LangGraph   |
| Synthesizer            | LangGraph   |
| Critic Agent           | AutoGen     |
| RCR Archetypes         | AutoGen     |
| Meta-Agent Reflector   | AutoGen     |
| Discriminator          | LangGraph   |
| Sketcher               | LangGraph   |
| Mathematician          | LangGraph   |
| Visualizer             | LangGraph   |
| Final Composer         | LangGraph   |

---

## ✅ Memory Architecture

- Vector memory via **ChromaDB** (with metadata filtering)  
- Supports retrieval by TIP, agent, archetype, domain  
- Enables Dynamic RAG + parameterized insight shaping  
- Logging of scores (TIP, CDF, MIVE) supported via PGVector  

---

## 🛠️ REST Insight Logging API

**FastAPI endpoint**: `POST /store_insight`

Stores:
- `user_prompt`, `final_output`
- `embedding` (vector)
- `tip_score`, `cdf_score`, `mive_score`
- `primary_agent`, `archetype`, `version`, `tags`
- `agent_trace` (JSON log)

Supports:
- Internal LLM agent logs  
- CRADLE + Composer insight versioning  
- Future dashboard or Langfuse integration  

---

## 🧪 PGVector SQL Table

```sql
CREATE TABLE insight_log (
    id SERIAL PRIMARY KEY,
    user_prompt TEXT,
    final_output TEXT,
    embedding VECTOR(1536),
    tip_score FLOAT,
    cdf_score FLOAT,
    mive_score FLOAT,
    primary_agent TEXT,
    archetype TEXT,
    version TEXT,
    domain TEXT,
    tags TEXT[],
    created_at TIMESTAMP DEFAULT now(),
    agent_trace JSONB
);
```

---

## 🌟 Benefits

- Modular + symbolic + visual + mathematical + philosophical  
- Personalized and score-adjustable insights  
- CRADLE-enhanced disruptive creativity  
- RCR agent loops with archetype critique  
- Observability + memory + semantic filtering = Dynamic Intelligence  
