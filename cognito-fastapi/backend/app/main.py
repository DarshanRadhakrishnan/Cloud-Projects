from fastapi import FastAPI
from .routes import users, items


app = FastAPI(title="AWS Cognito + FastAPI Backend")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def health():
    return {"status": "Backend running"}
