import json
import boto3

class SlackNotifier:
    def __init__(self, region_name='us-east-1', function_name='trigger-slack-notification'):
        # Initialize Lambda client with the specified region
        self.lambda_client = boto3.client('lambda', region_name=region_name)
        # Store the function name to use in the invoke call
        self.function_name = function_name

    def notify_on_slack(self, status, message, error="", stackTrace="", client=""):
        payload = {
            'message': message,
            'status': status,
            'errorLogs': error,
            'stackTrace': stackTrace,
            'client': client
        }

        try:
            # Invoke the Lambda function with the payload
            response = self.lambda_client.invoke(
                FunctionName=self.function_name,
                InvocationType='RequestResponse',
                Payload=json.dumps(payload)
            )
            # Parse the response
            result = json.loads(response['Payload'].read().decode())
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to send Slack notification: {e}")
