import sagemaker
from sagemaker.xgboost import XGBoostModel
from sagemaker.serializers import CSVSerializer

sagemaker_session = sagemaker.Session()
role = "arn:aws:iam::YOUR_ACCOUNT_ID:role/YourSageMakerRole"  # UPDATE with your role ARN
# Update model_data with your model artifact's S3 path
model_data = "s3://your-s3-bucket/ecommerce-personalization/model/model.bin"

xgb_model = XGBoostModel(model_data=model_data,
                         role=role,
                         framework_version="1.2-1",
                         sagemaker_session=sagemaker_session,
                         entry_point="deployment/inference.py")

predictor = xgb_model.deploy(initial_instance_count=1, instance_type="ml.m4.xlarge", serializer=CSVSerializer())
print("Model deployed. Endpoint name:", predictor.endpoint_name)
