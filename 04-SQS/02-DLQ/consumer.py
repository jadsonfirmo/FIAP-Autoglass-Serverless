from sqsHandler import SqsHandler
import time
sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/058264261117/demoqueue')

while(True):
    response = sqs.getMessage(10)
    if(len(response['Messages']) == 0):
        break

    time.sleep(1)