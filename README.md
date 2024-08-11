# Banknote Classifier API

This repository provides a Flask-based API that serves a preprocessed CSV dataset. The dataset includes various features related to banknote classification, and the API is designed to facilitate data analysis and machine learning tasks.

## Overview

The API allows you to:

- Access the entire dataset in JSON format.
- Query the dataset based on specific column values.

### Features

- **Dataset**: The dataset contains features such as variance, skewness, kurtosis, and entropy, along with a class label indicating the authenticity of the banknote.
- **Swagger Documentation**: Swagger UI is integrated to provide interactive API documentation and testing.

## Getting Started

### Prerequisites

Ensure you have Python installed. It’s recommended to use a virtual environment.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/banknote-classifier-api.git
   cd banknote-classifier-api
