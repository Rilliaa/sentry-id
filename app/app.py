# app/app.py
# 🛡️ Sentry-ID Level 1 — Streamlit Demo

import streamlit as st
import joblib
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sentry-ID Judol Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Sentry-ID Level 1 — MVP Gambling Detector")
st.markdown("Klasifikasi komentar YouTube ke dalam **PROMO_JUDOL**, **RISKY**, atau **NORMAL**.")

# -----------------------------
# Load Models
# -----------------------------

@st.cache_resource
def load_tfidf_model():
    word_vectorizer = joblib.load("results/tfidf/tfidf_word_vecctorizer_with_aug.joblib")
    model = joblib.load("results/tfidf/logreg_model_with_aug.joblib")
    return word_vectorizer, model

@st.cache_resource
def load_indobertweet_model():
    model_name = "indolem/indobertweet-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        "results/indobertweet"  # ganti ke path lokal model Anda
    )
    return tokenizer, model

word_vectorizer, tfidf_model = load_tfidf_model()
tokenizer, indobert_model = load_indobertweet_model()

label_names = ["NORMAL", "PROMO_JUDOL", "RISKY"]

# -----------------------------
# Prediction Functions
# -----------------------------
def predict_tfidf(text):
    vec = word_vectorizer.transform([text])
    probs = tfidf_model.predict_proba(vec)[0]
    pred = label_names[np.argmax(probs)]
    return pred, dict(zip(label_names, probs))

def predict_indobert(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = indobert_model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].cpu().numpy()
    pred = label_names[np.argmax(probs)]
    return pred, dict(zip(label_names, probs))

# -----------------------------
# UI
# -----------------------------
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.radio(
    "Pilih model:",
    ["TF-IDF + Logistic Regression", "IndoBERTweet"]
)

user_input = st.text_area("💬 Masukkan komentar YouTube:", "")

if st.button("🔍 Deteksi"):
    if not user_input.strip():
        st.warning("Silakan masukkan komentar terlebih dahulu.")
    else:
        if model_choice == "TF-IDF + Logistic Regression":
            pred, probs = predict_tfidf(user_input)
        else:
            pred, probs = predict_indobert(user_input)

        st.markdown(f"### ✅ Prediksi: **{pred}**")
        st.write("Probabilitas:")
        st.json({k: float(v) for k, v in probs.items()})

