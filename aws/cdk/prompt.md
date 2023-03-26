## Small  VM from CDK using Typescript
Create a small AWS infrastructure using the AWS SDK and the typescript language to build a small 1 vm infrastructure with a c5 large and 16GB memory as the machine type. Make the configuration highly available in regions us-west1 and us-east1. Use the latest Amazon Linux 2 AMI and preinstall git on the vms. Please provide detailed steps on deployment and a diagram in merlin format

Perplexity response
To create a small AWS infrastructure using the AWS SDK and TypeScript language, the AWS Cloud Development Kit (CDK) can be used. The AWS CDK allows developers to design, compose, and share custom components that incorporate unique requirements using familiar programming languages such as TypeScript[1]. 

To create a small 1 VM infrastructure with a c5 large and 16GB memory as the machine type, the following steps can be taken using the AWS CDK:
1. Install Node.js and the AWS CDK Toolkit.
2. Create a new AWS CDK project using the command `cdk init app --language typescript`.
3. In the lib folder, create a new file called my-stack.ts.
4. In my-stack.ts, import the necessary AWS CDK modules and classes, such as aws_ec2 for creating EC2 instances.
5. Define a new class that extends aws_cdk.core.Stack and defines the infrastructure to be created. For example, to create a c5 large instance with 16GB memory, use the following code:
