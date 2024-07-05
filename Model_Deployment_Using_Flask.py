{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ed750805-626e-4e0b-a759-684e5fb11b0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,request,jsonify,render_template\n",
    "import pickle \n",
    "\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d6dc8e2a-114c-45ad-8685-889e32bb7261",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c7e8d6a7-1d67-4268-9181-2864946b8e04",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=pickle.load(open('model.pkl','rb'))\n",
    "iris_species={0:'setosa',1:'versicolor',2:'virginica'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b0b9ee6c-cd19-4d9a-a09d-e8c98c8d14ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('IRIS.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "edd70453-b48b-4609-81fc-fc54bf310f7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    data=[float(x) for x in request.form.values()]\n",
    "    features=[np.array(data)]\n",
    "\n",
    "    prediction=model.predict(features)\n",
    "    return jsonify({'prediction':iris_species[(prediction[0])]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afdffc1e-77cb-461b-b17c-25792eff8771",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [05/Jul/2024 20:29:07] \"GET / HTTP/1.1\" 200 -\n",
      "C:\\Users\\RAHUL\\Downloads\\Anaconda\\Lib\\site-packages\\sklearn\\base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [05/Jul/2024 20:29:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__':\n",
    "    app.run(debug=True,use_reloader=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
