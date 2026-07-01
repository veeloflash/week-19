import json

from model.predictor import Predictor
from evaluation.confusion import compute_confusion_matrix
from evaluation.metrics import accuracy, precision, recall, f1_score
from analytics.generate_dashboard_data import generate_dashboard_data


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    questions = load_json("data/questions.json")
    labels = load_json("data/labels.json")
    predictions_data = load_json("data/predictions.json")

    predictor = Predictor()
    predictor.train(questions, labels)
    predictions = predictor.predict(questions)

    true_labels = [label["label"] for label in labels]
    cm = compute_confusion_matrix(true_labels, predictions, positive_label="Coding")
    prec = precision(cm["TP"], cm["FP"])
    rec = recall(cm["TP"], cm["FN"])
    f1 = f1_score(prec, rec)
    acc = accuracy(cm["TP"], cm["TN"], cm["FP"], cm["FN"])

    print("Confusion Matrix:", cm)
    print(f"Accuracy: {acc:.2f}")
    print(f"Precision: {prec:.2f}")
    print(f"Recall: {rec:.2f}")
    print(f"F1 Score: {f1:.2f}")

    predictions_output = [
        {"id": q["id"], "prediction": pred}
        for q, pred in zip(questions, predictions)
    ]
    with open("data/predictions.json", "w", encoding="utf-8") as file:
        json.dump(predictions_output, file, ensure_ascii=False, indent=2)

    dashboard_data = {
        "question_counts": {"Math": 2, "Coding": 2},
        "errors": [],
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1": f1,
    }
    with open("dashboard/dashboard_data.json", "w", encoding="utf-8") as file:
        json.dump(dashboard_data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
