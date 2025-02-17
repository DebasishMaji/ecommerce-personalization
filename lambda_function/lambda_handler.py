import os, json, boto3
runtime = boto3.client("sagemaker-runtime")
ENDPOINT_NAME = os.environ.get("ENDPOINT_NAME")

def lambda_handler(event, context):
    # Expect event payload to contain a CSV string under 'payload'
    payload = event.get("payload", "")
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="text/csv",
        Body=payload
    )
    result = response["Body"].read().decode("utf-8")
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": result})
    }
