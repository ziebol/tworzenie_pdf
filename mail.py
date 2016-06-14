import boto3

session = boto3.session.Session()
client = session.client('ses', region_name='eu-west-1')

def send_email(to, subject, body):
    response = client.send_email(
        Source='mailing@jkan.pl',
        Destination={
            'ToAddresses': [
                to,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': body,
                    'Charset': 'utf-8'
                },
                'Html': {
                    'Data': body,
                    'Charset': 'utf-8'
                }
            }
        },
        ReplyToAddresses=[
            'mailing@jkan.pl',
        ],
        ReturnPath='mailing@jkan.pl'
    )
    return response
