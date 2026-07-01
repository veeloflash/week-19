import json

from .features import build_tfidf_features
from .knn_model import KNNModel


class Predictor:
    def __init__(self, n_neighbors=3):
        self.knn = KNNModel(n_neighbors=n_neighbors)
        self.vectorizer = None

    def train(self, questions, labels):
        corpus = [question["question"] for question in questions]
        self.vectorizer, X = build_tfidf_features(corpus)
        y = [label["label"] for label in labels]
        self.knn.fit(X, y)

    def predict(self, questions):
        corpus = [question["question"] for question in questions]
        X = self.vectorizer.transform(corpus)
        return self.knn.predict(X).tolist()

    def save_predictions(self, questions, predictions, output_path):
        results = [
            {"id": question["id"], "question": question["question"], "prediction": prediction}
            for question, prediction in zip(questions, predictions)
        ]
        with open(output_path, "w", encoding="utf-8") as out_file:
            json.dump(results, out_file, ensure_ascii=False, indent=2)
