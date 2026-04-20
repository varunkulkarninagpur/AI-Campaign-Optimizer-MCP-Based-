import random

# Simulated campaign data
campaigns = [
    {"id": 1, "name": "Sale Campaign", "open_rate": 0.2, "click_rate": 0.05},
    {"id": 2, "name": "Festival Campaign", "open_rate": 0.35, "click_rate": 0.1},
]

def get_campaign_stats():
    return campaigns

def analyze_engagement():
    best = max(campaigns, key=lambda x: x["open_rate"] + x["click_rate"])
    return {
        "best_campaign": best["name"],
        "score": best["open_rate"] + best["click_rate"]
    }

def suggest_best_time():
    return random.choice(["Morning", "Afternoon", "Evening"])

def optimize_audience():
    return "Target users aged 18-30 with high engagement history"