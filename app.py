from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define iris species labels
iris_species = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@app.route('/')
def home():
    return render_template('IRIS.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form data
    data = [float(x) for x in request.form.values()]
    features = [np.array(data)]
    
    # Make a prediction using the trained model
    prediction = model.predict(features)
    
    # Return the predicted species
    return jsonify({'prediction': iris_species[prediction[0]]})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
 
