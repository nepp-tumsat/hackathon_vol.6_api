from fastapi import FastAPI

from api.routers import task, done ,gpt

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


app.include_router(task.router)
app.include_router(done.router)
app.include_router(gpt.router)
