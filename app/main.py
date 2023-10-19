from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException
from pathlib import Path


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

@app.exception_handler(404)
async def http_not_found_handler(request, __):
    return templates.TemplateResponse("error.html", {"request": request, "status_code": 404})


@app.exception_handler(405)
async def http_method_not_allowed_handler(request, __):
    return templates.TemplateResponse("error.html", {"request": request, "status_code": 405})

@app.exception_handler(500)
async def http_method_not_allowed_handler(request, __):
    return templates.TemplateResponse("error.html", {"request": request, "status_code": 500})



@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "translated_text": None})

@app.post("/result")
def translate(request: Request, input_text: str = Form(default="")):
    translated_text = cyrillic_to_latin(input_text)
    return templates.TemplateResponse("index.html", {"request": request, "translated_text": translated_text})


def cyrillic_to_latin(text):
    if not bool(text):
        return "text must be not empty"

    transliteration = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',

        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    latin_text = "".join(transliteration.get(c, c) for c in text)

    return latin_text
