
from utils.response import Response



response=Response()


def lambda_handler(event,context):


    log.info(
       "User lambda started"
    )


    user={

      "name":"John"

    }


   


    return response.success(user)
