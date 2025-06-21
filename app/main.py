from fastapi import FastAPI

app = FastAPI(
    title = "Build with fearfactor3",
    description = "Ease your build."
)

@app.get("/")
async def home():
    return {"success": True, "message": "Welcome to Build with fearfactor3!"}
