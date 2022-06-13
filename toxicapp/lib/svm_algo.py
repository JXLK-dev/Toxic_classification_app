from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
import numpy as np

app = Flask(__name__)

with open(r"toxic_vect.pkl", "rb") as f:
    toxic = pickle.load(f)

with open(r"severe_toxic_vect.pkl", "rb") as f:
    severe = pickle.load(f)

with open(r"obscene_vect.pkl", "rb") as f:
    obscene = pickle.load(f)

with open(r"insult_vect.pkl", "rb") as f:
    insult = pickle.load(f)

with open(r"threat_vect.pkl", "rb") as f:
    threat = pickle.load(f)

with open(r"identity_hate_vect.pkl", "rb") as f:
    identityHate = pickle.load(f)

# Load the pickled models
with open(r"toxic_model.pkl", "rb") as f:
    toxicSVM = pickle.load(f)

with open(r"severe_toxic_model.pkl", "rb") as f:
    severeSVM = pickle.load(f)

with open(r"obscene_model.pkl", "rb") as f:
    obsceneSVM = pickle.load(f)

with open(r"insult_model.pkl", "rb") as f:
    insultSVM = pickle.load(f)

with open(r"threat_model.pkl", "rb") as f:
    threatSVM = pickle.load(f)

with open(r"identity_hate_model.pkl", "rb") as f:
    idenHateSVM = pickle.load(f)


@app.route('/api', methods=['GET'])
def logpred():
    # Take a string input from user
    user_input = request.form['Query']
    data = [user_input]

    vector = toxic.transform(data)
    toxicPred = toxicSVM.predict_proba(vector)[:, 1]

    vector = severe.transform(data)
    severePred = severeSVM.predict_proba(vector)[:, 1]

    vector = obscene.transform(data)
    obscenePred = obsceneSVM.predict_proba(vector)[:, 1]

    vector = threat.transform(data)
    threatPred = threatSVM.predict_proba(vector)[:, 1]

    vector = insult.transform(data)
    insultPred = insultSVM.predict_proba(vector)[:, 1]

    vector = identityHate.transform(data)
    idenHatePred = idenHateSVM.predict_proba(vector)[:, 1]
