
from utils.response import Response



response=Response()


def lambda_handler(event,context):


    


    user={

      "name":"John"

    }


   


    return response.success(user)
