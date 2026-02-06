import joblib

model = joblib.load("intent_classifier.pkl")

def classify_rule_based(prompt: str) -> str:
    p = prompt.lower()

    if any(k in p for k in ["ignore rules", "jailbreak", "override"]):
        return "prompt_injection"

    if any(k in p for k in ["delete", "drop", "truncate"]):
        return "destructive"

    if len(p.split()) < 3:
        return "nonsense"

    return "read_query"

def classify_ml(prompt: str) -> str:
    return model.predict([prompt])[0]
