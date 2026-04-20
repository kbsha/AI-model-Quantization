from flask import Flask, request, jsonify
import json
import os
from trainer import Trainer

app = Flask(__name__)

trainer = Trainer()

os.makedirs("dataset/labels", exist_ok=True)


@app.route("/")
def index():
    return open("templates/index.html").read()

@app.route("/train")
def train():

    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset/data.yaml",
        epochs=10,
        imgsz=640
    )

    return "Training completed"


# @app.route("/save_annotations", methods=["POST"])
# def save_annotations():

#     data = request.json["boxes"]

#     yolo_lines = []

#     for box in data:

#         # convert to YOLO format (simplified)
#         x = box["x"] / 640
#         y = box["y"] / 640
#         w = box["w"] / 640
#         h = box["h"] / 640

#         class_id = 0  # single class MVP

#         yolo_lines.append(f"{class_id} {x} {y} {w} {h}")

#     with open("dataset/labels/sample.txt", "w") as f:
#         f.write("\n".join(yolo_lines))

#     trainer.train()

#     return jsonify({"status": "training started"})



@app.route("/save_annotations", methods=["POST"])
def save_annotations():

    data = request.json["boxes"]

    lines = []

    for b in data:

        x_center = b["x"] / 640
        y_center = b["y"] / 640
        w = b["w"] / 640
        h = b["h"] / 640

        class_id = 0

        lines.append(f"{class_id} {x_center} {y_center} {w} {h}")

    # SAVE TO YOLO FILE
    os.makedirs("dataset/labels/train", exist_ok=True)

    with open("dataset/labels/train/sample.txt", "w") as f:
        f.write("\n".join(lines))

    return {"status": "saved"}


if __name__ == "__main__":
    app.run(debug=True)