from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Mera yeshu yeshu..... Bolna lagiiiii"

app.run(host="0.0.0.0", port=4000)
