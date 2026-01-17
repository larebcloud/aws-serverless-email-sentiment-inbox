import boto3

s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read().decode('utf-8')

    response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )

    sentiment = response['Sentiment']
    scores = response['SentimentScore']

    print(f"Email file: {key}")
    print(f"Sentiment: {sentiment}")
    print(f"Scores: {scores}")

    return {
        "sentiment": sentiment,
        "scores": scores
    }
