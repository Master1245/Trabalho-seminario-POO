import boto3
import json

sns_client = boto3.client(
            'sns', 
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='sa-east-1')

sqs_client = boto3.client(
            'sqs', 
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='sa-east-1')

            
# puxar a fila de mensagens
# response = sqs_client.receive_message(
#     QueueUrl='https://sqs.sa-east-1.amazonaws.com/352212556623/FILA',
#     AttributeNames=[
#         'SentTimestamp'
#     ],
#     MaxNumberOfMessages=1,
#     MessageAttributeNames=[
#         'All'
#     ],
#     VisibilityTimeout=0,
#     WaitTimeSeconds=0
# )

# envio de mensagem para o SNS
response = sns_client.publish(
    TopicArn='arn:aws:sns:sa-east-1:352212556623:Fila',
    Message='Mensagem de teste',
    MessageStructure='string'
)

print(response)

# puxar as mensagem do sns