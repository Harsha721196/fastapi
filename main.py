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
    {
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

