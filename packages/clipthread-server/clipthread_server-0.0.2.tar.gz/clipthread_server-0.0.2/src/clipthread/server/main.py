from fastapi import FastAPI
from clipthread.server.api import clipboard, journal

app = FastAPI()

app.include_router(clipboard.router, prefix="/clipboard", tags=["clipboard"])
app.include_router(journal.router, prefix="/journal", tags=["journal"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ClipThread server!"}


def start_server():
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser(description='ClipThread server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind to')
    
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)

def _start_server(host: str, port: int):
    import uvicorn
    uvicorn.run(app, host=host, port=port)