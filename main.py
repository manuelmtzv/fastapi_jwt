from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI and JWT Auth example"}
