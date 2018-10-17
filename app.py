# -------- Flask hello World --------- #
from flask import Flask

app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello World!!"

if __name__ == '__main__':
    app.run()

