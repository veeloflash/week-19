from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf_features(corpus):
    """Extract TF-IDF features from a list of text documents."""
    vectorizer = TfidfVectorizer(stop_words="english")
    features = vectorizer.fit_transform(corpus)
    return vectorizer, features
