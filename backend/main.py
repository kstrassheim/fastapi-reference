from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from os import path as os_path

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api_router = APIRouter()

@api_router.get("/hello")
def read_hello():
    return {"message": "Hello from API"}

app.include_router(api_router, prefix="/api")

# Mount static files on /static (adjust if you want a different prefix)
app.mount("", StaticFiles(directory="./dist", html=True), name="client")

# Optional: Serve index.html at the root
@app.get('/')
async def client():  return RedirectResponse(url="client")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)