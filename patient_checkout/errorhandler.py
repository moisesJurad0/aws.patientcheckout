import logging

logger = logging.getLogger('patientcheckout')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print(message)
    logger.info('Messaging being published')
    logger.info(message)
