# Real_time-data_Sales_prediction
Developing a real-time data analytics dashboard using Streamlit and a pre-trained machine learning model. The dashboard should simulate real-time data, make predictions using a trained regression  and interactively display the data and predictions.

## Features

- **Simulated Sales Data**: Randomly generated sales data for various grocery products.
- **Regression Model**: A linear regression model that predicts total sales based on the number of units sold and the price per unit.
- **Real-Time Dashboard**: Continuously updates with new sales data and predictions, displayed using Streamlit.
- **Visualization**: Graphs showing predicted sales trends over time.

## Requirements

To run this project, you need Python and the following dependencies:

- `streamlit`: For building the interactive dashboard.
- `pandas`: For data manipulation.
- `matplotlib`: For visualizing data.
- `joblib`: For saving and loading the trained machine learning model.
- `scikit-learn`: For training the regression model.

## Machine Learning Model

The **regression model** used in this project is a **linear regression model** that predicts the total sales based on the following features:

- **Units Sold**: The number of units of a product sold.
- **Price per Unit**: The price of each unit sold.

The model is trained using the **scikit-learn** library and saved using **joblib** for later use. The model predicts **Total Sales** based on the input features: `Units Sold` and `Price per Unit`.

### Model Training

The model is trained on a simulated dataset of sales data where the target variable is **Total Sales**. The features used to train the model are:

- **Units Sold**
- **Price per Unit**

The training process involves fitting the model to the data and then using it to predict **Total Sales**. Once trained, the model is saved using **joblib** to allow for real-time predictions in the Streamlit dashboard.

## Model Evaluation

The performance of the model is evaluated using the following metrics:

- **Mean Squared Error (MSE)**: This metric measures the average squared difference between the actual values and the predicted values. A lower MSE indicates better performance, as it means the predictions are closer to the actual values.
  
  **Formula**:  
  \[
  MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
  \]
  Where:
  - \( y_i \) is the actual value,
  - \( \hat{y}_i \) is the predicted value,
  - \( n \) is the number of data points.

- **R² Score (Coefficient of Determination)**: This metric indicates how well the model fits the data. The R² score ranges from 0 to 1, with higher values indicating a better fit. An R² score of 1 means the model perfectly predicts the total sales.

  **Formula**:  
  \[
  R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
  \]
  Where:
  - \( y_i \) is the actual value,
  - \( \hat{y}_i \) is the predicted value,
  - \( \bar{y} \) is the mean of the actual values.

### Model Performance

After training the model, the following evaluation metrics were calculated:
- **Mean Squared Error (MSE)**: [Insert the value after testing the model]
- **R² Score**: [Insert the R² score after testing the model]

A good R² score and a low MSE indicate that the model is performing well in predicting total sales.

## Saving the Model

The trained model is saved as `regression_model.pkl` using **joblib**. This saved model is then loaded in the Streamlit app to make real-time predictions on new, simulated sales data.

