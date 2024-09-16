from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
'''Initializes a new Flask application. 
__name__ is passed to Flask to help it locate resources.'''

# Load the trained model
with open('best_sales_model.pkl', 'rb') as file:
    model = pickle.load(file)
'''pickle.load(file): Loads the trained model from a file named best_sales_model.pkl.
The model is deserialized and ready for making predictions.'''

'''Defines a route for the root URL ('/')
It accepts both GET and POST requests'''
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        # Get input values from the form
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])

        input_data = pd.DataFrame({
            'TV': [tv],
            'Radio': [radio],
            'Newspaper': [newspaper]
        })

        # Prepare features for prediction
        # features = np.array([[tv, radio, newspaper]])
        prediction = model.predict(input_data)[0]

        return render_template('result.html', prediction=prediction)
    return render_template('index.html',prediction=None)

'''When the user submits the form:
request.form: Retrieves form data sent with the POST request.
The tv, radio, and newspaper values are fetched and converted to floats.
model.predict(input_data)[0]: Uses the loaded model to make predictions based on the input data.
The [0] extracts the first prediction result from the array returned by predict.
render_template('result.html', prediction=prediction): Renders the result.html template and passes the prediction value to it for display'''

if __name__ == '__main__':
    app.run(debug=True)
