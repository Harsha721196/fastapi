from fastapi import FastAPI # type : ignore
from fastapi.responses import HTMLResponse # type : ignore
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
app = FastAPI()

posts :list[dict] = [
    {
        "id" : 1,
        "name" : "Tzuyu",
        "group" : "Twice",
        "leader" : "Jihyo"
    },
    {
        "id" : 2,
        "name" : "Lisa",
        "group" : "BlackPink",
        "leader" : "NO-leader"
    },
    {
        "id" : 3,
        "name" :"joy",
        "group" : "Red Velvet",
        "leader" : "Irene"
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
    
    <h2>{posts[1]['name']} belongs to, {posts[1]['group']}</h2>    
    <pre>{posts[0]}</pre>
    <pre>{posts[1]}</pre>
    
    <h3>Total posts: {len(posts)}</h3>
    
    """

@app.get("/api/posts")

def get_posts():
    return posts
print(posts)

@app.get("/leaders",response_class = HTMLResponse)

def get_leaders():
    return f'''
    <h1> {posts[0]['leader']} is leader of {posts[0]['group']}</h1>
    <br>
    <h1> {posts[1]['group']} has no leader </h1>
    <br>
    <h1>{posts[2]['leader']} is leader of {posts[2]['group']}</h1>
    '''
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "post not found"}

@app.get("/posts/{post_name}")
def get_post(post_name: str):
    for post in posts:
        if post['name'] == post_name:
            return post
    return {"error": "post not found"}

@app.get("/posts/{post_leader}")
def get_posts(post_leader : str):
    for post in posts:
        if post['leader'] == post_leader:
            return post
    raise HTTPException(status_code=404, detail="post not found")