from aws_cdk import (
   aws_eks as eks,
   aws_ec2 as ec2,
)
from constructs import Construct
from aws_cdk.lambda_layer_kubectl_v27 import KubectlV27Layer

def create_eks_ckuser_and_service(scope, vpc): 
        kubectl_layer = KubectlV27Layer(scope, "KubectlLayer")
        cluster = eks.Cluster(
            scope, "MyEksCluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_27,
            default_capacity=1,  # uses t3.small by default
            kubectl_layer=kubectl_layer  # required
        )
