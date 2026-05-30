from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("respiratory_model.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))
encoders = pickle.load(open("feature_encoders.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    age = int(request.form['age'])
    gender = request.form['gender']
    symptom1 = request.form['symptom1']
    symptom2 = request.form['symptom2']
    symptom3 = request.form['symptom3']

    gender = encoders["gender"].transform([gender])[0]
    symptom1 = encoders["symptom_1"].transform([symptom1])[0]
    symptom2 = encoders["symptom_2"].transform([symptom2])[0]
    symptom3 = encoders["symptom_3"].transform([symptom3])[0]

    data = [[age, gender, symptom1, symptom2, symptom3]]

    prediction = model.predict(data)

    result = label_encoder.inverse_transform(prediction)[0]

    return render_template(
        'index.html',
        prediction_text=f"Predicted Disease: {result}"
    )

if __name__ == "__main__":
    app.run(debug=True)