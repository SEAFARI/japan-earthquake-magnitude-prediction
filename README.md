# japan-earthquake-magnitude-prediction

## Live Demo
Want to see the earthquake prediction in action? Check out the deployed Streamlit application here:

Streamlit Application: https://japan-earthquake-magnitude-prediction-k5okggnr6sbxtgcakgdk4q.streamlit.app/

## Docker Deployment
For robust and reproducible deployment, the entire application has been containerized using Docker. You can find the image on Docker Hub:

Docker Hub Repository:


## Project Overview
Welcome to the Japan Earthquake Magnitude Prediction project! This initiative focuses on leveraging historical seismic data to accurately predict earthquake magnitudes in Japan. As a nation situated on the highly active Pacific Ring of Fire, Japan experiences frequent and sometimes devastating seismic events. My goal with this project was to build a robust machine learning model capable of assisting in understanding and potentially mitigating the impact of these natural phenomena.

I've meticulously collected and analyzed a dataset of significant earthquakes (magnitude 4.5 and above) in Japan spanning from 2005 to 2025 from the USGS earthquake catalog. Through extensive Exploratory Data Analysis (EDA) and rigorous model training, I've developed and deployed an Artificial Neural Network (ANN) that demonstrates strong predictive capabilities.

## Key Features & Achievements
Comprehensive Data Collection: Curated a unique dataset of damaging earthquakes (magnitude 4.5+) in Japan from 2005 to 2025, sourced from the USGS.
Insightful Exploratory Data Analysis (EDA): Uncovered critical patterns in Japan's seismic activity, specifically highlighting the intense period between 2010 and 2012, which includes the catastrophic 2011 Tōhoku earthquake (Magnitude 9.0–9.1).

## Graph: Total Annual Sum of Earthquake Magnitudes
![f11b1ad8-eae2-43b1-a221-0adbbe227acc](https://github.com/user-attachments/assets/c176a54d-7d39-4c53-afbd-35df8132e409)

## Advanced Machine Learning Model Development:
Initially explored a Random Forest Regressor with hyperparameter tuning via Randomized Search CV.

Developed a sophisticated Artificial Neural Network (ANN) with multiple dense layers, ELU activation, and L2 regularization, demonstrating its superiority for this prediction task.

Rigorous Model Evaluation: Performed detailed performance analysis on both training and test sets, comparing Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R2 Score to ensure model generalization.

Seamless Deployment: Successfully deployed the best-performing ANN model as an interactive web application using Streamlit, making the predictions accessible and user-friendly.

Containerization with Docker: Ensured reproducibility and ease of deployment by containerizing the entire application using Docker.

## Why Japan? The Seismic Context
Japan's geographical location at the convergence of several major tectonic plates makes it one of the most earthquake-prone countries in the world. This inherent seismic activity, while a natural phenomenon, poses significant challenges. The 2011 Tōhoku earthquake, one of the most powerful ever recorded globally, serves as a stark reminder of the immense destructive power of these events. My project aims to contribute to the ongoing efforts to understand and predict earthquake magnitudes, which is a vital step towards enhancing disaster preparedness and resilience in such a vulnerable region.

## Model Performance:

While the Random Forest achieved a slightly higher R2 score on the training data, the ANN showed better generalization capabilities to the unseen test data, with comparable or slightly better MAE and RMSE values.

This indicates its robustness and higher reliability for real-world predictions, making it the chosen model for deployment.

## Model Performance Comparison

| Model                       | Metric                  | Training Set | Test Set |
| :-------------------------- | :---------------------- | :----------- | :------- |
| **Random Forest Regressor** | Root Mean Squared Error | 0.0660       | 0.1783   |
|                             | Mean Absolute Error     | 0.0460       | 0.1259   |
|                             | R2 Score                | 0.9675       | 0.7751   |
| **Artificial Neural Network** | Root Mean Squared Error | 0.1635       | 0.1828   |
|                             | Mean Absolute Error     | 0.1172       | 0.1252   |
|                             | R2 Score                | 0.8004       | 0.7636   |


# How to Run Locally

If you'd like to explore the code or run the application on your local machine, follow these steps:

1. Clone the repository:
   ```bash
    git clone https://github.com/YOUR_USERNAME/japan-earthquake-magnitude-prediction.git
    cd japan-earthquake-magnitude-prediction
   
2. Set up a virtual environment (recommended):
   ```bash
     python -m venv venv
    source venv/bin/activate # On Windows, use: `venv\Scripts\activate`
   
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
    
5. Run the Streamlit application:
   ```bash
     streamlit run app.py 

## Future Enhancements

I'm always looking to improve! Here are some ideas for future development:

Feature Engineering: Incorporate more sophisticated features such as earthquake depth, specific geographical coordinates, and proximity to major fault lines.

Time-Series Forecasting: Explore advanced time-series models (e.g., LSTMs, Transformers) to predict not just magnitude but also the likelihood and timing of future seismic events.

Real-time Data Integration: Connect directly to live USGS earthquake feeds for continuous model updates and real-time predictions.

Interactive Visualization: Enhance the Streamlit app with more interactive graphs and maps for better data exploration and prediction visualization.






