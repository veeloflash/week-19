def compute_confusion_matrix(true_labels, predicted_labels, positive_label="Coding"):
    tp = tn = fp = fn = 0
    for true, pred in zip(true_labels, predicted_labels):
        if true == positive_label and pred == positive_label:
            tp += 1
        elif true != positive_label and pred != positive_label:
            tn += 1
        elif true != positive_label and pred == positive_label:
            fp += 1
        elif true == positive_label and pred != positive_label:
            fn += 1
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}
