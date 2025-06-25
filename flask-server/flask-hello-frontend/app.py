from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Pass dynamic data into the template if you want.
    return render_template("index.html", title="Hello Flask")

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json or {}
    return jsonify({"you_sent": data}), 200

if __name__ == "__main__":
    # Use debug only in dev
    app.run(debug=True, host="0.0.0.0", port=5002)
