import json
import boto3
import pprint

pp = pprint.PrettyPrinter(indent=4)

def lambda_handler(event, context):
    rekognition = boto3.client('rekognition', 'us-east-1')
    s3 = boto3.client('s3')
    start_face_detection = rekognition.start_face_detection(
    FaceAttributes="ALL",
    Video={
        'S3Object': {
            'Bucket': 'bucket-543425021727',
            'Name': 'test2.mp4'
        }
    },
    NotificationChannel= { 
      "SNSTopicArn": "arn:aws:sns:us-east-1:543425021727:AmazonRekognition_test",
      "RoleArn": "arn:aws:iam::543425021727:role/RekognitionSNSRole"
  }
    
    )
