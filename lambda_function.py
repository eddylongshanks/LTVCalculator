""" Lambda to consume the LTV Calculator """

import json
import os
from LTVCalculator import LTVCalculator

def lambda_handler(event, context): # pylint: disable=unused-argument
    """ Instantiate calculator and return values in a response object """

    try:
        body = json.loads(event['body'])
        loan_amount_raw = body['loan_amount']
        property_value_raw = body['property_value']
    except KeyError as ex:
        return response_object(400, f"Bad Request: Missing Value: {str(ex)}")

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
    except Exception as ex: # pylint: disable=broad-except
        return response_object(400, f"Bad Request: {str(ex)}")

def float_conversion(value):
    """ Attempt to convert incoming value to a float """

    try:
        return float(value)
    except (ValueError, TypeError) as ex:
        raise ValueError(f"The provided value: '{value}', must be convertible to a number") from ex

def get_maxltv():
    """ Return MAX_LTV from Env Variable """

    maxltv = os.environ.get('MAX_LTV')

    if maxltv is not None:
        return maxltv
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
