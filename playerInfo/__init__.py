import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    playerId = req.params.get('id')
    if not playerId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            playerId = req_body.get('id')

    if playerId:
        playerData2 = getPlayerInfo(id = playerId)
        return func.HttpResponse(playerData2)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )




#class player
def getPlayerInfo(id):
    player = {
        "id" : 1,
        "nombre" : "Santiago",
        "apellido" : "Torres",
        "terniumDollars" : 15,
        "terniumCoins" : 20000,
        "xp" : 150,
        "level": 3
    }

    return json.dumps(player)

