import json
import boto3
import pprint

bucket = '<myBucket>'

def lambda_handler(event, context):
    rekognition = boto3.client('rekognition', 'us-east-1')
    s3 = boto3.client('s3')
    start_face_detection = rekognition.start_face_detection(
    FaceAttributes="ALL",
    Video={
        'S3Object': {
            'Bucket': bucket,
            'Name': 'test2.mp4'
        }
    },
    NotificationChannel= { 
      "SNSTopicArn": "<AmazonRekognitionARN>",
      "RoleArn": "<RekognitionSNSRole>"
  }
    
    )
