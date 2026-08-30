# IPO Listing Price Prediction

A Machine Learning project to predict the expected **IPO Listing Price** using information available before an IPO is listed.

## Project Overview

This project uses historical Indian IPO data to train, tune, compare, and select regression models for IPO listing-price prediction.

### Target Variable

- `List Price` — actual IPO listing price.

### Features Used

- `Issue_Size(crores)`
- `QIB`
- `HNI`
- `RII`
- `Total`
- `Offer Price`

## Data Leakage Prevention

The following post-listing columns are excluded:

- `Listing Gain`
- `CMP(BSE)`
- `CMP(NSE)`
- `Current Gains`

`IPO_Name` and `Date` are also excluded from model training.

This makes the prediction setup suitable for **pre-listing prediction**.

## Models Compared

1. Linear Regression
2. Decision Tree Regressor
3. Tuned Decision Tree
4. Random Forest Regressor
5. Tuned Random Forest
6. XGBoost Regressor
7. Tuned XGBoost

Hyperparameter tuning was performed using `RandomizedSearchCV`.

## Model Comparison

| Model | MAE | MSE | RMSE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | 65.302 | 10279.153 | 101.386 | 0.942823 |
| Decision Tree | 64.812 | 10380.544 | 101.885 | 0.942259 |
| Tuned Decision Tree | 68.454 | 12745.104 | 112.894 | 0.929107 |
| **Random Forest** | **54.920** | **8180.181** | **90.444** | **0.954499** |
| Tuned Random Forest | 54.898 | 8418.775 | 91.754 | 0.953172 |
| XGBoost | 55.066 | 9310.971 | 96.493 | 0.948209 |
| Tuned XGBoost | 58.975 | 9931.253 | 99.656 | 0.944759 |

## Best Model

**Random Forest Regressor** was selected as the final model.

- MAE: **54.92**
- MSE: **8180.18**
- RMSE: **90.44**
- R²: **0.9545**

The final fitted model is saved as:

```text
models/random_forest_final.pkl