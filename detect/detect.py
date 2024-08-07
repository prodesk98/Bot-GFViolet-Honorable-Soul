from os import PathLike

from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator


class Detect:
    def __init__(self):
        self.model = YOLO("model/gf0.pt")

    def predict(self, path: str | PathLike):
        results = self.model.predict(path)

        img = cv2.imread(path)
        annotator = Annotator(img)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls
                annotator.box_label(b, self.model.names[int(c)])
        annotator.result()
        cv2.imwrite(
            f"predicted.jpg",
            img
        )


if __name__ == "__main__":
    de = Detect()
    print(de.predict("./img.png"))
