## Video Emotion analysis using AWS Rekognition, AWS Lambda and SNS

### start_analysis.py

This lambda function calls AWS Rekognition StartFaceSearch API with input video file stored in s3. AWS Rekognition will put the jobId once finished in SNS topic.


### get_analysis.py

This lambda function calls AWS Rekognition GetFaceSearch API with JobId as parameter. The result is parsed to obtain only emotion details with highest confidence and written to csv file. And the csv file is uploaded to s3 bucket for further use.
