# IMDB Movie Review Sentiment Analysis using SimpleRNN

An end-to-end Deep Learning based Natural Language Processing project that performs sentiment analysis on IMDB movie reviews using Word Embeddings and SimpleRNN architecture. The application predicts whether a movie review is Positive or Negative through a Streamlit web interface.

---

## Project Overview

This project focuses on building a complete NLP pipeline for sentiment analysis using Recurrent Neural Networks. The model is trained on the IMDB Movie Reviews Dataset and deployed as an interactive Streamlit application.

The system takes movie reviews as input, processes the text using integer encoding and padding techniques, and predicts sentiment using a trained SimpleRNN model.

---

## Key Features

- End-to-end NLP workflow
- Deep Learning based sentiment analysis
- Word Embedding implementation
- SimpleRNN sequence modeling
- Real-time sentiment prediction
- Streamlit web application
- Learning rate scheduling
- Early stopping implementation
- Model checkpoint saving
- Custom review prediction support
- Interactive user interface

---

## Dataset Information

The project uses the IMDB Movie Reviews Dataset provided by TensorFlow/Keras.

Dataset characteristics:

- 50,000 movie reviews
- Binary sentiment classification
- Positive and Negative labels
- Preprocessed integer encoded sequences
- Balanced dataset distribution

---

## Deep Learning Workflow

The project follows a complete Deep Learning pipeline:

1. Dataset Loading  
2. Text Preprocessing  
3. Integer Encoding  
4. Sequence Padding  
5. Word Embedding Generation  
6. SimpleRNN Training  
7. Model Evaluation  
8. Streamlit Deployment  
9. Real-Time Prediction  

---

## Model Architecture

The model architecture includes:

- Input Layer
- Embedding Layer
- SimpleRNN Layer
- Dense Output Layer
- Sigmoid Activation Function

The Embedding Layer converts words into dense vector representations, while the SimpleRNN captures sequential dependencies from review text.

---

## Training Strategy

The model was trained using multiple optimization techniques to improve performance and prevent overfitting.

Training techniques used:

- Adam Optimizer
- Binary Crossentropy Loss
- EarlyStopping Callback
- ReduceLROnPlateau Callback
- ModelCheckpoint Callback

The learning rate was automatically reduced during training whenever validation loss stopped improving.

---

## Training Performance

The model achieved strong sentiment classification performance on the IMDB dataset.

Highlights:

- Validation Accuracy around 84%
- Automatic learning rate scheduling
- Early stopping for overfitting prevention
- Best model restoration after training

---

## Streamlit Application

The project includes a fully interactive Streamlit application where users can:

- Enter custom movie reviews
- Predict sentiment instantly
- View confidence scores
- Test positive and negative reviews
- Interact with the trained Deep Learning model

The application performs preprocessing internally before sending input to the trained model.

---

## NLP Concepts Used

This project demonstrates practical implementation of:

- Natural Language Processing
- Word Embeddings
- Sequence Modeling
- Sentiment Analysis
- Recurrent Neural Networks
- Text Vectorization
- Sequence Padding
- Binary Classification

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Streamlit
- Matplotlib

---

## Project Structure

The project contains:

- Deep Learning training notebook
- Saved trained model
- Streamlit application
- Requirements file
- Documentation

---

## Real-World Applications

This type of sentiment analysis system can be applied in:

- Movie review analysis
- Product review analysis
- Social media sentiment tracking
- Customer feedback systems
- Brand reputation monitoring
- Opinion mining systems

---

## Future Improvements

Potential improvements for future development:

- Replace SimpleRNN with LSTM
- Add GRU architecture
- Implement Attention Mechanism
- Deploy using Docker
- Deploy on Hugging Face Spaces
- Add multilingual sentiment analysis
- Improve UI/UX design
- Add explainable AI features

---

## Learning Outcomes

Through this project, the following concepts were explored:

- NLP preprocessing pipelines
- Deep Learning model development
- Sequence-based neural networks
- TensorFlow/Keras workflows
- Model optimization techniques
- Streamlit deployment
- Real-time inference systems

---

## Conclusion

This project demonstrates how Deep Learning can be applied to Natural Language Processing tasks such as sentiment analysis. By combining Word Embeddings with SimpleRNN architecture, the system successfully learns contextual patterns from movie reviews and predicts sentiment effectively.

The project also showcases practical deployment of Deep Learning models using Streamlit for real-world interactive applications.