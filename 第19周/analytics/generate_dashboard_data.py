import json

from .statistics import question_statistics, error_analysis


def generate_dashboard_data(questions, labels, predictions, output_path):
    stats = question_statistics(questions)
    errors = error_analysis(questions, labels, predictions)

    data = {
        "question_counts": stats,
        "errors": errors,
        "accuracy": None,
        "precision": None,
        "recall": None,
        "f1": None,
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
