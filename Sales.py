import streamlit as st
import pandas as pd
import random
import joblib
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained regression model
model = joblib.load("C:\\Users\\reddy\\Downloads\\regression_model.pkl")

# Define product details
products = {
    "Rice": (20, 50),  # Price range (min, max)
    "Bread": (15, 30),
    "Milk": (10, 25),
    "Eggs": (5, 12),
    "Fruits": (10, 50),
    "Vegetables": (5, 40)
}

# Function to generate sales data
def generate_sales_record():
    product = random.choice(list(products.keys()))
    price = random.uniform(*products[product])  # Random price within range
    units_sold = random.randint(1, 100)  # Random units sold
    total_sales = price * units_sold
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
    return {
        "Product": product,
        "Price per Unit": round(price, 2),
        "Units Sold": units_sold,
        "Total Sales": round(total_sales, 2),
        "Timestamp": timestamp
    }

# Simulate real-time data generation
def simulate_data(num_records=10):
    data = [generate_sales_record() for _ in range(num_records)]
    return pd.DataFrame(data)

# Streamlit UI elements
st.title("Real-Time Sales Prediction Dashboard")

# Simulation parameter inputs
num_records = st.slider("Number of records to generate", min_value=1, max_value=50, value=10)
update_interval = st.selectbox(
    "Data generation interval (seconds)",
    options=[0, 15, 30, 45, 60],  # Predefined intervals
    index=0  # Default to 0 seconds
)

# Dropdown to choose the type of graph
graph_type = st.selectbox("Select Graph Type", [ "Bar Chart", "Scatter Plot", "Boxplot", "Distplot", "Heatmap"])

# Placeholder for simulated sales data
sales_data_placeholder = st.empty()
prediction_placeholder = st.empty()
chart_placeholder = st.empty()

# Simulate new data at specified intervals
if st.button("Start Simulation"):
    while True:
        # Generate new sales data
        new_data = simulate_data(num_records)
        
        # Predict total sales using the regression model
        X_new = new_data[["Units Sold", "Price per Unit"]]
        new_predictions = model.predict(X_new)
        new_data["Predicted Total Sales"] = new_predictions
        
        # Update sales data in the Streamlit app
        sales_data_placeholder.write(new_data)
        
        # Update predictions table
        prediction_placeholder.write(new_data[["Product", "Units Sold", "Price per Unit", "Predicted Total Sales", "Timestamp"]])
        
        # Visualization based on selected graph type
        fig, ax = plt.subplots()

        if graph_type == "Bar Chart":
            ax.bar(new_data["Product"], new_data["Predicted Total Sales"], color="green")
            ax.set_xlabel("Product")
            ax.set_ylabel("Predicted Total Sales")
            ax.set_title("Predicted Total Sales by Product")

        elif graph_type == "Scatter Plot":
            ax.scatter(new_data["Units Sold"], new_data["Predicted Total Sales"], color="red")
            ax.set_xlabel("Units Sold")
            ax.set_ylabel("Predicted Total Sales")
            ax.set_title("Predicted Total Sales vs Units Sold")

        elif graph_type == "Boxplot":
            sns.boxplot(data=new_data, x="Product", y="Predicted Total Sales", ax=ax)
            ax.set_title("Boxplot of Predicted Total Sales by Product")

        elif graph_type == "Distplot":
            sns.histplot(new_data["Predicted Total Sales"], kde=True, ax=ax, color="purple")
            ax.set_title("Distribution of Predicted Total Sales")

        elif graph_type == "Heatmap":
            corr_matrix = new_data[["Units Sold", "Price per Unit", "Predicted Total Sales"]].corr()
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Correlation Heatmap")

        st.pyplot(fig)
        
        # Wait for the defined update interval before generating new data
        time.sleep(update_interval)
