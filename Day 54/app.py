from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "" \
           "<h1 style=\"text-align:center\">Hello World</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://images.unsplash.com/photo-1615789591457-74a63395c990?ixlib=rb-1.2.1&ixid" \
           "=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZG9tZXN0aWMlMjBjYXR8ZW58MHx8MHx8&w=1000&q=80'>" \
           ""


def make_decorators():
    return "<b></b>"


@app.route("/bye")
@make_decorators
def bye():
    return "<b>Bye</b>"


@app.route("/username/<name>/<int:number>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)  # running app in debug mode to auto reload
