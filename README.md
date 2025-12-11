# 🎴 Playing Card Detection & Recognition using YOLOv8

This project builds a complete computer vision pipeline to **detect and classify playing cards** in images using a YOLOv8 model trained on **52 card classes** (A–K × 4 suits).  
The goal is to take an input image and output labeled bounding boxes such as:

- **“7H” (Seven of Hearts)**  
- **“KC” (King of Clubs)**  
- **“10D” (Ten of Diamonds)**  

This README documents the full pipeline: dataset, training, inference, evaluation, and results.

---

# 📌 1. Project Overview

Playing card recognition is a classic computer vision challenge involving:

- Object detection  
- Fine-grained classification  
- Handling rotation, lighting changes, and overlapping cards  

This project uses **YOLOv8n**, a lightweight yet powerful object detection model, making it suitable for a student project and demo.

---

# 📂 2. Dataset

The dataset comes from **Roboflow**, containing:

- **170 training images**  
- **20 validation images**  
- **10 test images**  
- **52 classes**, each representing a unique card (e.g., "AS", "7H", "QC")

The folder structure is:

data/detection/
├── train/
│ ├── images/
│ └── labels/
├── valid/
│ ├── images/
│ └── labels/
├── test/
│ ├── images/
│ └── labels/
└── data.yaml

# 🧠 3. Training the Model

Training was performed using YOLOv8n with 50 epochs.

Training Command
yolo detect train \ model=yolov8n.pt \ data=/Users/.../Final_Project/data/detection/data.yaml \ epochs=50 imgsz=640

### 📝 Notes

CPU training is slower but works fine.

YOLO saves outputs to:

runs/detect/trainX/

Inside this folder are:

weights/best.pt (final model)

results.png

confusion_matrix.png

PR_curve.png

# 🔍 4. Running Inference (Prediction)
YOLO CLI 
yolo detect predict \ model=runs/detect/train5/weights/best.pt \ source=data/detection/test/images \ conf=0.05

Predictions will be saved in:

runs/detect/predict/

# 5. Discussion

### Strengths
- The model performs well on clear, well-lit card images.
- YOLOv8n is fast and efficient, even on CPU.
- The system identifies all 52 card types reliably when visible.

### Challenges
- Some cards look very similar (e.g., 6H vs 9H).
- Red suits (hearts & diamonds) can be confused.
- Dataset size is small relative to 52 classes.
- CPU training is slow.

### Improvements
- Train for 100+ epochs or use YOLOv8s/m.
- Add more diverse training images.
- Use image augmentation (rotation, blur, shadows).
- Train on a GPU for faster experimentation.

Overall, the project successfully demonstrates playing card detection & classification using modern deep learning.


# 🏁 6. Conclusion

This project demonstrates a complete end-to-end playing card detection system using YOLOv8.
The model can detect and classify 52 unique card types and serves as a solid foundation for more advanced card recognition tasks.