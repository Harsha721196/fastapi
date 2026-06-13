from fastapi import FastAPI # type : ignore
from fastapi.responses import HTMLResponse # type : ignore


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
    },
]
@app.get("/home",response_class = HTMLResponse)  # type :ignore
def home():
    return f"""
    <h1>{posts[0]['name']}</h1>
    <p>Group: {posts[0]['group']}</p>
    <p>Leader: {posts[0]['leader']}</p>
    <h1>{posts[1]['name']}</h1>
    <p>Group: {posts[1]['group']}</p>
    <p>{posts[1]['leader']}</p>
    
    <h2>{posts[0]['name']} belongs to, {posts[0]['group']} and the leader is {posts[0]['leader']}</h2>
    """

@app.get("/api/posts")

def get_posts():
    return posts
print(posts)

