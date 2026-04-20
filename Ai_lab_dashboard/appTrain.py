from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

UPLOAD = "static/uploads"
LABELS = "dataset/labels"

os.makedirs(UPLOAD, exist_ok=True)
os.makedirs(LABELS, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]
    path = os.path.join(UPLOAD, file.filename)
    file.save(path)

    return jsonify({"path": path})


@app.route("/save_label", methods=["POST"])
def save_label():

    data = request.json

    filename = data["filename"]
    labels = data["labels"]

    label_path = os.path.join(LABELS, filename + ".json")

    with open(label_path, "w") as f:
        json.dump(labels, f)

    return jsonify({"status": "saved"})


if __name__ == "__main__":
    app.run(debug=True)