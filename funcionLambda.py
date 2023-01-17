import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    items = event["items"]
    preference_data = {
       "items": items
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    print(json.dumps(preference))
    return {
        "statusCode": 200,
        "body": json.dumps(
            preference
        ),
    }
