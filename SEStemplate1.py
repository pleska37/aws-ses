from socket import timeout
import boto3

ses = boto3.client('ses')

body = """
    Hello, this is a test for a python script for Amazon SES

    Aleksa
"""

emailAD = ses.verify_email_address(
    EmailAddress='pleskovicaleksa99@gmail.com'
)

emailID = ses.verify_email_identity(
  EmailAddress = 'pleskovicaleksa99@gmail.com'
)

ses.send_email(
    Source = 'pleskovicaleksa99@gmail.com',
    Destination={
        'ToAddresses': [
            'pleskovicaleksa99@gmail.com',
        ]
    },
    Message={
        'Subject': {
            'Data': 'SES Demo',
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data' :body,
                'Charset': 'UTF-8'
            }
        }
    }
)




print(emailAD)
print(emailID)