# Fake News Detection using the LIAR Dataset

## Overview

This repository contains a **learning-oriented experimental project** for fake news detection using the **LIAR dataset**.  
The primary objective is **conceptual understanding**, not achieving state-of-the-art performance.

The project systematically explores **multiple NLP representations and modeling approaches**, ranging from classical machine learning to deep learning, to understand how text data flows through different pipelines and how modeling choices affect performance.

**Dataset source:** https://github.com/tfs4/liar_dataset

---

## Project Goals

- Understand how **raw text is transformed into numerical representations**
- Experiment with **different feature extraction techniques**
- Compare **classical ML models vs deep learning models**
- Observe **dimensionality changes and data flow**
- Practice **model evaluation, iteration, and debugging**

---

## Dataset Description

- **Dataset:** LIAR
- **Task Type:** Binary text classification (Fake vs Real)
- **Input Data:** Short political statements
- **Original Labels:** Multi-class → converted to binary
- **Data Splits:** Train / Validation / Test

---

## Experimentation Pipeline

The following modeling approaches were implemented and evaluated iteratively.

### 1. TF-IDF + Logistic Regression
- **Text Representation:** TF-IDF vectors
- **Classifier:** Logistic Regression
- **Purpose:**
  - Establish a strong baseline
  - Learn sparse, high-dimensional feature behavior

---

### 2. TF-IDF + XGBoost
- **Text Representation:** TF-IDF vectors
- **Classifier:** XGBoost
- **Purpose:**
  - Compare linear vs tree-based classifiers
  - Analyze overfitting on sparse feature spaces

---

### 3. TF-IDF + SVD + Logistic Regression / XGBoost
- **Text Representation:** TF-IDF
- **Dimensionality Reduction:** Truncated SVD
- **Classifiers:**
  - Logistic Regression
  - XGBoost
- **Purpose:**
  - Reduce sparsity
  - Capture latent semantic structure
  - Improve training efficiency

---

### 4. BERT Embeddings + Logistic Regression / XGBoost
- **Text Representation:** Pretrained BERT sentence embeddings
- **Classifiers:**
  - Logistic Regression
  - XGBoost
- **Purpose:**
  - Decouple feature extraction from classification
  - Compare pretrained deep embeddings with classical ML

---

### 5. BERT Embeddings + MLP
- **Encoder:** Pretrained BERT (frozen)
- **Classifier:** Multi-Layer Perceptron
- **Purpose:**
  - Learn non-linear decision boundaries
  - Transition from classical ML to neural models

---

### 6. LSTM (End-to-End Deep Learning)
- **Tokenization:** Keras Tokenizer
- **Embedding Layer:**
  - `input_dim = vocabulary_size`
  - `output_dim = embedding_dimension`
- **Architecture:**
  - Embedding → LSTM → Dense
- **Purpose:**
  - Learn sequential dependencies in text
  - Understand padding, masking, and sequence modeling
  - Handle class imbalance using class weights

---

## Key Concepts Learned

- Tokenization vs vectorization
- Sparse vs dense text representations
- Dimensionality reduction using SVD
- Pretrained embeddings vs learned embeddings
- Bag-of-words vs sequence-based models
- Class imbalance handling
- Shape mismatches and neural network debugging

---

## Project Nature

- This project is **experimental and educational**
- Multiple approaches were tried intentionally
- Suboptimal results are expected and informative
- Emphasis is on **understanding model behavior**, not optimization

