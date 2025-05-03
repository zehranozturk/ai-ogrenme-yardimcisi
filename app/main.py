from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.ai_model import explain_with_model

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/explain", response_class=HTMLResponse)
async def form_post(request: Request, term: str = Form(...)):
    explanation = explain_with_model(term)
    return templates.TemplateResponse("index.html", {"request": request, "term": term, "explanation": explanation})

