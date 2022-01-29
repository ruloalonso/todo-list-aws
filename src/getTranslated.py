import json
import decimalencoder
import todoList

def getTranslated(event, context):
    # create a response
    id = event['pathParameters']['id']
    language = event['pathParameters']['language']
    item = todoList.get_translated_item(id, language)

    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item.get('TranslatedText'),
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
