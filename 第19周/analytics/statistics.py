import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def question_statistics(questions):
    counts = {}
    for item in questions:
        counts[item["category"]] = counts.get(item["category"], 0) + 1
    return counts


def error_analysis(questions, labels, predictions):
    label_map = {item["id"]: item["label"] for item in labels}
    results = []
    for item, pred in zip(questions, predictions):
        true_label = label_map[item["id"]]
        if true_label != pred:
            results.append({"id": item["id"], "question": item["question"], "true": true_label, "predicted": pred})
    return results
