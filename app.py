
import streamlit as st
import joblib
import spacy
import re

# Load models
model = joblib.load("intent_model.pkl")
tfidf = joblib.load("tfidf.pkl")
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "name": None,
        "source": None,
        "destination": None,
        "travel_date": None
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["name"] = ent.text

        elif ent.label_ == "DATE":
            entities["travel_date"] = ent.text

    match = re.search(r'from\\s+(\\w+)\\s+to\\s+(\\w+)', text, re.IGNORECASE)

    if match:
        entities["source"] = match.group(1)
        entities["destination"] = match.group(2)

    return entities

st.title("✈️ Airline Ticket Booking Automation System")

email = st.text_area("Paste Customer Email")

if st.button("Analyze"):

    if email.strip():

        vector = tfidf.transform([email])

        intent = model.predict(vector)[0]

        confidence = round(
            max(model.predict_proba(vector)[0]) * 100,
            2
        )

        entities = extract_entities(email)

        st.success("Analysis Complete")

        st.write("### Intent")
        st.write(intent)

        st.write("### Confidence")
        st.write(f"{confidence}%")

        st.write("### Extracted Details")
        st.json(entities)

    else:
        st.warning("Please enter an email.")
