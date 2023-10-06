from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello_world!"


if __name__ == "name":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
