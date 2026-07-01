import random

from .confusion import compute_confusion_matrix
from .metrics import accuracy, precision, recall, f1_score


def create_imbalanced_dataset(questions, labels, math_ratio=0.9):
    math_items = [q for q in questions if q["category"] == "Math"]
    coding_items = [q for q in questions if q["category"] == "Coding"]

    target_math = int(len(questions) * math_ratio)
    selected_math = math_items[:target_math]
    selected_coding = coding_items[: max(1, len(questions) - target_math)]

    combined = selected_math + selected_coding
    random.shuffle(combined)

    imbalanced_labels = [next(label["label"] for label in labels if label["id"] == item["id"]) for item in combined]
    return combined, imbalanced_labels


def run_experiment(true_labels, predicted_labels):
    cm = compute_confusion_matrix(true_labels, predicted_labels, positive_label="Coding")
    prec = precision(cm["TP"], cm["FP"])
    rec = recall(cm["TP"], cm["FN"])
    f1 = f1_score(prec, rec)
    acc = accuracy(cm["TP"], cm["TN"], cm["FP"], cm["FN"])
    return {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1, "confusion_matrix": cm}
