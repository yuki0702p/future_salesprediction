# Sales Prediction Model with Flask

## Overview

This project focuses on building a **Sales Prediction Model** using machine learning techniques. The aim is to predict the sales of a product based on its advertising budget across three channels: **TV**, **Radio**, and **Newspaper**. The model is trained on an advertising dataset and deployed using a **Flask web application** for real-time sales predictions.

## Objective

Predicting future sales based on advertising expenditure helps businesses optimize their marketing strategies and budget allocations. By using historical data and applying machine learning models, this project provides a mechanism for accurate predictions, which can inform advertising decisions.

## Project Structure

The project is divided into the following key steps:

1. **Data Cleaning and Preprocessing**:
   - Dataset in used contain Advertising fees spend on TV , RADIO and NEWSPAPER. This code examines who has more dependency on sales production.
   - Performed summary statistics, handled missing values, and removed outliers using **IQR** filtering to clean the dataset.
   - Visualized relationships between features using scatter plots and pair plots.

2. **Model Building**:
   - Three regression models were used:
     - **Linear Regression**
     - **Decision Tree Regressor**
     - **Random Forest Regressor**
   - The models were evaluated using **R2 Score** and **RMSE** to assess performance.

3. **Hyperparameter Tuning**:
   - Used **GridSearchCV** to fine-tune the **Random Forest Regressor** model by optimizing parameters such as the number of estimators, max depth, and minimum samples split.

4. **Model Saving**:
   - The best-performing model (Random Forest) was saved as a **pickle file** (`best_sales_model.pkl`) to be used in the web application.

5. **Flask Web Application**:
   - A simple Flask web app was created to allow users to input the advertising budget and predict future sales based on the trained model.
   - The user inputs values for **TV**, **Radio**, and **Newspaper** advertising, and the app returns the predicted sales.
   
6. **Deployment**:
   - The Flask application is ready to be hosted on a local server or deployed to platforms like **Heroku** for production use.

## How to Use

### 1. Requirements

Ensure you have the following installed:
- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- pickle

Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

### 2. Running the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sales-prediction-flask.git
   ```

2. **Prepare the Data**:
   - Make sure the `advertising.csv` file is in the root directory.

3. **Train the Model** (Optional):
   - If you want to retrain the model, run the `model_training.py` script to clean the data, train the models, perform hyperparameter tuning, and save the model.

4. **Start the Flask Application**:
   - Navigate to the project directory and run the Flask app:
   ```bash
   python web_application.py
   ```

5. **Use the Web App**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.
   - Enter the advertising budget for **TV**, **Radio**, and **Newspaper**.
   - Submit the form to get the predicted sales result.

### 3. Model Prediction

Once the Flask app is running:
- The model will take inputs from the form (TV, Radio, Newspaper advertising budgets).
- It will use the **Random Forest** model (trained and stored in `best_sales_model.pkl`) to predict sales and display the result on a new page.

### 4. Folder Structure

```
- app.py (Flask app)
- advertising.csv (Dataset)
- best_sales_model.pkl (Saved model)
- templates/
  - index.html (Input form)
  - result.html (Prediction result)
- static/
  - styles.css (CSS for styling)
- requirements.txt (List of required packages)
```

## Summary of Process

1. **Data Cleaning**: The dataset was cleaned by removing outliers and handling missing data.
2. **Model Training**: Three models were trained and evaluated based on performance metrics like **R2 Score** and **RMSE**.
3. **Hyperparameter Tuning**: The best parameters for the **Random Forest Regressor** were found using **GridSearchCV**.
4. **Model Deployment**: The model was saved as a pickle file and used in a Flask web application to provide real-time sales predictions based on user input.
5. **User Interface**: The user can enter advertising budgets into a simple, styled HTML form, and the app will return a sales prediction based on the input values.

## Future Enhancements

- Deploy the Flask app on a cloud platform such as **Heroku**.
- Add more advanced machine learning models and compare their performance.
- Expand the dataset with additional features to improve prediction accuracy.

## License
This project is licensed under the MIT License -You are free to use, modify, and distribute the software as long as you include the original license.
