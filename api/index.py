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


@app.get("/api")
def api_get(name: list[str] = Query([])) -> dict[str, list[int]]:

    with open("students.json") as file:
        student_data = json.load(file)

    return {"marks": [student_data[n] for n in name if n in student_data]}
