import streamlit as st
import joblib
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

# ==============================
# Load TF-IDF artefak
# ==============================
@st.cache_resource
def load_tfidf():
    model = joblib.load("results/tf-idf/logreg_model_with_aug.joblib")
    vec_word = joblib.load("results/tf-idf/tfidf_word_vectorizer_with_aug.joblib")
    vec_char = joblib.load("results/tf-idf/tfidf_char_vectorizer_with_aug.joblib")
    return model, vec_word, vec_char

# ==============================
# Load IndoBERTweet dari HF Hub
# ==============================
@st.cache_resource
def load_indobertweet():
    model_name = "rilliaa//sentry-id-indobertweet"  # ganti dengan repo HF Anda
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

# ==============================
# Prediction functions
# ==============================
def predict_tfidf(text, model, vec_word, vec_char):
    X_word = vec_word.transform([text])
    X_char = vec_char.transform([text])
    from scipy.sparse import hstack
    X = hstack([X_word, X_char])
    probs = model.predict_proba(X)[0]
    pred = model.classes_[np.argmax(probs)]
    return pred, dict(zip(model.classes_, probs))

def predict_indobertweet(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].numpy()
    pred_id = np.argmax(probs)
    labels = list(model.config.id2label.values())
    return labels[pred_id], dict(zip(labels, probs))

# ==============================
# Streamlit UI
# ==============================
st.title("🛡️ Sentry-ID Level 1 — MVP Gambling Detector")

option = st.sidebar.selectbox("Choose Model:", ["TF-IDF + Logistic Regression", "IndoBERTweet"])

text = st.text_area("Enter a YouTube comment:", height=100)

if st.button("Predict"):
    if option == "TF-IDF + Logistic Regression":
        model, vec_word, vec_char = load_tfidf()
        pred, probs = predict_tfidf(text, model, vec_word, vec_char)
    else:
        tokenizer, model = load_indobertweet()
        pred, probs = predict_indobertweet(text, tokenizer, model)

    st.markdown(f"### 🔮 Prediction: **{pred}**")
    st.json(probs)
