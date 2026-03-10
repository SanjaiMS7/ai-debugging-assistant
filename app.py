from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from debugger.debug_logic import analyze_error

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/debug")
def debug(request: Request, code: str = Form(...)):
    result = analyze_error(code)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})