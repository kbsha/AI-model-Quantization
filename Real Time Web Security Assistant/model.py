from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-sms-spam-detection"
)

def predict_text(text):
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    return {
        "prediction": label,
        "confidence": round(score * 100, 2)
    }