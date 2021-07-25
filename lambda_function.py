""" Lambda to consume the LTV Calculator """

import json
import os
from LTVCalculator import LTVCalculator

def lambda_handler(event, context):
    """ Instantiate calculator and return values in a response object """

    try:
        body = json.loads(event['body'])
        loan_amount_raw = body['loan_amount']
        property_value_raw = body['property_value']
    except Exception as e:
        return response_object(400, f"Bad Request: Missing Value: {str(e)}")

    try:
        loan_amount = float_conversion(loan_amount_raw)
        property_value = float_conversion(property_value_raw)
        max_ltv = float_conversion(get_maxltv())

        ltv_calculator = LTVCalculator(loan_amount, property_value, max_ltv)

        ltv_percentage = ltv_calculator.get_value()
        is_acceptable = ltv_calculator.is_acceptable()

        data = {
            "ltv_percentage": ltv_percentage,
            "is_acceptable": is_acceptable
        }

        return response_object(200, data)
    except Exception as e:
        return response_object(400, f"Bad Request: {str(e)}")

def float_conversion(value):
    """ Attempt to convert incoming value to a float """

    try:
        return float(value)
    except:
        raise TypeError(f"The provided value: '{value}', must be convertible to a number")

def get_maxltv():
    """ Return MAX_LTV from Env Variable """

    maxltv = os.environ.get('MAX_LTV')

    if maxltv is not None:
        return maxltv
    else:
        raise ValueError("MAX_LTV environment variable does not exist")

def response_object(status_code, message):
    """ encapsulates the return object """

    return {
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
