import matplotlib.pyplot as plt
import numpy as np
import yaml
import os

RUN_DIR = "runs/detect/train4"  # adjust if needed

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def plot_confusion_matrix():
    cm_path = os.path.join(RUN_DIR, "confusion_matrix.png")
    if os.path.exists(cm_path):
        print(f"Confusion matrix saved at: {cm_path}")
    else:
        print("Confusion matrix not found. YOLO generates this after evaluation.")

def plot_pr_curve():
    pr_path = os.path.join(RUN_DIR, "PR_curve.png")
    if os.path.exists(pr_path):
        print(f"Precision Recall curve at: {pr_path}")
    else:
        print("PR curve not found. YOLO generates this after validation.")

if __name__ == "__main__":
    plot_confusion_matrix()
    plot_pr_curve()
