# python -m uvicorn main:app --reload

from fastapi import FastAPI
import random
from data import data_list

app = FastAPI()


@app.get("/")
async def root():
    return data_list
