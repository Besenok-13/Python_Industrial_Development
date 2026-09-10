from dataclasses import dataclass
from .classifier import classify

@dataclass
class RequestRouter:
    def route(self, text: str) -> str:
        return classify(text)
