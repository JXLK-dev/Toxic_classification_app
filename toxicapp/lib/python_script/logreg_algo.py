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
def logpred():
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


if __name__ == "__main__":
    app.run(debug=True)