import json
import csv
import boto3

bucket_name = '<myBucket>'

def lambda_handler(event, context):
    JobStatusResponse = event['Records'][0]['Sns']['Message']
    JobId = json.loads(JobStatusResponse)['JobId']
    
    rekognition = boto3.client('rekognition', 'us-east-1')
    s3 = boto3.client('s3', 'us-east-1')
    
    get_face_detection = rekognition.get_face_detection(JobId=JobId)
    data = get_face_detection
    
    file_name = '/tmp/analysis-{}.csv'.format(JobId)
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Timestamp', 'Type', 'Confidence'])
    
        for i in data['Faces']:
            csv_writer.writerow([i['Timestamp'],i['Face']['Emotions'][0]['Type'],i['Face']['Emotions'][0]['Confidence']])
            
    s3.upload_file(file_name, bucket_name, 'analysis-{}.csv'.format(JobId))

