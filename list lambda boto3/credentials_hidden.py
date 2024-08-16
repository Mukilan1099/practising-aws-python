import boto3
session=boto3.Session()
lambdaclient=session.client('lambda')
response=lambdaclient.list_functions()

for functions in response['Functions']:
    print(functions['FunctionName'])