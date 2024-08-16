import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_vpc,rt,subnet.cdk_vpc,rt,subnet_stack import CdkVpc,rt,subnetStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_vpc,rt,subnet/cdk_vpc,rt,subnet_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkVpc,rt,subnetStack(app, "cdk-vpc-rt-subnet")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
