from fastapi import FastAPI , Request , HTTPException , status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas import PostCreate , PostResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


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

@app.get("/" , include_in_schema=False) # we will add include_in_schema key to ensure it doesnt shows in the docs ( the html endpoints)
@app.get("/posts", include_in_schema=False) #what we did here is mapped two diff endpoints(/ and /posts) to same function
def home(request : Request) :
    return templates.TemplateResponse(request, name="home.html" , context= {"posts" : posts , "title" : "Home"})

@app.get("/api/posts" , response_model=list[PostResponse]) #we use list because we want to return many
def get_posts():
    return posts

@app.get("/api/posts/{post_id}" , response_model= PostResponse)
def get_post(post_id : int):
    for post in posts :
        if post.get("id") == post_id :
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="post not found")