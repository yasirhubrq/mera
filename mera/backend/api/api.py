from fastapi import FastAPI
import csv
from random import randint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../../frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

read = []


with open("quotes.csv",'r',encoding='utf-8') as f:
    read = list(csv.reader(f, delimiter=",", quotechar='"'))

def random():
    r = randint(1,10000)
    return (read[r][0],read[r][1],read[r][2])

@app.get("/api/quote")
def quote():
    r = random()
    return {
        'quote':r[0],
        'by':r[1],
        'tags':r[2]
    }

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))