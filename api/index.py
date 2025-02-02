from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from JSON file
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "../marks.json")

with open(json_path, 'r') as file:
    marks_data = json.load(file)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist('name')
    marks_list = []
    for name in names:
        mark_entry = next((item for item in marks_data if item["name"].lower() == name.lower()), None)
        marks_list.append(mark_entry["marks"] if mark_entry else None)
    return {"marks": marks_list}
