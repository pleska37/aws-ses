import boto3

ses = boto3.client('ses')

response = ses.verify_email_identity(
  EmailAddress = 'aleksapleskovic@rocketmail.com'
)

print(response)