# E-commerce Personalization Pipeline

An end-to-end machine learning pipeline that delivers personalized product recommendations for an e-commerce platform using AWS services. This repository demonstrates how to ingest data from AWS S3, preprocess and engineer features, train a recommendation model using XGBoost, deploy the model on Amazon SageMaker, and expose the model via RESTful APIs using AWS API Gateway and Lambda.



## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Running the Pipeline](#running-the-pipeline)
  - [Data Ingestion](#data-ingestion)
  - [Data Preprocessing & Feature Engineering](#data-preprocessing--feature-engineering)
  - [Model Training, Validation & Evaluation](#model-training-validation--evaluation)
  - [Model Deployment on SageMaker](#model-deployment-on-sagemaker)
  - [Exposing the Model via REST API](#exposing-the-model-via-rest-api)
- [Visualization & Results](#visualization--results)
- [MLOps Best Practices & Error Handling](#mlops-best-practices--error-handling)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



## Overview

This project implements a complete pipeline for e-commerce personalization that includes:

1. **Data Ingestion:** Uploading raw data to an AWS S3 bucket.
2. **Data Preprocessing & Feature Engineering:** Cleaning and transforming data to extract user behavior and product attributes.
3. **Model Training:** Training a recommendation model (using XGBoost as an example) with validation and evaluation.
4. **Model Deployment:** Deploying the model on Amazon SageMaker as a real-time inference endpoint.
5. **API Exposure:** Using AWS API Gateway and Lambda to expose the endpoint for real-time product recommendations.
6. **Visualization:** Generating exploratory data analysis (EDA) and training evaluation plots.



## Architecture

The solution leverages the following AWS services:

- **Amazon S3:** Stores raw and processed datasets.
- **Amazon SageMaker:** Handles data preprocessing, model training, and deployment.
- **SageMaker Feature Store:** (Optional) Maintains engineered features for consistency.
- **AWS Lambda:** Acts as a compute layer to invoke the SageMaker endpoint.
- **Amazon API Gateway:** Exposes a RESTful API for real-time inference.

This architecture represents an **end-to-end e-commerce personalization pipeline** leveraging AWS services. The pipeline consists of several key components, each handling different stages of data processing, model training, deployment, and inference. Below is a breakdown:



### **1. Data Ingestion**
- **Amazon S3:** Acts as the central storage for raw e-commerce data, including:
  - User behavior logs
  - Product metadata
  - Transaction records  
- **Data Flow:**  
  - **E-commerce Data Source → Amazon S3** (Labeled as **"Raw Data Upload"**)



### **2. Data Preprocessing & Feature Engineering**
- **AWS SageMaker (Notebook/Data Wrangler)**: Retrieves raw data from S3, processes it, and generates structured features. This includes:
  - **Data Cleaning**
  - **Feature Engineering**
  - **Exploratory Data Analysis (EDA)**  
- **Data Flow:**  
  - **Amazon S3 → SageMaker Notebook/Data Wrangler** (Labeled as **"Data Retrieval"**)  



### **3. Model Training**
- **Amazon SageMaker Training Job:** Uses a machine learning algorithm (e.g., **XGBoost, Deep Learning**) to train a personalization model. Key processes include:
  - **Training**
  - **Validation**
  - **Model Artifact Generation**  
- **Data Flow:**  
  - **SageMaker Preprocessing → SageMaker Training** (Labeled as **"Processed Data"**)  



### **4. Model Deployment**
- **Amazon SageMaker Model Endpoint:** Deploys the trained model as a real-time inference endpoint.  
- **Data Flow:**  
  - **SageMaker Training → SageMaker Endpoint** (Labeled as **"Deployed Model"**)  



### **5. API Exposure**
- **AWS Lambda Function:** Invokes the SageMaker endpoint for real-time recommendations.  
- **Amazon API Gateway:** Exposes a **RESTful API** that allows external clients to interact with the personalization service.  
- **Data Flow:**  
  - **Client Applications → API Gateway** (Labeled as **"API Requests"**)  
  - **API Gateway → AWS Lambda** (Labeled as **"Trigger Inference"**)  
  - **AWS Lambda → SageMaker Endpoint** (Labeled as **"Inference Request"**)  
  - **SageMaker Endpoint → AWS Lambda** (Labeled as **"Prediction Response"**)  
  - **AWS Lambda → API Gateway → Client Applications** (Labeled as **"Personalized Recommendations"**)  



### **6. Client Applications**
- **Web & Mobile Applications:** Consume the recommendations via the API for personalized user experiences.  
- **Data Flow:**  
  - **API Gateway → Client Apps** (Labeled as **"Personalized Recommendations"**)  



### **7. Monitoring & Logging (Optional)**
- **Amazon CloudWatch:** Monitors **SageMaker Endpoint** and **Lambda Function** for logging and metrics.  
- **Data Flow:**  
  - **SageMaker Endpoint → CloudWatch** (Labeled as **"Logs & Metrics"**)  
  - **AWS Lambda → CloudWatch** (Labeled as **"Logs & Metrics"**)  



### **8. Data Flow Annotations**
- **All arrows in the flowchart will be clearly labeled** to indicate the type of data or process they represent:
  - **"Raw Data Upload"** for data ingestion  
  - **"Processed Data"** for feature engineering outputs  
  - **"Model Artifacts"** for trained model files  
  - **"API Requests" / "API Responses"** for interaction between applications and the API  


The high-level architecture diagram:

![diagram](https://github.com/user-attachments/assets/bdb8d239-459c-4c47-972f-fb72f257d95f)


## Requirements

- **Python 3.8+**
- **AWS CLI** (configured with necessary permissions)
- **GitHub CLI (gh)** for repository management (optional)
- Python libraries (listed in `requirements.txt`): boto3, sagemaker, pandas, numpy, xgboost, joblib, matplotlib, seaborn



## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DebasishMaji/ecommerce-personalization.git
   cd ecommerce-personalization
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   Create a `.env` file in the root directory and add:
   
   ```env
   AWS_DEFAULT_REGION=your-region
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   ```

4. **Upload Raw Data:**

   Place your raw dataset (e.g., `ecommerce_data.csv`) in `data/raw/` (create the folder if necessary) and run:
   
   ```bash
   bash data_ingestion/s3_upload.sh
   ```



## Running the Pipeline

### Data Ingestion

- **Script:** `data_ingestion/s3_upload.sh`  
- **Action:** Uploads raw CSV files to your specified S3 bucket.

### Data Preprocessing & Feature Engineering

- **Script:** `data_preprocessing/preprocess.py`  
- **Notebook:** `data_preprocessing/visualization.ipynb`  
- **Action:** Cleans data, performs one-hot encoding, normalizes features, and saves the processed data to CSV.

### Model Training, Validation & Evaluation

- **Script:** `model_training/train.py`  
  - Splits data into training and validation sets.
  - Trains an XGBoost model.
  - Saves the model locally (to be uploaded later to S3 for deployment).
- **Script:** `model_training/evaluate.py`  
  - Generates evaluation plots (e.g., loss curves).

### Model Deployment on SageMaker

- **Script:** `deployment/deploy.py`  
- **Action:** Uploads the trained model artifact to S3, creates a SageMaker model, and deploys a real-time endpoint.  
- **Note:** Update the IAM role ARN and S3 bucket path in the script.

### Exposing the Model via REST API

- **Lambda Function:** `lambda_function/lambda_handler.py`
  - Invokes the SageMaker endpoint.
  - Expects a JSON payload with a key `"payload"` containing CSV-formatted input.
- **API Gateway:** `api_gateway/api_definition.yaml`
  - Defines a REST API that maps HTTP POST requests to your Lambda function.
  - Replace placeholders (e.g., `{region}`, `{account-id}`) with your actual values.



## Visualization & Results

- **EDA Visualizations:**  
  Open `data_preprocessing/visualization.ipynb` in JupyterLab to view:
  - Histograms, bar charts, scatter matrices, and other EDA plots.
- **Model Evaluation:**  
  Run `model_training/evaluate.py` to generate plots (loss curves, ROC curves, etc.).
- **Inference Testing:**  
  After deployment, test the API via Postman or cURL:
  
  ```bash
  curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/your-stage/predict \
    -H "Content-Type: application/json" \
    -d '{"payload": "1,2,3,4,5"}'
  ```



## MLOps Best Practices & Error Handling

- **Version Control:**  
  Use Git to manage changes. Follow branching strategies and code reviews.
- **Automated Testing:**  
  Write unit tests for preprocessing, training, and inference functions.
- **Logging & Monitoring:**  
  Configure CloudWatch for SageMaker, Lambda, and API Gateway. Set up alarms for error detection.
- **Error Handling:**  
  Implement try-except blocks in Python and Lambda functions. Use API Gateway retry policies to handle transient errors.
- **CI/CD:**  
  Integrate with pipelines (e.g., GitHub Actions or Azure DevOps) to automate testing, model retraining, and deployment.



## Usage Examples

After deploying the API, send a POST request with a CSV-formatted payload to obtain real-time predictions. For example:

```bash
curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/your-stage/predict \
  -H "Content-Type: application/json" \
  -d '{"payload": "1,2,3,4,5"}'
```

The API will return a JSON response similar to:

```json
{
  "prediction": "{\"predictions\": [0.65, 0.70, 0.80]}"
}
```



## Contributing

Contributions are welcome! If you have ideas, bug fixes, or improvements, please open an issue or submit a pull request. Ensure you follow the coding standards and document your changes appropriately.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Contact

**Debasish Maji**  
Email: [debasishmath92@gmail.com](mailto:debasishmath92@gmail.com)  
GitHub: [https://github.com/DebasishMaji](https://github.com/DebasishMaji)



Happy coding and happy recommending!
```
