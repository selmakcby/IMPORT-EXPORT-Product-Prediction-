Trade Partner Recommendation System

This repository contains a machine learning-based system designed to predict the best trade partners for importing or exporting a specific product. The system leverages historical trade data and machine learning models to recommend the top 5 countries for either importing or exporting a product based on user inputs.

Features

Import/Export Prediction: Predict the best countries for import or export based on product and country selection.
Machine Learning Models: Trained using RandomForestClassifier to predict the most likely trade partners.
Interactive UI: Users can select a country, product, and trade type (import/export) through a simple widget interface.
Feature Importance: Visualizes the importance of different trade-related features in the model.
Files

train_export_model.py: Script to train the RandomForest model for predicting the best export countries.
train_import_model.py: Script to train the RandomForest model for predicting the best import countries.
train_product_encoder.py: Script to encode product categories (L3Desc) and save the encoder.
interactive_ui.py: Script that provides an interactive interface to predict the top 5 countries for import/export based on user inputs using pre-trained models.
Requirements

Python 3.7+
scikit-learn
pandas
ipywidgets
joblib
matplotlib
Install the dependencies via pip:

bash
Copy code
pip install -r requirements.txt
Usage

Training Models
To train the models using historical trade data, run the respective training scripts:

bash
Copy code
python train_export_model.py
python train_import_model.py
Interactive UI
Run the interactive interface to select a product, country, and trade type to get recommendations:

bash
Copy code
python interactive_ui.py
This will display a widget where you can select a country and a product and get the top 5 trade partner recommendations based on the machine learning model's predictions.

Model Training

The RandomForest models are trained using a dataset with numerical and categorical trade-related features, such as:

Reporter_Total_Imports, Reporter_Total_Exports
Partner_Total_Imports, Partner_Total_Exports
Encoded product (L3Desc) and country names
These features are used to predict the best partner countries for trading a specific product.

Feature Importance

The train_export_model.py script also visualizes the feature importance of the trained RandomForest model, allowing you to see which features have the most impact on the model's decisions.
