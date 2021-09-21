from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import spacy
from process_sentence import render


nlp = spacy.load("en_core_sci_sm")
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def analyse_input(request: Request, sentence: str = Form(...)):
    filepath = Path("./static/image.svg")
    render(sentence, nlp, filepath)
    return templates.TemplateResponse("response.html", {"request": request,
                                                        "sentence": sentence,
                                                        "image": filepath})


@app.get("/example", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("response.html",
                                      {"request": request,
                                       "sentence": """This is an example sentence, 
                                       albeit one lacking in scientific content""",
                                       "image": "static/example.svg"})
