import json
from utils.response import Response



response=Response()


def lambda_handler(event,context):

    for record in event["Records"]:

        body = json.loads(record["body"])

        order = {
            "user_id": body["user_id"],
            "item": body["item"]
        }

        print("Processing order:", order)

    user={

      "name":"John",
      "msg": "order recieved"

    }


   


    return response.success(user)
