

import os
import pytest
import lambda_function

class TestFloatConversion:
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
