import pandas as pd

# Load raw data (ensure 'data/raw/ecommerce_data.csv' exists)
df = pd.read_csv("data/raw/ecommerce_data.csv")

# Data cleaning: forward fill missing values
df.fillna(method='ffill', inplace=True)

# One-hot encoding for categorical features (example: product_category, brand)
df_encoded = pd.get_dummies(df, columns=["product_category", "brand"])

# Save processed data locally and optionally upload to S3
df_encoded.to_csv("data_preprocessing/processed_data.csv", index=False)
print("Data preprocessing complete. Processed data saved to 'data_preprocessing/processed_data.csv'.")
