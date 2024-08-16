import boto3

session=boto3.Session(
    aws_access_key_id='AKIAZI2LEUOYMTDHF5VO',
    aws_secret_access_key='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',
    region_name='us-east-1'
)
lambdaclient=session.client('lambda')
response=lambdaclient.list_functions()
print(response)#printing the response as to know the response structure and then we can extract the required data
for functions in response['Functions']:
    print(functions['FunctionName'])   #needed function arn means put functions['FunctionArn'] in the place of 'FunctionName'
                                   