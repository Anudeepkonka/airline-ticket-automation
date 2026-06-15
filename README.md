# ✈️ Airline Ticket Booking Automation System

## Live Demo

🔗 Streamlit App: [https://YOUR-STREAMLIT-URL.streamlit.app](https://airline-ticket-automation-laqrlqmn6jtlhhfbeoungc.streamlit.app/)

## Project Overview

This project automates the processing of airline customer emails using Machine Learning and NLP techniques.

### Features

* Intent Classification

  * Book Flight
  * Cancel Flight
  * Reschedule Flight
  * General Inquiry

* Entity Extraction

  * Passenger Name
  * Source
  * Destination
  * Travel Date

* Interactive Streamlit Interface

## Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas
* NumPy
* Joblib
* Regular Expressions

## Machine Learning Workflow

Customer Email
↓
TF-IDF Vectorization
↓
Logistic Regression
↓
Intent Prediction
↓
Entity Extraction
↓
Streamlit Dashboard

## Sample Input

Book a flight for John from Hyderabad to Delhi tomorrow.

## Sample Output

Intent: Book Flight

Confidence: 86.11%

Extracted Details:

* Name: John
* Source: Hyderabad
* Destination: Delhi
* Travel Date: tomorrow

## Repository Structure

* app.py
* requirements.txt
* intent_model.pkl
* tfidf.pkl
* airline_emails.csv

## Deployment

Deployed using Streamlit Community Cloud.
