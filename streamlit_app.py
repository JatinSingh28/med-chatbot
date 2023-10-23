import joblib
import streamlit as st
from functions import show_status, cancel, reschedule, greet, notWell
from model.func import predict_disease_and_symptoms

# Load the pre-trained models and data
classifier = joblib.load("svc_classifier")
vectorizer = joblib.load("vectorizer")
symptom_list = joblib.load("symptoms_list.joblib")

# Function to perform actions based on user input
def func(text):
    vtext = vectorizer.transform([text])
    pred = classifier.predict(vtext)[0]
    
    if pred == "Reschedule":
        return reschedule(text)
    elif pred == "Cancel":
        return cancel()
    elif pred == "Show Status":
        return show_status()
    elif pred == "Greet":
        return greet()
    else:
        return notWell()

# Function to extract symptoms from user input
symptoms = set()
def extract_symptoms(text):
    words = text.split()
    capitalized_text = ' '.join([word.capitalize() for word in words])
    f=0
    try:
        symptoms = joblib.load("extracted_symptoms")
    except:
        pass
    for symptom in symptom_list:
        if symptom in capitalized_text:
            symptoms.add(symptom)
            f=1
    # print(symptoms)
    joblib.dump(symptoms,"extracted_symptoms")
    return f==1, list(symptoms)

# Streamlit app
def main():
    st.title("Appointment Assistant")

    user_input = st.text_input("Input:", "") 
    if user_input == "exit":
        try:
            symptoms = joblib.load("extracted_symptoms")
            symptoms.clear()
            joblib.dump(symptoms,"extracted_symptoms")

        except:
            pass

    if user_input:
        # st.write(f"User Input: {user_input}")
        # print(user_input)
        string = func(user_input)
        st.write(string)
        extract_symptoms(string)
        
        # print("AA:",string)
        # flag,_ = extract_symptoms(user_input)
        try:
            symptoms = joblib.load("extracted_symptoms")
        except:
            pass
        # if flag:
        # if len(symptoms)==0:
        #     st.write(string)
            
        st.write("Extracted Symptoms:", symptoms)
        
        result = predict_disease_and_symptoms(list(symptoms))
        
        st.subheader("Possible Diseases:")
        for disease, probability in result['possible_diseases']:
            st.write(f"{disease} (Probability: {probability:.3f})")
        
        st.subheader("Possible Related Symptoms:")
        st.write(result['possible_related_symptoms'])

if __name__ == "__main__":
    main()
