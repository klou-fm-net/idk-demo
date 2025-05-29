from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda as lambdafunc,
    aws_ssm as ssm,
    aws_eks as eks,
    aws_ec2 as ec2   
)


from constructs import Construct
# from resources.lambda_function import create_lambda_function
# from resources.dynamodb_db import create_dynamodb_table
# from resources.eks_cluster import create_eks_ckuser_and_service

class KevinLDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       # dynamodb_table = create_dynamodb_table(self)
       # lambda_function = create_lambda_function(self, dynamodb_table)
        # iam_role = create_iam_role(self)
        # vpc = ec2.CfnVPC(self, "eks_vpc")
        # eks_cluster = create_eks_ckuser_and_service (self, vpc)
        vpc = ec2.Vpc(self, "EksVpc", max_azs=2)

        cluster = eks.Cluster(
            self, "EksCluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_27,
            default_capacity=1  # This uses t3.small by default
        )







