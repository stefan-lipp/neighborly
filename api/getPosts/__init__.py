import logging
import azure.functions as func
import pymongo
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ["CosmosDbConnection"]
        client = pymongo.MongoClient(url)
        database = client['neighborly']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)