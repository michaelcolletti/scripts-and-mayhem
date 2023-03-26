#!/usr/bin/env python3
import os

import aws_cdk as cdk

#from app_deploy.app_deploy_stack import AppDeployStack
from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        # Create a security group
        sg = ec2.SecurityGroup(self, "MySecurityGroup", vpc=vpc)

        # Allow inbound traffic on port 22 (SSH)
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22))

        # Create an EC2 instance
        instance = ec2.Instance(self, "MyInstance",
            instance_type=ec2.InstanceType("c5.large"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            security_group=sg,
            block_devices=[ec2.BlockDevice(device_name="/dev/xvda", volume=ec2.BlockDeviceVolume.ebs(16))]
        )

        # Make the instance highly available
        instance.instance.add_property_override("AvailabilityZone", {"Fn::Select": ["0", {"Fn::GetAZs": ""}]})

app = core.App()
MyStack(app, "my-stack")
app.synth()


#app = cdk.App()
#AppDeployStack(app, "AppDeployStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
#    )

#app.synth()
