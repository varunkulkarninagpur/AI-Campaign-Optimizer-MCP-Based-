# 🚀 CPaaS AI Campaign Optimizer (MCP-Based)

## 🔥 Overview
An AI-powered campaign optimization system built using MCP (Model Context Protocol) concepts.

This system simulates real CPaaS challenges like:
- Campaign performance analysis
- Audience targeting
- Optimal timing decisions
- Multi-step AI reasoning

---

## 🧠 Key Features
- MCP-style tool architecture
- AI-based intent detection (HuggingFace)
- Multi-step tool orchestration
- Agent-like decision loop
- Campaign performance optimization

---

## 🛠️ Tech Stack
- Python
- FastAPI
- HuggingFace Transformers
- Uvicorn

---

## ⚙️ How It Works
1. User sends query
2. AI selects appropriate tool(s)
3. System executes tools
4. Returns optimized recommendations

---

## 🚀 Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
