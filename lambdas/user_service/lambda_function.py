
from utils.response import Response
from utils.sqs_service import SQSService


resp=Response()



def lambda_handler(event,context):


    order={

       "id":101,

       "item":"Laptop"

    }
    sqs = SQSService()

    sqs.send_message(order)



    return resp.success(order)
