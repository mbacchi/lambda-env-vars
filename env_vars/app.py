import json
import os


def lambda_handler(event, context):
    """Display Lambda environment variables

    Lambda environment variables are described here:
    https://docs.aws.amazon.com/lambda/latest/dg/lambda-environment-variables.html

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    body = {
        "_HANDLER": os.environ.get("_HANDLER"),
        "AWS_REGION": os.environ.get("AWS_REGION"),
        "AWS_EXECUTION_ENV": os.environ.get("AWS_EXECUTION_ENV"),
        "AWS_LAMBDA_FUNCTION_NAME": os.environ.get("AWS_LAMBDA_FUNCTION_NAME"),
        "AWS_LAMBDA_FUNCTION_MEMORY_SIZE": os.environ.get(
            "AWS_LAMBDA_FUNCTION_MEMORY_SIZE"
        ),
        "AWS_LAMBDA_FUNCTION_VERSION": os.environ.get("AWS_LAMBDA_FUNCTION_VERSION"),
        "AWS_LAMBDA_LOG_GROUP_NAME": os.environ.get("AWS_LAMBDA_LOG_GROUP_NAME"),
        "AWS_LAMBDA_LOG_STREAM_NAME": os.environ.get("AWS_LAMBDA_LOG_STREAM_NAME"),
        "LANG": os.environ.get("LANG"),
        "TZ": os.environ.get("TZ"),
        "LAMBDA_TASK_ROOT": os.environ.get("LAMBDA_TASK_ROOT"),
        "LAMBDA_RUNTIME_DIR": os.environ.get("LAMBDA_RUNTIME_DIR"),
        "PATH": os.environ.get("PATH"),
        "LD_LIBRARY_PATH": os.environ.get("LD_LIBRARY_PATH"),
        "PYTHONPATH": os.environ.get("PYTHONPATH"),
        "AWS_LAMBDA_RUNTIME_API": os.environ.get("AWS_LAMBDA_RUNTIME_API"),
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
