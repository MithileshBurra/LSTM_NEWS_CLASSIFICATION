# LSTM_NEWS_CLASSIFICATION
Overview
This project is an end-to-end News Classification system built using a BiLSTM-based deep learning model trained on the AG News dataset. The system classifies news articles into four categories:

World
Sports
Business
Sci/Tech
The solution is production-oriented and includes a RESTful API backend, a containerized deployment setup, and a cloud-hosted interactive frontend.

Architecture
The system follows a clean separation between backend and frontend services:

User
→ Streamlit Frontend
→ FastAPI Backend
→ BiLSTM Model

The backend is responsible for model inference and API handling.
The frontend provides a user interface for submitting text and viewing predictions.
The model and tokenizer artifacts are persisted to ensure consistent inference.

Model Details
Architecture: Embedding → BiLSTM → BiLSTM → Dense (Softmax)
Framework: TensorFlow / Keras
Dataset: AG News
Input preprocessing:

Lowercasing
Removal of URLs, HTML, numbers, and punctuation
Whitespace normalization
Tokenizer saved using tokenizer.to_json() and reloaded using tokenizer_from_json() to prevent training-inference drift.
Maximum sequence length: 400 tokens

Backend
Framework: FastAPI
Features:

RESTful inference endpoint
Batch prediction support
Structured JSON request and response schemas
Model loaded once at application startup
Containerized using Docker
Deployed on Render
API Endpoint
POST /predict

Request format:

{
"texts": ["sentence1", "sentence2"]
}

Response format:

[
{
"Sentence": "processed text",
"Category": "World",
"Confidence": 0.92
}
]

Live API Documentation:

https://lstm-news-classification.onrender.com/docs


Frontend
Framework: Streamlit
Features:

Single and batch prediction support
Confidence score display
Real-time API integration using HTTP requests
Deployed on Streamlit Cloud
Live Application:

https://lstmnewsclassification-9qm4ncektfyr8uuhhtzqop.streamlit.app/


Project Structure
LSTM_NEWS_CLASSIFICATION/
│
├── backend/
│ ├── app.py
│ ├── Prediction.py
│ ├── Dockerfile
│ ├── requirements.txt
│ └── Model/
│
├── frontend/
│ ├── streamlit_app.py
│ ├── requirements.txt
│ └── runtime.txt
│
└── README.md


Local Setup
Backend
Navigate to the backend folder:
cd backend

Install dependencies:
pip install -r requirements.txt

Run the API:
uvicorn app:app --reload

Access documentation at:
http://127.0.0.1:8000/docs


Frontend
Navigate to the frontend folder:
cd frontend

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run streamlit_app.py


Docker Deployment
To build and run the backend container locally:

cd backend
docker build -t news-api .
docker run -p 8000:8000 news-api

Access:

http://localhost:8000/docs


Key Features
End-to-end deep learning pipeline
Batch inference support
Clean separation of frontend and backend
Dockerized backend for environment consistency
Cloud deployment on Render and Streamlit Cloud
Persistent tokenizer and model artifacts to ensure reproducible inference

Author
Mithilesh Burra
Machine Learning and AI Engineer
