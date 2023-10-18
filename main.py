from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("html/index.html", {"request": request, "translated_text": None})

@app.post("/result")
def translate(request: Request, input_text):
    map ={
        "A": "а",
        "Б": "b",
        "В": "B",
        "Г": "G",
        "Д": "D",
        "E": "e",
        "Ж": "}|{",
        "З": "3",
        "И": "u",
        "K": "K",
        "Л": "J|",
        "M": "M",
        "H": "H",
        "O": "O",
        "П": "p",
        "P": "P",
        "C": "C",
        "T": "T",
        "У": "y",
        "ф": "f"
    }
    translated_text = input_text
    return templates.TemplateResponse("index.html", {"request": request, "translated_text": translated_text})