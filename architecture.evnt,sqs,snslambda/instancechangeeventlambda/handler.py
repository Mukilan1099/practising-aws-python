import json

def lambda_handler(event, context):
    print(event)
   #this method is for the event directly coming from eventbridge=>sqs=>lambda
   #only differnce betweeen two is it is parsing the data...based on this option only:raw messaage delivery.if enabled,no additional metadata is added to the message,so 1 parse is enough.
   
    for record in event['Records']:
        # The SQS message body contains the SNS message in JSON format
        sns_message = json.loads(record['body'])
        
        # Extract the 'detail' part of the event, which includes the state
        event_data = sns_message
        
        # Extract the state of the EC2 instance from the event data
        ec2_state = event_data['detail']['state']
        ec2_instance_id = event_data['detail']['instance-id']
        
        # Print the EC2 instance state and instance ID
        print(f"EC2 instance {ec2_instance_id} state: {ec2_state}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('State printed successfully!')
    }
#here it is used ,when the raw message delivery is not enabled ,so it comes with th message masked from the sns.so 2 parse needed to out the expected output.
# def lambda_handler(event, context):
#     print(event)
#     for record in event['Records']:
#         # Parse the SQS message body
#         body = json.loads(record['body'])
        
#         # Parse the SNS message contained within the SQS body
#         sns_message = json.loads(body['Message'])
        
#         # Extract the EC2 instance state from the SNS message
#         instance_id = sns_message['detail']['instance-id']
#         state = sns_message['detail']['state']
        
#         # Print the EC2 instance state
#         print(f"EC2 Instance {instance_id} is now {state}")
        
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Processed EC2 state change event')
#     }
