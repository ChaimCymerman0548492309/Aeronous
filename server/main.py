from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import uuid
import json
import os


app = FastAPI()

# ✅ הגדרת CORS Middleware תקינה
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # באפשרותך לשים ['http://localhost:4200'] אם אתה רוצה להחמיר
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# הגדרת שם קובץ ה-JSON
JSON_FILE = "targets_db.json"

# פונקציה לטעינת נתונים מהקובץ
def load_targets() -> Dict[str, Dict]:
    if not os.path.exists(JSON_FILE):
        return {}
    with open(JSON_FILE, "r") as f:
        return json.load(f)

# פונקציה לשמירת נתונים לקובץ
def save_targets(targets: Dict[str, Dict]):
    with open(JSON_FILE, "w") as f:
        json.dump(targets, f, indent=4)

# מודל Pydantic עבור קלט
class Target(BaseModel):
    name: str
    heading: float
    signal_strength: int
    timestamp: str

# פונקציה לסיווג אוטומטי
def classify_target(signal: int) -> str:
    if signal >= 80:
        return "hostile"
    elif signal < 30:
        return "friendly"
    return "neutral"

# POST endpoint להוספת targets
@app.post("/targets")
async def add_targets(targets: List[Target]):
    current_targets = load_targets()
    for target in targets:
        target_id = str(uuid.uuid4())
        classification = classify_target(target.signal_strength)
        current_targets[target_id] = {
            **target.model_dump(),
            "id": target_id,
            "classification": classification
        }
    save_targets(current_targets)
    return {"message": "Targets added successfully"}

# GET endpoint לקבלת כל ה-targets
@app.get("/targets")
async def get_targets():
    return list(load_targets().values())

# DELETE endpoint למחיקת target לפי ID
@app.delete("/targets/{target_id}")
async def delete_target(target_id: str):
    current_targets = load_targets()
    if target_id not in current_targets:
        raise HTTPException(status_code=404, detail="Target not found")
    del current_targets[target_id]
    save_targets(current_targets)
    return {"message": "Target deleted"}

@app.patch("/targets/{target_id}")
def update_classification(target_id: str, data: dict):
    new_classification = data.get("classification")
    
    if new_classification not in ["hostile", "friendly", "neutral"]:
        raise HTTPException(status_code=400, detail="Invalid classification value")

    current_targets = load_targets()

    if target_id not in current_targets:
        raise HTTPException(status_code=404, detail="Target not found")

    current_targets[target_id]["classification"] = new_classification
    save_targets(current_targets)

    return {"message": f"Target {target_id} classification updated to {new_classification}"}


