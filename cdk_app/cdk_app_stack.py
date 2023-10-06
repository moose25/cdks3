from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "wzchrbuckettestcdk", versioned=True, removal_policy=cdk.RemovalPolicy.DESTROY, auto_delete_objects=True, env=env)
