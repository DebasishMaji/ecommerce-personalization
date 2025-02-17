# E-commerce Personalization Pipeline

An end-to-end machine learning pipeline for delivering personalized product recommendations using AWS services.

## Overview

This project implements:
- Data ingestion from an AWS S3 bucket
- Data preprocessing & feature engineering tailored for user behavior and product attributes
- Model training using a recommendation algorithm (here using XGBoost as an example)
- Deployment of the trained model on Amazon SageMaker
- Exposing the model via RESTful APIs using AWS API Gateway and Lambda for real-time recommendations
- Visualization of EDA and model performance

## Project Structure

\`\`\`
ecommerce-personalization/
├── data_ingestion/
│   └── s3_upload.sh
├── data_preprocessing/
│   ├── preprocess.py
│   └── visualization.ipynb
├── model_training/
│   ├── train.py
│   └── evaluate.py
├── deployment/
│   ├── deploy.py
│   └── inference.py
├── lambda_function/
│   └── lambda_handler.py
├── api_gateway/
│   └── api_definition.yaml
├── requirements.txt
├── README.md
└── .env
\`\`\`

## Setup and Usage

1. Clone the repository and install dependencies:
   \`\`\`
   git clone https://github.com/DebasishMaji/ecommerce-personalization.git
   cd ecommerce-personalization
   pip install -r requirements.txt
   \`\`\`
2. Update AWS credentials in the .env file.
3. Upload your raw data using:
   \`\`\`
   bash data_ingestion/s3_upload.sh
   \`\`\`
4. Run data preprocessing:
   \`\`\`
   python data_preprocessing/preprocess.py
   \`\`\`
5. Train the model:
   \`\`\`
   python model_training/train.py
   \`\`\`
6. Deploy the model:
   \`\`\`
   python deployment/deploy.py
   \`\`\`
7. Set the \`ENDPOINT_NAME\` environment variable in Lambda.
8. Deploy the API using the provided API definition.

## Visualization

Open \`data_preprocessing/visualization.ipynb\` in JupyterLab to view EDA plots and visualizations.

## License

This project is licensed under the MIT License.

## Contact

**Debasish Maji**  
Email: [debasishmath92@gmail.com](mailto:debasishmath92@gmail.com)  
GitHub: [https://github.com/DebasishMaji](https://github.com/DebasishMaji)
