import json

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


with open("students.json") as file:
    STUDENT_DATA = json.load(file)


def student_get(name: str) -> int:
    return next((d["marks"] for d in STUDENT_DATA if d["name"] == name), None)


@app.get("/api/")
def api_get(name: list[str] = Query([])):
    return {"marks": [student_get(n) for n in name]}
