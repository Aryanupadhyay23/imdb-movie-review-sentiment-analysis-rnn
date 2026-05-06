# app.py

import streamlit as st
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Page configuration

st.set_page_config(
    page_title="IMDB Sentiment Analysis",
    layout="wide"
)

# Constants

max_features = 10000
max_len = 500

# Load IMDB word index

word_index = imdb.get_word_index()

# Load trained model

@st.cache_resource
def load_sentiment_model():

    model = load_model(
        "model/best_simple_rnn_model.keras"
    )

    return model

model = load_sentiment_model()

# Encode review

def encode_review(text):

    words = text.lower().split()

    encoded_review = []

    for word in words:

        index = word_index.get(word, 2)

        encoded_review.append(index + 3)

    padded_review = pad_sequences(
        [encoded_review],
        maxlen=max_len
    )

    return padded_review

# Predict sentiment

def predict_sentiment(review):

    processed_text = encode_review(review)

    prediction = model.predict(processed_text)

    prediction_score = float(prediction[0][0])

    if prediction_score >= 0.5:
        sentiment = "Positive Review"
    else:
        sentiment = "Negative Review"

    return sentiment, prediction_score

# Sidebar

with st.sidebar:

    st.title("Example Reviews")

    st.success(
        "This movie was absolutely amazing with brilliant acting and emotional storytelling."
    )

    st.error(
        "The movie was boring, poorly written, and a complete waste of time."
    )

# Main title

st.title("IMDB Movie Review Sentiment Analysis")

st.write(
    "Enter a movie review and predict whether the sentiment is positive or negative."
)

# Layout

col1, col2 = st.columns([2, 1])

# Input section

with col1:

    st.subheader("Enter Movie Review")

    review = st.text_area(
        "Movie Review",
        height=250,
        placeholder="Write your movie review here..."
    )

    analyze_button = st.button(
        "Analyze Sentiment",
        use_container_width=True
    )

# Prediction section

with col2:

    st.subheader("Prediction Output")

    if analyze_button:

        if review.strip() == "":

            st.warning("Please enter a movie review.")

        else:

            sentiment, score = predict_sentiment(review)

            confidence = score * 100

            if score >= 0.5:

                st.success(
                    f"""
                    Prediction: {sentiment}

                    Confidence Score: {confidence:.2f}%
                    """
                )

                st.progress(float(score))

            else:

                st.error(
                    f"""
                    Prediction: {sentiment}

                    Confidence Score: {(100-confidence):.2f}%
                    """
                )

                st.progress(float(1 - score))

# Footer

st.divider()

st.caption(
    "Built using Streamlit and TensorFlow"
)