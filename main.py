from fastapi import FastAPI
from pydantic import BaseModel
from tools import campaign_tools
from transformers import pipeline

classifier = pipeline("zero-shot-classification")
app = FastAPI()

# MCP Tool Registry
tools = [
    {
        "name": "get_campaign_stats",
        "description": "Get performance stats of campaigns"
    },
    {
        "name": "analyze_engagement",
        "description": "Find best performing campaign"
    },
    {
        "name": "suggest_best_time",
        "description": "Suggest best time to run campaign"
    },
    {
        "name": "optimize_audience",
        "description": "Suggest best target audience"
    }
]

@app.get("/tools")
def get_tools():
    return tools

class Query(BaseModel):
    query: str

# Simple AI decision logic (FREE)
def decide_tool(query):
    labels = [
        "get campaign stats",
        "analyze best campaign",
        "suggest best time",
        "optimize audience"
    ]

    result = classifier(query, labels)

    best_label = result["labels"][0]

    if best_label == "analyze best campaign":
        return "analyze_engagement"
    elif best_label == "suggest best time":
        return "suggest_best_time"
    elif best_label == "optimize audience":
        return "optimize_audience"
    else:
        return "get_campaign_stats"
    

@app.post("/ask")
def ask_ai(q: Query):
    query = q.query

    context = {
        "history": [],
        "final_answer": None
    }

    for step in range(3):  # limit steps (important)
        
        # AI decides next action
        decision = decide_tool(query + str(context["history"]))

        result = execute_tool(decision)

        context["history"].append({
            "tool": decision,
            "result": result
        })

        # simple stopping condition
        if decision == "optimize_audience":
            context["final_answer"] = {
                "message": "Campaign optimized successfully",
                "steps": context["history"]
            }
            break

    return context

    # fallback to AI decision
    tool = decide_tool(query)

    if tool == "get_campaign_stats":
        result = campaign_tools.get_campaign_stats()
    elif tool == "analyze_engagement":
        result = campaign_tools.analyze_engagement()
    elif tool == "suggest_best_time":
        result = campaign_tools.suggest_best_time()
    elif tool == "optimize_audience":
        result = campaign_tools.optimize_audience()
    else:
        result = "Unknown"

    return {
        "tool_used": tool,
        "result": result
    }

def execute_tool(tool_name, input_data=None):
    if tool_name == "get_campaign_stats":
        return campaign_tools.get_campaign_stats()

    elif tool_name == "analyze_engagement":
        return campaign_tools.analyze_engagement()

    elif tool_name == "suggest_best_time":
        return campaign_tools.suggest_best_time()

    elif tool_name == "optimize_audience":
        return campaign_tools.optimize_audience()

    return "Unknown tool"