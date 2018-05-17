from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def getMember(name):
    return "Hello " + name + "!"

if __name__ == "__main__":
    app.run()
