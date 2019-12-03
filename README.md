# Example SAM function lambda-env-vars

This is a sample SAM function that displays some basic configuration of the AWS
Serverless Application Model (SAM).

It was created using the `hello-world` SAM template, and modified to display the
environment variables that Lambda exposes in its execution environment,
described
[here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-environment-variables.html).

## General Information

This SAM function template was created with the command:

```
sam init --runtime python3.7 --dependency-manager pip --name lambda-env-vars --app-template hello-world
```

I then modified the SAM Template files `app.py`, `template.yaml` and others in
order to make it do what I wanted as opposed to returning the "hello world"
string that the hello world template app does.

The CloudWatch Log Group used here is set to expire after 3 days, versus the default which never expires.

### Testing using SAM Local

You can try this function out by running `sam local invoke` with the below command. It returns output similar to what you see here.

```
sam local invoke LambdaEnvVarsFunction --event events/event.json

Invoking app.lambda_handler (python3.7)

Fetching lambci/lambda:python3.7 Docker container image.............................................................................................................................................................................................................................................................
Mounting /home/mbacchi/data/repos/mbacchi/lambda-env-vars/.aws-sam/build/LambdaEnvVarsFunction as /var/task:ro,delegated inside runtime container
START RequestId: b8396045-b89a-164d-4fa1-a2aea54ddcb5 Version: $LATEST
END RequestId: b8396045-b89a-164d-4fa1-a2aea54ddcb5
REPORT RequestId: b8396045-b89a-164d-4fa1-a2aea54ddcb5	Init Duration: 2066.65 ms	Duration: 2.33 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 23 MB	

{"statusCode":200,"body":"{\"_HANDLER\": \"app.lambda_handler\", \"AWS_REGION\": \"us-east-1\", \"AWS_EXECUTION_ENV\": \"AWS_Lambda_python3.7\", \"AWS_LAMBDA_FUNCTION_NAME\": \"test\", \"AWS_LAMBDA_FUNCTION_MEMORY_SIZE\": \"128\", \"AWS_LAMBDA_FUNCTION_VERSION\": \"$LATEST\", \"AWS_LAMBDA_LOG_GROUP_NAME\": \"/aws/lambda/test\", \"AWS_LAMBDA_LOG_STREAM_NAME\": \"2019/12/01/[$LATEST]be32830d70b0de7e919b98b8e48d9e78\", \"LANG\": \"en_US.UTF-8\", \"TZ\": \":UTC\", \"LAMBDA_TASK_ROOT\": \"/var/task\", \"LAMBDA_RUNTIME_DIR\": \"/var/runtime\", \"PATH\": \"/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin\", \"LD_LIBRARY_PATH\": \"/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib\", \"PYTHONPATH\": null, \"AWS_LAMBDA_RUNTIME_API\": null}"}
```

### Deploying to AWS

Before deploying this example, you must first have an S3 bucket to house the deployment artifacts. In this example I've used the S3 bucket named `sam-artifacts-20191124153927646200000001`.

To deploy, run the following commands(as described in the SAM tutorial
[here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html))

1. `sam build`
2. `sam package --output-template-file packaged.yaml --s3-bucket sam-artifacts-20191124153927646200000001`
3. `sam deploy --template-file packaged.yaml --region us-east-2 --capabilities CAPABILITY_IAM --stack-name lambda-env-vars`
4. `aws cloudformation describe-stacks --stack-name lambda-env-vars --region us-east-2 --query "Stacks[].Outputs"`
5. `curl -i https://x0kk0v6eoa.execute-api.us-east-2.amazonaws.com/Prod/env_vars/`

### Removing the CloudFormation stack

To delete the SAM function and the entire cloudformation stack, run:

1. `aws cloudformation delete-stack --stack-name lambda-service-deployment-cicd-test1 --region us-east-2`
