import sys

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(name: str = "World"):
    return {"message": f"Hello {name}"}

@app.get("/python-version")
def python_version():
    return {"python_version": sys.version}
