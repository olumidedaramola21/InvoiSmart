from datetime import datetime
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    today = datetime.today().strftime("%B %#d, %Y")
    return render_template("invoice.html", date=today)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
