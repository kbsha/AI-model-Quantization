import cv2
import os
from ultralytics import YOLO

class Detector:

    def __init__(self):

        self.model = YOLO("models/best.pt")

        # COCO-style labels (edit if custom dataset)
        self.names = self.model.names if hasattr(self.model, "names") else {}

    def detect(self, image_path):

        img = cv2.imread(image_path)

        results = self.model(img)[0]

        detected_objects = []

        for box in results.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            name = self.names.get(cls, str(cls))

            detected_objects.append(f"{name} ({conf:.2f})")

        annotated = results.plot()

        output_path = image_path.replace("uploads", "results")

        cv2.imwrite(output_path, annotated)

        return output_path, detected_objects