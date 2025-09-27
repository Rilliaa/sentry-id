## 🚀 Live Demo

### 1. Streamlit App
Try the interactive demo on **Streamlit Cloud**:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sentry-id-ww5vv8cgu4cfmbudssbdeg.streamlit.app/)

Features:
- Input any YouTube comment in Indonesian
- Choose between:
  - **TF-IDF + Logistic Regression** (Baseline)
  - **IndoBERTweet (Fine-tuned)** (Advanced)
- Get prediction + class probabilities

---

### 2. Hugging Face Model Card
Fine-tuned IndoBERTweet is also published on Hugging Face Hub:  
👉 [rilliaa/sentry-id-indobertweet](https://huggingface.co/rilliaa/IndoBERTweet_with_aug)

Usage:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "rilliaa/sentry-id-indobertweet"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Main judi online bikin rugi, temen gue sampai berhutang"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
print(probs)
