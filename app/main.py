from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes.expenses import router as expenses_router
from .routes.settlements import router as settlements_router
from .routes.people import router as people_router
from .routes.categories import router as categories_router
from .routes.recurring import router as recurring_router
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Expense Splitter",
    description="API for splitting expenses fairly among people",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with API version prefix
app.include_router(
    expenses_router,
    prefix="/api/v1"
)

app.include_router(
    settlements_router,
    prefix="/api/v1"
)

app.include_router(
    people_router,
    prefix="/api/v1"
)

app.include_router(
    categories_router,
    prefix="/api/v1"
)

app.include_router(
    recurring_router,
    prefix="/api/v1"
)

# Health check endpoint
@app.get("/health")
def read_health():
    return {"status": "healthy"}

@app.get("/api")
def read_root():
    return {"message": "Welcome to Expense Splitter API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
