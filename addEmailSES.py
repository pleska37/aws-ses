import boto3

ses = boto3.client('ses')


response = ses.verify_email_address(
    EmailAddress='aleksapleskovic@rocketmail.com'
)

print(response)