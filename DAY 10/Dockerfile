FROM ultralytics/ultralytics:latest

WORKDIR /app

COPY . .

RUN pip install --default-timeout=1000 --retries 20 streamlit scikit-learn

EXPOSE 8501

CMD ["streamlit","run","app.py","--server.address=0.0.0.0","--server.port=8501"]