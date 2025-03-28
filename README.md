# Model Deployment Using Flask for Iris Classification
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja, and has become one of the most popular Python web application frameworks.

This repository demonstrates how to deploy a machine learning model using Flask for classifying Iris flower species. The deployed model predicts the species (setosa, versicolor, or virginica) based on input features such as sepal length, sepal width, petal length, and petal width.

# Files:
### model.pkl:
Pickled machine learning model trained on the Iris dataset.

### app.py:
Python script containing Flask web application code for model deployment.

#### import Libraries:
```python
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
```

#### load the trained model:
```python
model = pickle.load(open('model.pkl', 'rb'))
iris_species = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
```

#### initialize Flask application:
```python
app = Flask(__name__)
```

#### define routes:
```python
@app.route('/')
def home():
    return render_template('IRIS.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = [np.array(data)]
    
    prediction = model.predict(features)
    predicted_species = iris_species[prediction[0]]
    
    return jsonify({'prediction': predicted_species})
```

#### run the application:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Templates:
HTML file for the web interface where users can input feature values and get predictions.
### IRIS.html:
```html
<html>
<head>
	<title>ML Model Prediction</title>
</head>
<body bgcolor='red'>
<h1>ML Model Prediction</h1>
<form action="/predict" method="post">
<label for="sepal_length">Sepal Length:</label>
<input type="text" id="sepal_length" name="sepal_length"><br><br>
<label for="sepal_width">Sepal Width:</label>
<input type="text" id="sepal_width" name="sepal_width"><br><br>
<label for="petal_length">Petal Length:</label>
<input type="text" id="petal_length" name="petal_length"><br><br>
<label for="petal_width">Petal Width:</label>
<input type="text" id="petal_width" name="petal_width"><br><br>
<input type="submit" value="Predict">
<!-- <button type="submit">Predict</button> -->
</form>
</body>
</html>
```
# Requirements:
- [Python](https://github.com/python)

- [HTML](https://github.com/html)

- [Jupyter](https://github.com/jupyter)

- [Flask](https://github.com/flask)

- [scikit-learn](https://github.com/scikit-learn)

- [numpy](https://github.com/numpy)

## License

Flask is completely free and open-source and licensed under the [BSD-3-Clause](https://flask.palletsprojects.com/en/2.3.x/license/) license.
