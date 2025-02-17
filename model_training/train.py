import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Load processed data
data = pd.read_csv("data_preprocessing/processed_data.csv")

# For demonstration, assume first column is the target; adjust accordingly
y = data.iloc[:, 0]
X = data.iloc[:, 1:]

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert datasets into DMatrix format
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

# Hyperparameters for XGBoost
params = {
    'max_depth': 5,
    'eta': 0.2,
    'objective': 'binary:logistic',
    'eval_metric': 'logloss'
}
num_rounds = 100

# Train the model
model = xgb.train(params, dtrain, num_rounds, [(dval, 'eval')])

# Save the model to file
model.save_model("model_training/model.bin")

# Evaluate the model
preds = model.predict(dval)
rmse = np.sqrt(mean_squared_error(y_val, preds))
print("Validation RMSE:", rmse)
