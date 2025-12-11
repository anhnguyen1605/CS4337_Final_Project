# 🎴 Playing Card Detection & Recognition using YOLOv8

This project implements a complete computer vision pipeline to **detect
and classify playing cards** using a YOLOv8 model trained on **52
individual classes** (A--K × 4 suits).\
Given an input image, the system outputs labeled bounding boxes such as:

-   **"7H" --- Seven of Hearts**\
-   **"KC" --- King of Clubs**\
-   **"10D" --- Ten of Diamonds**

This repository documents the **dataset**, **training procedure**,
**inference pipeline**, **results**, and **discussion**.

## 📌 1. Project Overview

Playing card recognition is a common computer vision task that includes:

-   **Object detection**\
-   **Fine-grained classification**\
-   **Handling real-world variations** such as rotation, blur, lighting,
    shadows, and overlapping cards

We chose **YOLOv8n**, the smallest YOLOv8 model, because it is
lightweight, fast, and easy to train on CPU.

## 📂 2. Dataset

Dataset from Roboflow, with:

-   170 training images\
-   20 validation images\
-   10 test images\
-   52 classes (AS, 7H, QC, ...)

Folder structure:

    data/detection/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    ├── test/
    │   ├── images/
    │   └── labels/
    └── data.yaml

## 🧠 3. Training the Model

Trained using YOLOv8n for 50 epochs.

Command:

    yolo detect train     model=yolov8n.pt     data=./data/detection/data.yaml     epochs=50     imgsz=640

Outputs located in:

    runs/detect/trainX/

Includes metrics, curves, and best model weights.

## 🔍 4. Running Inference

    yolo detect predict     model=runs/detect/train5/weights/best.pt     source=data/detection/test/images     conf=0.05

Outputs saved to:

    runs/detect/predict/

## 📊 5. Results

Model detects and classifies most cards accurately. Handles rotation
well but sometimes confuses similar red-suit cards or 6/9 shapes.

## 💬 6. Discussion

### Strengths

-   Fast inference\
-   Handles all 52 classes\
-   Works well on clear images

### Challenges

-   Small dataset\
-   Red suits often confused\
-   CPU training is slow

### Improvements

-   Train longer (100--200 epochs)\
-   Use larger YOLO models\
-   Add augmentation\
-   Train on GPU

## 🏁 7. Conclusion

The project successfully implements a YOLOv8-based playing card
detection and classification system. Serves as foundation for real-time
card recognition, poker automation, or AR applications.

## 📎 8. Acknowledgments

-   Roboflow dataset\
-   Ultralytics YOLOv8\
-   CS4337 Computer Vision course
