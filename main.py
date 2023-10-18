from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("html/index.html", {"request": request, "translated_text": None})

@app.post("/result")
def translate(request: Request, input_text, str=Form(...)):
    translated_text = input_text
    return templates.TemplateResponse("index.html", {"request": request, "translated_text": translated_text})