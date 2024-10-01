import boto3

def send_email(subject, body, to_address):
    client = boto3.client('ses', region_name='us-east-1')
    response = client.send_email(
        Source='your_email@example.com',
        Destination={
            'ToAddresses': [to_address],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body,
                },
            },
        }
    )
    return response
