""" Lambda to consume the LTV Calculator """

import os
from LTVCalculator import LTVCalculator

def lambda_handler(event, context):
    """ Instantiate calculator and return values in a response object """

    try:
        loan = event['loan_amount']
        prop = event['property_value']

        loan_amount = float_conversion(loan)
        property_value = float_conversion(prop)
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
        return response_object(400, str(e))

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
        'body': message
    }