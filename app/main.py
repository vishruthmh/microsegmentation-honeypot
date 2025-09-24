from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Main App Home"}

@app.get("/data")
def data():
    r = requests.get("http://db:6000/query")
    return r.json()
