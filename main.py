import uvicorn
from fastapi import FastAPI

from config import ServerInfo
from router import router

ServerInfo = ServerInfo()
app = FastAPI(docs_url='/community-docs/', redoc_url='/community-redoc/')
app.include_router(router.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=ServerInfo.host, port=ServerInfo.port, reload=True, workers=1)
