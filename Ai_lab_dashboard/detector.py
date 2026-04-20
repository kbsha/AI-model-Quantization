from ultralytics import YOLO
import cv2

class Detector:

    def __init__(self, model_path="models/v1.pt"):

        self.model = YOLO(model_path)

    def predict(self, img_path):

        img = cv2.imread(img_path)

        results = self.model(img)[0]

        return results.plot()