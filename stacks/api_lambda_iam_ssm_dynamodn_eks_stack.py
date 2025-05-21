from aws_cdk import (
    Stack,
    Duration,
    aws_iam as iam,
    aws_lambda as lambdafunc
)


from constructs import Construct
from resources.lambda_function import create_lambda_function
from resources.dynamodb_db import create_dynamodb_table


class KevinLDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        dynamodb_table = create_dynamodb_table(self)
        lambda_function = create_lambda_function(self, dynamodb_table)
        # iam_role = create_iam_role(self)




