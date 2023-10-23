import joblib 
from functions import show_status, cancel, reschedule, greet, notWell, schedule
from model.func import predict_disease_and_symptoms

classifier = joblib.load("svc_classifier")
vectorizer = joblib.load("vectorizer")
symptom_list = joblib.load("symptoms_list.joblib")


def func(text):
    vtext = vectorizer.transform([text])
    pred = classifier.predict(vtext)
    # print(pred)
    if pred == "Reschedule":
        return reschedule(text)
    elif pred == "Cancel":
        return cancel()
    elif pred == "Show Status":
        return show_status()
    elif pred == "Greet":
        return greet()
    elif pred == "Schedule":
        return schedule(text)
    else:
        return notWell()

symptoms = set()
def extract_symptoms(text):
    words = text.split()
    capitalized_text = ' '.join([word.capitalize() for word in words])
    
    for symptom in symptom_list:
        # print(symptom)
        if symptom in capitalized_text:
            symptoms.add(symptom)

    # for word in capitalized_text:
    #     if word in symptom_list:
    #         symptoms.add(word) 

while True:
    text = input("Input:")
    if text == "exit":
        break
    string = func(text)
    print(string)
    extract_symptoms(text)
    # list(symptoms)
    print(list(symptoms))
    if len(symptoms)!=0:
        result = predict_disease_and_symptoms(list(symptoms))
        # print(result['possible_diseases'])
        # possible_diseases = result.possible_diseases
        # print(possible_diseases)
        for dis in result['possible_diseases']:
            print(dis[0],"***Probability: {:.3f}***".format(dis[1]))
        print("similar possible symptoms occuring symptoms:")
        print(result['possible_related_symptoms'])
    
    
# func("Hii I want to reschedule my appointment to tomorrow")
# func("Please cancel my appointment")
# func("show my appointment status")
