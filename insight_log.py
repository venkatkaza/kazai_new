CREATE EXTENSION IF NOT EXISTS vector;

#PGVector scheme

CREATE TABLE insight_log (
    id SERIAL PRIMARY KEY,
    
    -- Input/Output
    user_prompt TEXT NOT NULL,
    final_output TEXT NOT NULL,

    -- Vector embedding (e.g. 1536-dim OpenAI/Groq)
    embedding VECTOR(1536),  -- You can change dimension if needed

    -- Score fields
    tip_score FLOAT,         -- Total Interference Potential
    cdf_score FLOAT,         -- Conceptual Divergence Function
    mive_score FLOAT,        -- Math Insight Validator result (0 or 1)

    -- Agent metadata
    primary_agent TEXT,      -- e.g., "Synthesizer"
    archetype TEXT,          -- e.g., "Einstein", "Da Vinci", "Tagore"
    version TEXT,            -- e.g., "RCR v2.1"

    -- Traceable metadata
    domain TEXT,             -- e.g., "physics", "metaphysics", "biology"
    tags TEXT[],             -- Custom tag list
    created_at TIMESTAMP DEFAULT NOW(),
    
    -- Optional JSON logs (full trace or LangGraph state snapshot)
    agent_trace JSONB
);
