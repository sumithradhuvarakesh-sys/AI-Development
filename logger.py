import json
import os
from datetime import datetime
def log_step(iteration, stage, message):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/agent_trace.json"
    entry = {
        "iteration": iteration,
        "time": datetime.now().strftime("%H:%M:%S"),
        "stage": stage,
        "message": str(message)
    }
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            try:
                logs = json.load(file)
            except:
                logs = []
    else:
        logs = []
    logs.append(entry)
    with open(log_file, "w") as file:
        json.dump(logs, file, indent=4)