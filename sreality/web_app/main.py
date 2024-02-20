import os
import subprocess
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sreality.models import Estate

app = FastAPI()
templates = Jinja2Templates(directory="web_app/templates")

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_size=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



@app.get("/", response_class=HTMLResponse)
def get_estates(request: Request):
    db = SessionLocal()
    estates_data = db.query(Estate).all()
    response = templates.TemplateResponse("index.html", {"request": request, "estates_data": estates_data})
    response.headers["Cache-Control"] = "no-cache"
    return response

def run_crawler():
    subprocess.run(["scrapy", "crawl", "sreality_spider"])

@app.post("/crawl")
async def crawl():
    run_crawler()
    return {"message": "Crawler started"}

@app.post("/clear")
async def clear_estates():
    try:
        db = SessionLocal()
        db.query(Estate).delete()
        db.commit()
        return {"message": "All records deleted from estates table"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
