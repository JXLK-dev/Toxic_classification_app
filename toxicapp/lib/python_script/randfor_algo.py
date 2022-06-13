from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle

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
    toxicRDF = pickle.load(f)

with open(r"severe_toxic_model.pkl", "rb") as f:
    severeRDF = pickle.load(f)

with open(r"obscene_model.pkl", "rb") as f:
    obsceneRDF = pickle.load(f)

with open(r"insult_model.pkl", "rb") as f:
    insultRDF = pickle.load(f)

with open(r"threat_model.pkl", "rb") as f:
    threatRDF = pickle.load(f)

with open(r"identity_hate_model.pkl", "rb") as f:
    idenHateRDF = pickle.load(f)


@app.route('/randomforest', methods=['GET'])
def logpred():
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


if __name__ == "__main__":
    app.run(debug=True)
