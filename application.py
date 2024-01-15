from flask import Flask, jsonify, render_template
from quote import breaking_quote

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quote")
def quote():
  random_quote = breaking_quote()
  return jsonify({ "quote": random_quote })


if __name__ == "__main__":
    app.run(debug=True).run(debug=True)