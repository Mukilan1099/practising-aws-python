from fastapi import FastAPI, HTTPException
import boto3
from pydantic import BaseModel, EmailStr
from mangum import Mangum

app = FastAPI()

class CreateSubscriptionRequest(BaseModel):
    email: EmailStr

class DeleteSubscriptionRequest(BaseModel):
    subscription_arn: str

@app.post("/create-sns-topic")
def create_sns_topic(request: CreateSubscriptionRequest):
    try:
        sns_client = boto3.client('sns')
        
        # Create the SNS topic
        response_topic = sns_client.create_topic(Name='sns-topic-project')
        topic_arn = response_topic['TopicArn']
        
        # Subscribe to the SNS topic
        response_subscription = sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=request.email
        )
        
        return {
            'message': 'Subscription created successfully',
            'TopicArn': topic_arn,
            'SubscriptionArn': response_subscription['SubscriptionArn']
        }

    except Exception as e:
        # Log the error
        print(f"Error creating SNS topic or subscription: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/unsubscribe")
def delete_subscription(request: DeleteSubscriptionRequest):
    sns_client = boto3.client('sns')
    
    # Unsubscribe from the SNS topic
    sns_client.unsubscribe(
        SubscriptionArn=request.subscription_arn
    )
    
    return {
        'message': 'Subscription deleted successfully',
        'SubscriptionArn': request.subscription_arn
    }

# Create Mangum handler
handler = Mangum(app)
