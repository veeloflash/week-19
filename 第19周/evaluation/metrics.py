def accuracy(tp, tn, fp, fn):
    total = tp + tn + fp + fn
    return (tp + tn) / total if total else 0.0


def precision(tp, fp):
    return tp / (tp + fp) if (tp + fp) else 0.0


def recall(tp, fn):
    return tp / (tp + fn) if (tp + fn) else 0.0


def f1_score(prec, rec):
    return 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
