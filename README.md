# 📦 Trade Partner Recommendation System

A machine learning-based system to predict the top 5 countries for importing or exporting a specific product. The system uses historical trade data and machine learning models to recommend trade partners based on user inputs.

## ✨ Features

- **Import/Export Prediction**: Predict the best countries for import/export based on product and country selection.
- **Machine Learning Models**: Built using `RandomForestClassifier` to predict trade partners.
- **Interactive UI**: A simple widget interface to select a country, product, and trade type (import/export) to receive recommendations.
- **Feature Importance Visualization**: Displays the importance of trade-related features in the model.

---

## 📁 Files

| File                      | Description                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------|
| `train_export_model.py`    | Script to train the RandomForest model for predicting the best export countries.                  |
| `train_import_model.py`    | Script to train the RandomForest model for predicting the best import countries.                  |
| `train_product_encoder.py` | Script to encode product categories (`L3Desc`) and save the encoder.                             |
| `interactive_ui.py`        | Interactive UI that lets users select inputs and get top 5 countries for export/import prediction.|

---

## ⚙️ Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/trade-partner-recommendation.git
    ```

2. **Install dependencies**:

    Make sure you have Python 3.7+ installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

### 🏋️‍♂️ Training Models

To train the models using historical trade data, run the respective scripts:

```bash
  python train_export_model.py
  python train_import_model.py

```
### 🖥️ Interactive Interface
To launch the interactive interface, run the following:

```bash
python interactive_ui.py

This will display a widget where you can select a country, product, and trade type (import/export), and get the top 5 trade partner recommendations based on the machine learning model's predictions.

```
### 🔍 Model Training

The RandomForestClassifier models are trained using a dataset containing both numerical and categorical trade-related features, such as:

  - Numerical Features: Reporter_Total_Imports, Reporter_Total_Exports, Partner_Total_Imports, Partner_Total_Exports
  - Categorical Features: Encoded product (L3Desc) and country names (ReporterName, PartnerName)
  These features are used to predict the best partner countries for trade based on the selected inputs.

### 🔧 Feature Importance

The train_export_model.py and train_import_model.py scripts visualize the feature importance of the trained models, allowing you to understand which features have the most influence on the model’s predictions.

python Copy code
      importances = reporter_model.feature_importances_
      plt.barh(feature_names, importances)
      plt.title('Feature Importance')
      plt.show()


