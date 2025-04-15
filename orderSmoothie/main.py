import json
from flask import Response

def orderSmoothies(request):
    try:
        body = request.get_json()

        response = 'Sending Smoothie ID {} to table {}'.format(body['id'], body['table_number'])

        return Response(response = response, status = 200)
                
    except Exception as e:
        print("ERROR ", e)
        return Response(response = 'INTERNAL ERROR', status = 400)
