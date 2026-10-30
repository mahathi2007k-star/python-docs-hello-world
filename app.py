from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Mahathi and the GitHub with dbms Repository Analytics team!"

