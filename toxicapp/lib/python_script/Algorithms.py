import os
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

app = Flask(__name__)

os.chdir(r"C:\Users\minem\OneDrive\Desktop\Machine learning Toxic classification\Toxic_classification_app\toxicapp\lib\python_script")


# RandomForest Algorithm
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
with open(r"r_toxic_model.pkl", "rb") as f:
    toxicRDF = pickle.load(f)

with open(r"r_severe_toxic_model.pkl", "rb") as f:
    severeRDF = pickle.load(f)

with open(r"r_obscene_model.pkl", "rb") as f:
    obsceneRDF = pickle.load(f)

with open(r"r_insult_model.pkl", "rb") as f:
    insultRDF = pickle.load(f)

with open(r"r_threat_model.pkl", "rb") as f:
    threatRDF = pickle.load(f)

with open(r"r_identity_hate_model.pkl", "rb") as f:
    idenHateRDF = pickle.load(f)


@app.route('/')
def debugpurpose():
    return 'Hello World'


@app.route('/randomforest', methods=['GET'])
def randomForest():
    # Take a string input from user
    user_input = request.args['Query']
    data = [user_input]

    vector = toxic.transform(data)
    toxicPred = toxicRDF.predict_proba(vector)[:, 1]

    vector = severe.transform(data)
    severePred = severeRDF.predict_proba(vector)[:, 1]

    vector = obscene.transform(data)
    obscenePred = obsceneRDF.predict_proba(vector)[:, 1]

    vector = threat.transform(data)
    threatPred = threatRDF.predict_proba(vector)[:, 1]

    vector = insult.transform(data)
    insultPred = insultRDF.predict_proba(vector)[:, 1]

    vector = identityHate.transform(data)
    idenHatePred = idenHateRDF.predict_proba(vector)[:, 1]

    outToxic = round(toxicPred[0], 2)
    outSevere = round(severePred[0], 2)
    outObscene = round(obscenePred[0], 2)
    outInsult = round(insultPred[0], 2)
    outThreat = round(threatPred[0], 2)
    outIdenHate = round(idenHatePred[0], 2)

    return jsonify({
        'Toxic': 'Toxic : {}'.format(outToxic),
        'Severe': 'Severe: {}'.format(outSevere),
        'Obscene': 'Obscene {}'.format(outObscene),
        'Insult': 'Insult {}'.format(outInsult),
        'Threat': 'Threat {}'.format(outThreat),
        'IdenHate': 'IdenHate {}'.format(outIdenHate),
    })


# Logistic Algorithm
with open(r"l_toxic_model.pkl", "rb") as f:
    toxicLR = pickle.load(f)

with open(r"l_severe_toxic_model.pkl", "rb") as f:
    severeLR = pickle.load(f)

with open(r"l_obscene_model.pkl", "rb") as f:
    obsceneLR = pickle.load(f)

with open(r"l_insult_model.pkl", "rb") as f:
    insultLR = pickle.load(f)

with open(r"l_threat_model.pkl", "rb") as f:
    threatLR = pickle.load(f)

with open(r"l_identity_hate_model.pkl", "rb") as f:
    idenHateLR = pickle.load(f)


@app.route('/logreg', methods=['GET'])
def logisticRegression():
    # Take a string input from user
    user_input = request.args['Query']
    data = [user_input]

    vector = toxic.transform(data)
    toxicPred = toxicLR.predict_proba(vector)[:, 1]

    vector = severe.transform(data)
    severePred = severeLR.predict_proba(vector)[:, 1]

    vector = obscene.transform(data)
    obscenePred = obsceneLR.predict_proba(vector)[:, 1]

    vector = threat.transform(data)
    threatPred = threatLR.predict_proba(vector)[:, 1]

    vector = insult.transform(data)
    insultPred = insultLR.predict_proba(vector)[:, 1]

    vector = identityHate.transform(data)
    idenHatePred = idenHateLR.predict_proba(vector)[:, 1]

    outToxic = round(toxicPred[0], 2)
    outSevere = round(severePred[0], 2)
    outObscene = round(obscenePred[0], 2)
    outInsult = round(insultPred[0], 2)
    outThreat = round(threatPred[0], 2)
    outIdenHate = round(idenHatePred[0], 2)

    return jsonify({
        'Toxic': 'Toxic : {}'.format(outToxic),
        'Severe': 'Severe: {}'.format(outSevere),
        'Obscene': 'Obscene {}'.format(outObscene),
        'Insult': 'Insult {}'.format(outInsult),
        'Threat': 'Threat {}'.format(outThreat),
        'IdenHate': 'IdenHate {}'.format(outIdenHate),
    })

# KNN algorithm from SVM as it doesn't have predict_proba


with open(r"k_toxic_model.pkl", "rb") as f:
    toxicSVM = pickle.load(f)

with open(r"k_severe_toxic_model.pkl", "rb") as f:
    severeSVM = pickle.load(f)

with open(r"k_obscene_model.pkl", "rb") as f:
    obsceneSVM = pickle.load(f)

with open(r"k_insult_model.pkl", "rb") as f:
    insultSVM = pickle.load(f)

with open(r"k_threat_model.pkl", "rb") as f:
    threatSVM = pickle.load(f)

with open(r"k_identity_hate_model.pkl", "rb") as f:
    idenHateSVM = pickle.load(f)


@app.route('/knn', methods=['GET'])
def kNearestNeighbour():
    # Take a string input from user
    user_input = request.args['Query']
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

    outToxic = round(toxicPred[0], 2)
    outSevere = round(severePred[0], 2)
    outObscene = round(obscenePred[0], 2)
    outInsult = round(insultPred[0], 2)
    outThreat = round(threatPred[0], 2)
    outIdenHate = round(idenHatePred[0], 2)

    return jsonify({
        'Toxic': 'Toxic : {}'.format(outToxic),
        'Severe': 'Severe: {}'.format(outSevere),
        'Obscene': 'Obscene {}'.format(outObscene),
        'Insult': 'Insult {}'.format(outInsult),
        'Threat': 'Threat {}'.format(outThreat),
        'IdenHate': 'IdenHate {}'.format(outIdenHate),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
