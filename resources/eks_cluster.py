from aws_cdk import (
   aws_eks as eks,
   aws_ec2 as ec2,
)
# from aws_cdk.lambda_layer_kubectl import KubectlLayer

def create_eks_ckuser_and_service(scope, vpc): 
        cluster = eks.Cluster(
            scope, "MyEksCluster",
            version=eks.KubernetesVersion.V1_27,
            vpc=vpc,
            default_capacity=1,
            default_capacity_instance=ec2.InstanceType("t2.micro"),
            kubectl_layer = None
            # No kubectl_layer here
        )
