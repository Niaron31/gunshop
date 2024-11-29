from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return 'Hello'

@app.route("/login")
def login():
    return "Login"
@app.route("/register")
def register():
    return "Rehister"
app.run()