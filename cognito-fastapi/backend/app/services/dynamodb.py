import boto3
import os

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION")
)

TABLE_NAME = os.getenv("DYNAMO_TABLE")
table = dynamodb.Table(TABLE_NAME)
