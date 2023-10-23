from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from your_module import find_possible_disease_and_symptoms  # Import your function from your_module
import joblib
import numpy as np

disease_dict = joblib.load("./model/disease_dict")
nb_classifier = joblib.load("./model/nbClassifier.joblib")
symptoms = joblib.load("./model/symptoms_list.joblib")
le = joblib.load("./model/label_encoder.joblib")

app = FastAPI()

class SymptomInput(BaseModel):
    input_symptom: list


@app.get("/")
def greet():
    return "Hello, API running"

@app.post('/predict')
def predict_disease_and_symptoms(input_symptom: SymptomInput):
    try:
        print(input_symptom)
        print(type(input_symptom))
        input_symptom = input_symptom.input_symptom
        print(input_symptom)
        serlis = [1 if symptom in input_symptom else 0 for symptom in symptoms]
        prob = nb_classifier.predict_proba(np.expand_dims(serlis, axis=0))

        possible_diseases = []
        for i in range(len(prob[0])):
            if prob[0][i] > 0.1:
                possible_diseases.append((le.inverse_transform([i])[0],prob[0][i]))

        possible_related_symptoms = set()
        for disease in possible_diseases:
            print(disease[0])
            for symp in disease_dict[disease[0]]:
                possible_related_symptoms.add(symp)

        response = {
            "possible_diseases": possible_diseases,
            "possible_related_symptoms": list(possible_related_symptoms-set(input_symptom))
        }
        
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
