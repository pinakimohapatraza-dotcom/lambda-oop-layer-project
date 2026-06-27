
from utils.response import Response


resp=Response()



def lambda_handler(event,context):


    order={

       "id":101,

       "item":"Laptop"

    }


  


    return resp.success(order)
