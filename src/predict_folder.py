from ultralytics import YOLO
import glob, os

def main():
    folder = "data/detection/test/images/"

    model = YOLO("runs/detect/train4/weights/best.pt")

    images = glob.glob(os.path.join(folder, "*.jpg"))

    print(f"Running inference on {len(images)} images...")

    for img in images:
        model(img, save=True, conf=0.5)

    print("All predictions saved to runs/detect/predict/")

if __name__ == "__main__":
    main()
