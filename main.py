from fastapi import FastAPI,Request
from fastapi.responses import HTML Response



app = FastAPI()

posts :list[dict] = [
    {
        "name" : "Tzuyu",
        "group" : "Twice",
        "leader" : "Jihyo"
    },
    {
        "name" : "Lisa",
        "group" : "BlackPink",
        "leader" : "NO-leader"
    }
]
@app.get("/api/posts")
@app.get("/response_class= HTMLResponse")
def get_posts():
    return posts
