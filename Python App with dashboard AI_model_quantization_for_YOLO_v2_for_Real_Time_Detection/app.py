from flask import Flask, render_template, request
import os
from detector import Detector

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

detector = Detector()


@app.route("/", methods=["GET", "POST"])
def index():

    result_img = None
    explanation = None
    objects = []

    if request.method == "POST":

        file = request.files["image"]

        if file:

            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            result_img, objects = detector.detect(path)

            explanation = generate_explanation(objects)

    return render_template(
        "index.html",
        result_img=result_img,
        explanation=explanation,
        objects=objects
    )


def generate_explanation(objects):

    if not objects:
        return "No objects detected in this image."

    text = "This image contains: " + ", ".join(objects) + "."

    if "person" in str(objects):
        text += " A person is detected, indicating human presence in the scene."

    if "car" in str(objects):
        text += " Vehicles detected suggest traffic or road environment."

    return text


if __name__ == "__main__":
    app.run(debug=True)