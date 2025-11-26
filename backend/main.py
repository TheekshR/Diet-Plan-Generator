from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import calculator, meals, pdf_router 

app = FastAPI(title="Diet Plan Generator API")

# ----- CORS Setup -----
origins = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins
    allow_credentials=True,
    allow_methods=["*"],     # Allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)

# ----- Routers -----
app.include_router(calculator.router)
app.include_router(meals.router)
app.include_router(pdf_router.router)

# ----- Root Endpoint -----
@app.get("/")
def home():
    return {"message": "Diet Plan API is running"}
