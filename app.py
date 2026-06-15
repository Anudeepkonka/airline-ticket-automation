```python
import streamlit as st
import joblib
import re

# Load models
model = joblib.load("intent_model.pkl")
tfidf = joblib.load("tfidf.pkl")


def extract_entities(text):
    entities = {
        "name": None,
        "source": None,
        "destination": None,
        "travel_date": None
    }

    # Name
    name_match = re.search(r'for\s+(\w+)', text, re.IGNORECASE)
    if name_match:
        entities["name"] = name_match.group(1)

    # Source and Destination
    route_match = re.search(
        r'from\s+(\w+)\s+to\s+(\w+)',
        text,
        re.IGNORECASE
    )

    if route_match:
        entities["source"] = route_match.group(1)
        entities["destination"] = route_match.group(2)

    # Travel Date
    date_match = re.search(
        r'(tomorrow|today|next Monday|next Tuesday|next Wednesday|next Thursday|next Friday)',
        text,
        re.IGNORECASE
    )

    if date_match:
        entities["travel_date"] = date_match.group(1)

    return entities


st.title("✈️ Airline Ticket Booking Automation System")

email = st.text_area("Paste Customer Email")


if st.button("Analyze"):

    if email.strip():

        vector = tfidf.transform([email])

        intent = model.predict(vector)[0]

        confidence = round(
            float(max(model.predict_proba(vector)[0])) * 100,
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
```
