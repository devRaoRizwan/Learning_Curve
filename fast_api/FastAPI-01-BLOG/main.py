from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/" , response_class= HTMLResponse , include_in_schema=False) # we will add include_in_schema key to ensure it doesnt shows in the docs ( the html endpoints)
@app.get("/posts" , response_class=HTMLResponse) #what we did here is mapped two diff endpoints(/ and /posts) to same function
def home() :
    return f"<h1>{posts[0]["title"]}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts