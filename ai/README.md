# AI Crop Recommendation Module

This module provides machine learning-based crop recommendations for the Primary Key Smart Agriculture system.

## Technology

- Python 3.14.6
- Pandas 3.0.5
- Scikit-learn 1.9.0
- Decision Tree Classifier
- Flask

## Input Parameters

The model accepts:

- Soil Type
- Soil pH
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)

## Prediction

The Decision Tree model processes the agricultural parameters and predicts a suitable crop.

### Example

Input:

```text
Soil Type: Loamy
pH: 6.5
Nitrogen: 90
Phosphorus: 45
Potassium: 40