from .cv_classifier import Classifier as CVClassifier
from .nlp_classifier import Classifier as NLPClassifier

def build_demo() -> tuple[str, str]:
    return CVClassifier().domain, NLPClassifier().domain
