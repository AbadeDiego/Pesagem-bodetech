# Machine Learning Inference using AWS Lambda and Amazon EFS
Repository for deploying multiple machine learning models for inference on AWS Lambda and Amazon EFS

## Introduction 

In this repo, you will find all the code needed to deploy your application for Machine Learning Inference using AWS Lambda and Amazon EFS. 

## Application Workflow 

Here is the architectural work flow of our application:

- Create a serverless application which will __trigger__ a Lambda function upon a new model upload in your `S3 bucket`. And the function would copy that file from your S3 bucket to `EFS File System`

- Create another Lambda function that will load the model from `Amazon EFS` and performs the __prediction__ based on an image.

- Build and deploy both the application using  `AWS Serverless Application Model (AWS SAM)` application.

# Architecture 

To use the Amazon EFS file system from Lambda, you need the following:

- An Amazon __Virtual Private Cloud (Amazon VPC)__
- An __Amazon EFS__ file system created within that VPC with an access point as an application entry point for your __Lambda function__.
- A __Lambda function__ (in the same VPC and private subnets) referencing the access point.

The following diagram illustrates the solution architecture:

![Architecture Diagram](img/img1.png)

# Create an Amazon EFS file system, access point, and Lambda function

Now, we are going to use a single SAM deployment to deploy this, which will create the following two serverless applications, let’s call it :

- __app1(s3-efs)__: The serverless application which will transfer the uploaded ML models from your S3 bucket to the your EFS file system
- __app2(ml-inference)__: The serverless application which will perform the ML Inference from the client. 

![Architecture Diagram](img/img2.png)

# Demo walkthrough

Here is a quick walkthrough of the demo:

https://user-images.githubusercontent.com/56056673/131384905-4fc5cfbd-9251-4cbf-ba21-287808566073.mp4

# Feedback 
Let us know what you thought of this lab and how we can improve the experience for you in the future by completing this poll. Participants who complete the surveys from [AWS Innovate - AI/ML Edition](https://aws.amazon.com/events/aws-innovate/machine-learning/) will receive a gift code for USD25 in AWS credits. Here is the [feedback Form](https://amazonmr.au1.qualtrics.com/jfe/form/SV_3fNc9oH4ql0guCq?Session=HAN6)

AWS credits will be sent via email by 31 March, 2022.
 
Note: Only registrants of AWS Innovate - AI/ML Edition who complete the surveys will receive a gift code for USD25 in AWS credits via email.

- ![AWS Promotional Credits Terms and conditions apply](https://aws.amazon.com/awscredits/)
- Limited to 1 x USD 25 AWS credits per participant.
- Participants will be required to provide their business email addresses to receive the gift code for AWS credits.

And for queries about the AWS Innovate - AI/ML Edition and credit codes, please contact : aws-apj-marketing@amazon.com
