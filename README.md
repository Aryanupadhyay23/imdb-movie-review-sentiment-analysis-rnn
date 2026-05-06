# IMDB Movie Review Sentiment Analysis using SimpleRNN

<p align="center">
  Deep Learning based NLP project for real-time movie review sentiment classification using TensorFlow, Keras, and Streamlit.
</p>

---

## Overview

This project is an end-to-end Natural Language Processing application that classifies IMDB movie reviews as either Positive or Negative using a Recurrent Neural Network architecture.

The system learns semantic relationships and contextual patterns from text data through Word Embeddings and sequence modeling using SimpleRNN.

The project covers the complete Deep Learning workflow including:

- Text preprocessing
- Sequence padding
- Word embeddings
- Recurrent Neural Networks
- Model optimization
- Training callbacks
- Streamlit deployment
- Docker deployment

---

## Demo Features

- Real-time sentiment prediction
- Interactive Streamlit web application
- Positive and negative review classification
- Confidence score visualization
- Custom user review input
- Deep Learning based inference system

---

## Dataset Information

The project uses the IMDB Movie Reviews Dataset available through TensorFlow/Keras.

### Dataset Details

| Feature | Value |
|---|---|
| Total Reviews | 50,000 |
| Classification Type | Binary |
| Labels | Positive / Negative |
| Dataset Type | Preprocessed Text Sequences |

---

## NLP Pipeline

```text
Movie Review
     ↓
Text Cleaning
     ↓
Integer Encoding
     ↓
Sequence Padding
     ↓
Embedding Layer
     ↓
SimpleRNN Layer
     ↓
Dense Layer
     ↓
Sentiment Prediction
```

---

## Deep Learning Architecture

The model architecture consists of:

### Embedding Layer
Transforms integer encoded words into dense vector representations.

### SimpleRNN Layer
Captures sequential and contextual information from movie reviews.

### Dense Output Layer
Produces final sentiment probability using sigmoid activation.

---

## Training Strategy

To improve model performance and prevent overfitting, multiple training optimization techniques were used.

### Optimization Techniques

- Adam Optimizer
- Binary Crossentropy Loss
- EarlyStopping
- ReduceLROnPlateau
- ModelCheckpoint

### Callback Benefits

| Callback | Purpose |
|---|---|
| EarlyStopping | Prevents overfitting |
| ReduceLROnPlateau | Dynamically reduces learning rate |
| ModelCheckpoint | Saves best model automatically |

---

## Model Performance

### Final Test Results

| Metric | Score |
|---|---|
| Test Accuracy | 82.07% |
| Test Loss | 0.4215 |

---

### Best Validation Results

| Metric | Score |
|---|---|
| Validation Accuracy | 84.18% |
| Validation Loss | 0.4173 |

---

## Training Insights

During training:

- Validation loss improved significantly in early epochs
- Learning rate scheduling stabilized convergence
- Early stopping prevented unnecessary training
- Best model weights were restored automatically

The model achieved stable generalization performance on unseen IMDB reviews.

---

## Streamlit Application

The project includes a fully interactive Streamlit application for real-time sentiment analysis.

### Application Features

- User-friendly interface
- Instant prediction system
- Confidence score display
- Example positive and negative reviews
- Real-time NLP inference

---

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| NLP | Word Embeddings, SimpleRNN |
| Frontend | Streamlit |
| Visualization | Matplotlib |
| Deployment | Docker, Hugging Face |

---

## Project Structure

```text
IMDB-Sentiment-Analysis/
│
├── model/
│   └── best_simple_rnn_model.keras
│
├── notebooks/
│   └── text_classification.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Real-World Applications

This type of sentiment analysis system can be applied in:

- Movie review analysis
- Product review classification
- Customer feedback analysis
- Social media monitoring
- Brand reputation analysis
- Opinion mining systems

---

## Future Improvements

Future enhancements planned for the project:

- Replace SimpleRNN with LSTM
- Add GRU architecture
- Implement Attention Mechanism
- Improve UI/UX design
- Add multilingual sentiment analysis
- Build scalable API deployment
- Add explainable AI features

---

## Key Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing
- Word Embeddings
- Sequence Modeling
- Recurrent Neural Networks
- TensorFlow/Keras workflows
- Deep Learning optimization
- Streamlit deployment
- Model evaluation and inference

---

## Conclusion

This project demonstrates how Deep Learning and Recurrent Neural Networks can be effectively applied to Natural Language Processing tasks such as sentiment analysis.

Using Word Embeddings and SimpleRNN architecture, the model successfully learns contextual patterns from IMDB movie reviews and predicts sentiment with strong performance.

The project also highlights practical deployment of Deep Learning systems using Streamlit and Docker for real-world applications.

---