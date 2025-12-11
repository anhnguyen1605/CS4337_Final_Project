from ultralytics import YOLO
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
        return

    image_path = sys.argv[1]

    # Load your trained model
    model = YOLO("runs/detect/train4/weights/best.pt")

    # Run prediction
    results = model(image_path, save=True, conf=0.5)

    print("Prediction complete! Check the 'runs/detect/predict' folder.")

if __name__ == "__main__":
    main()
