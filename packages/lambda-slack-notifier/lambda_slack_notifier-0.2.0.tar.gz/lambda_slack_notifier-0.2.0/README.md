# AWS Slack Notifier

A simple Python package to send Slack notifications via AWS Lambda.

## Installation

```bash
pip install lambda-slack-notifier
```

## Usage

```python
from aws_slack_notifier import SlackNotifier

# Initialize the notifier
notifier = SlackNotifier(region_name='us-east-1')

# Send a notification
notifier.notify(
    status="SUCCESS",
    message="Job completed successfully",
    client="MyGlueJob"
)

# Send a notification with error details
notifier.notify(
    status="ERROR",
    message="Job failed",
    error="ValueError: Invalid input",
    stackTrace="Full stack trace here",
    client="MyGlueJob"
)
```

## Requirements

- AWS Lambda function named 'trigger-slack-notification' that handles Slack messaging
- Appropriate AWS IAM permissions to invoke Lambda functions
- boto3 library

## License

MIT License