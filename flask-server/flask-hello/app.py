from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json or {}
    return jsonify({"you_sent": data}), 200

if __name__ == "__main__":
    # Production servers (gunicorn, uvicorn, etc.) handle this differently.
    app.run(debug=True, host="0.0.0.0", port=5000)
