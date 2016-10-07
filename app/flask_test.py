from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/index")
def new():
    return "something new"


@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hi %s </h2>" % username


@app.route('/post/<int:user_id>')
def post(user_id):
    return "<h2>ID is %s </h2>" % user_id

if __name__ == "__main__":
    app.run(debug=True)
