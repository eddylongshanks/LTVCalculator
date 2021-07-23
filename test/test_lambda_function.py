

import os
import pytest
import lambda_function
from unittest import mock

class TestFunctionFloatConversion:
    """ Tests for the float_conversion function """

    def test_float_conversion_WithTextString_ThrowsTypeErrorException(self):
        """ Text String """

        # Arrange
        test_value = "testtext"

        # Act
        with pytest.raises(TypeError) as te:
            result = lambda_function.float_conversion(test_value)

        # Assert
        assert str(te.value) == "The provided value: 'testtext', must be convertible to a number"

    def test_float_conversion_WithNull_ThrowsTypeErrorException(self):
        """ Test for Null """

        # Arrange
        test_value = None

        # Act
        with pytest.raises(TypeError) as te:
            result = lambda_function.float_conversion(test_value)

        # Assert
        assert str(te.value) == "The provided value: 'None', must be convertible to a number"

    def test_float_conversion_WithFloat_ReturnsResultAsFloat(self):
        """ Test for Float """

        # Arrange
        test_value = float(45.5)

        # Act
        result = lambda_function.float_conversion(test_value)

        # Assert
        assert type(result) is float

    def test_float_conversion_WithInt_ReturnsResultAsFloat(self):
        """ Test for Int """

        # Arrange
        test_value = int(45)

        # Act
        result = lambda_function.float_conversion(test_value)

        # Assert
        assert type(result) is float

    def test_float_conversion_WithNumberAsString_ReturnsResultAsFloat(self):
        """ Test for number as string """

        # Arrange
        test_value = "55"

        # Act
        result = lambda_function.float_conversion(test_value)

        # Assert
        assert type(result) is float


class TestFunctionGetMaxLTV:
    """ Tests for get_maxltv function """

    @mock.patch.dict(os.environ, {"MAX_LTV": "80"})
    def test_get_maxltv_WithValue_ReturnsValidResponse(self):
        """ Valid value set in environment (mocked) """

        # Act
        result = lambda_function.get_maxltv()

        # Assert
        assert result == "80"
    
    @mock.patch.dict(os.environ, clear=True)
    def test_get_maxltv_WithNoValue_ThrowsValueErrorException(self):
        """ No environment value set """

        # Act
        with pytest.raises(ValueError) as te:
            result = lambda_function.get_maxltv()

        # Assert
        assert str(te.value) == "MAX_LTV environment variable does not exist"


class TestFunctionLambdaHandler:
    """ Tests for the lambda_handler function """

    testdata = [
            (100000, 100000, 100.0, False),
            (75000, 100000, 75.0, False),
            (50100, 100000, 50.1, False),
            (49900, 100000, 49.9, True),
            (30000, 100000, 30.0, True),
            (100, 100000, 0.1, True),
        ]

    @mock.patch.dict(os.environ, {"MAX_LTV": "50"})
    @pytest.mark.parametrize("loan, prop, ltv, is_acceptable", testdata)
    def test_WithParameterisedValues_ShouldReturnAppropriateResponse(self, loan, prop, ltv, is_acceptable):
        """ Parameterised Boundary Test based on max ltv of 50% """

        # Arrange
        event = {
            "loan_amount": loan, 
            "property_value": prop
        }
        context = 1
        expected = {
            'statusCode': 200,
            'body': {
                'ltv_percentage': ltv, 
                'is_acceptable': is_acceptable
            }
        }

        # Act
        result = lambda_function.lambda_handler(event, context)

        # Assert
        assert result == expected

    @pytest.mark.skip(reason="need to mock 'context' object")
    @mock.patch.dict(os.environ, {"MAX_LTV": "80"})
    def test_WithStringLoanAmount_ReturnsBadRequestWithInformativeErrorMessage(self):
        """ Invalid loan_amount value """

        # Arrange
        event = {
            "loan_amount": "invalid_loan_amount", 
            "property_value": 100000
        }
        context = 1
        expected = {
            'statusCode': 400,
            'body': "Bad Request: The provided value: 'invalid_loan_amount', must be convertible to a number"
        }

        # Act
        result = lambda_function.lambda_handler(event, context)

        # Assert
        assert result == expected

    @pytest.mark.skip(reason="need to mock 'context' object")
    @mock.patch.dict(os.environ, {"MAX_LTV": "80"})
    def test_WithStringPropertyValue_ReturnsBadRequestWithInformativeErrorMessage(self):
        """ Invalid property_value value """

        # Arrange
        event = {
            "loan_amount": 40000, 
            "property_value": "invalid_property_value"
        }
        context = 1
        expected = {
            'statusCode': 400,
            'body': "Bad Request: The provided value: 'invalid_property_value', must be convertible to a number"
        }

        # Act
        result = lambda_function.lambda_handler(event, context)

        # Assert
        assert result == expected

    @pytest.mark.skip(reason="need to mock 'context' object")
    @mock.patch.dict(os.environ, {"MAX_LTV": "80"})
    def test_WithNoLoanAmount_ReturnsBadRequestWithInformativeErrorMessage(self):
        """ Missing loan_amount value """

        # Arrange
        event = {
            "loan_amount": 40000
        }
        context = 1
        expected = {
            'statusCode': 400,
            'body': "Bad Request: Missing Value: 'property_value'"
        }

        # Act
        result = lambda_function.lambda_handler(event, context)

        # Assert
        assert result == expected

    @pytest.mark.skip(reason="need to mock 'context' object")
    @mock.patch.dict(os.environ, {"MAX_LTV": "80"})
    def test_WithNoPropertyValue_ReturnsBadRequestWithInformativeErrorMessage(self):
        """ Missing property_value value """

        # Arrange
        event = {
            "property_value": 100000
        }
        context = 1
        expected = {
            'statusCode': 400,
            'body': "Bad Request: Missing Value: 'loan_amount'"
        }

        # Act
        result = lambda_function.lambda_handler(event, context)

        # Assert
        assert result == expected
