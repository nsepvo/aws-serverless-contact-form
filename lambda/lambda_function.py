import json
import boto3
import logging

# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS SES client
ses = boto3.client('ses', region_name='ap-southeast-2')

# Email config
TO_EMAIL = "nevenspooner03@gmail.com"
FROM_EMAIL = "nevenspooner03@gmail.com"

# Input limits (cost + abuse protection)
MAX_MESSAGE_LENGTH = 2000
MAX_NAME_LENGTH = 100
MAX_EMAIL_LENGTH = 150


def lambda_handler(event, context):
    """
    Handles contact form submissions:
    - validates input
    - applies size limits
    - sends email via SES
    """

    logger.info("Request received")

    try:
        # Parse request body safely
        body = json.loads(event.get("body", "{}"))

        name = body.get("name", "")
        email = body.get("email", "")
        message = body.get("message", "")

        # Validate required fields
        if not name or not email or not message:
            return {
                "statusCode": 400,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Missing required fields"})
            }

        # Enforce size limits
        if (
            len(name) > MAX_NAME_LENGTH or
            len(email) > MAX_EMAIL_LENGTH or
            len(message) > MAX_MESSAGE_LENGTH
        ):
            return {
                "statusCode": 400,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Input too large"})
            }

        logger.info(f"Processing message from {email}")

        # Send email via SES
        ses.send_email(
            Source=FROM_EMAIL,
            Destination={"ToAddresses": [TO_EMAIL]},
            Message={
                "Subject": {
                    "Data": f"Contact Form Message from {name}"
                },
                "Body": {
                    "Text": {
                        "Data": f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                    }
                }
            }
        )

        logger.info("Email sent successfully")

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Sent"})
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")

        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Internal server error"})
        }
