# Respiratory Disease Smart Assistant

AI-powered healthcare application that predicts respiratory diseases using symptom analysis and video-based respiratory pattern detection.

## Live Demo

Local:

http://localhost:8501

AWS Deployment:

http://16.170.240.217:8501

---

## Features

* Symptom-based respiratory disease prediction
* Video-based respiratory disease detection using YOLOv8
* User-friendly Streamlit interface
* Real-time prediction and confidence scores
* Machine Learning disease classification
* AI-assisted healthcare support

---

## Diseases Detected

* Asthma
* Pneumonia
* Respiratory Infection
* Normal Healthy Condition

---

## Technologies Used

* Python
* Streamlit
* YOLOv8
* OpenCV
* Scikit-learn
* Pandas
* NumPy
* Docker
* AWS EC2

---

## Project Structure

```text
Smart Healthcare/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── best.pt
├── respiratory_model.pkl
├── label_encoder.pkl
├── feature_encoders.pkl
├── dataset/
├── training/
└── runs/
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Smart-Healthcare
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Docker Deployment

Build Docker Image:

```bash
docker build -t respiratory-assistant .
```

Run Docker Container:

```bash
docker run -p 8501:8501 respiratory-assistant
```

Open:

```text
http://localhost:8501
```

---

## AWS Deployment

The application is deployed on an AWS EC2 instance using Docker.

Public URL:

```text
http://16.170.240.217:8501
```

---

## Workflow

1. User enters symptoms or uploads a respiratory video.
2. Machine Learning model predicts disease from symptoms.
3. YOLOv8 analyzes respiratory video patterns.
4. Disease prediction and confidence score are generated.
5. Results are displayed through the Streamlit dashboard.

---

## Future Enhancements

* X-ray image analysis
* RAG-based medical knowledge assistant
* Treatment recommendation system
* Doctor consultation support
* Medical report generation

---

## Author

Swathi G

B.Tech Artificial Intelligence and Machine Learning

Sri Shakthi Institute of Engineering and Technology
