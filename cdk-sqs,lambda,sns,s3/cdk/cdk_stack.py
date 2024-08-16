from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as lambda_,

    aws_s3 as s3,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "Mukilanbucket1099")

        queue = sqs.Queue(
            self, "CdkQueue",
            # visibility_timeout=Duration.seconds(300),
            queue_name="MukilanQueue"
        )

        # topic = sns.Topic(
        #     self, "CdkTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))

        topic = sns.Topic(
            self, "CdkTopic",
            display_name="MukilanTopic",
            topic_name="MukilanTopic"
        )


        function = lambda_.Function(
            self, "CdkFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("./lambdacode"),
            handler="lambdacode.handler",
            function_name="MukilanLambda",
        )
        