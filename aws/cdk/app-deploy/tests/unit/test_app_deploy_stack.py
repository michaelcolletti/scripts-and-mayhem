import aws_cdk as core
import aws_cdk.assertions as assertions

from app_deploy.app_deploy_stack import AppDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in app_deploy/app_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AppDeployStack(app, "app-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
