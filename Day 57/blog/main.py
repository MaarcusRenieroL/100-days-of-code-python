from flask import Flask, render_template
from post import Post
import requests

BLOG_API_ENDPOINT = "https://api.npoint.io/ReDaC+3d_3nDpO!n+_aDdr3$$"


def refresh_api():
    posts = requests.get(BLOG_API_ENDPOINT).json()
    global post_objects
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return post_objects


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    refresh_api()
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
