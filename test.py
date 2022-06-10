import boto3

ses = boto3.client('ses')

body = """
    Hello, this is a test for a python script for Amazon SES

    Aleksa
"""


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
                'Data' : body,
                'Charset': 'UTF-8'
            }
        }
    }
)