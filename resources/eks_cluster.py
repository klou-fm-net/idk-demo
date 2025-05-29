from aws_cdk import (
   aws_eks as eks,
   aws_ec2 as ec2
)

def create_eks_ckuser_and_service(scope, vpc): 
    
    eks.Cluster(scope, "DemoAppEKS",
        version=eks.KubernetesVersion.V1_27,
        vpc=vpc,
        default_capacity=1,
        default_capacity_instance=ec2.InstanceType("t2.micro")
    )
