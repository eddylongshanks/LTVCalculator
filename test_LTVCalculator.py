""" LTV Calculator tests
"""

import pytest
from LTVCalculator import LTVCalculator

# max ltv as string
# loan amount as string
# prop value as string


class TestValidationMaxLtv:
    def test_max_ltv_AsString_ThrowsTypeErrorException(self):
        """ max_ltv as string throws TypeError Exception """

        # Arrange
        loan_amount = 50
        property_value = 100
        max_ltv = "NaN"

        # Act
        with pytest.raises(TypeError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "max_ltv must be a number"
    
    def test_max_ltv_AsFloat_ShouldInstantiateLTVCalculator(self):
        """ max_ltv as float returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 50
        property_value = 100
        max_ltv = 50.5

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)

    def test_max_ltv_AsInt_ShouldInstantiateLTVCalculator(self):
        """ max_ltv as int returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 50
        property_value = 100
        max_ltv = 50

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)
    
    def test_max_ltv_AboveMaxValue_ThrowsTypeErrorException(self):
        """ max_ltv above max configured value throws TypeError Exception """
        
        # Arrange
        loan_amount = 50
        property_value = 100
        max_ltv = 100.00001
        
        # Act
        with pytest.raises(ValueError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "max_ltv must be a number between 1 and 100"

    def test_max_ltv_BelowMinValue_ThrowsTypeErrorException(self):
        """ max_ltv below min configured value throws TypeError Exception """
        
        # Arrange
        loan_amount = 50
        property_value = 100
        max_ltv = -0.00001
        
        # Act
        with pytest.raises(ValueError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "max_ltv must be a number between 1 and 100"


class TestValidationLoanAmount:
    def test_loan_amount_AsString_ThrowsTypeErrorException(self):
        """ loan_amount as string throws TypeError Exception """
        # Arrange
        loan_amount = "NaN"
        property_value = 100
        max_ltv = 80

        # Act
        with pytest.raises(TypeError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "loan_amount must be a number"

    def test_loan_amount_AsFloat_ShouldInstantiateLTVCalculator(self):
        """ loan_amount as float returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 0.0001
        property_value = 100
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)

    def test_loan_amount_AsInt_ShouldInstantiateLTVCalculator(self):
        """ loan_amount as int returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 1
        property_value = 100
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)
    
    def test_loan_amount_BelowMinValue_ThrowsTypeErrorException(self):
        """ loan_amount below min configured value throws TypeError Exception """
        
        # Arrange
        loan_amount = 0
        property_value = 100
        max_ltv = 80
        
        # Act
        with pytest.raises(ValueError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "loan_amount must be a number and be higher than zero"


class TestValidationPropertyValue:
    def test_property_value_AsString_ThrowsTypeErrorException(self):
        """ property_value as string throws TypeError Exception """
        # Arrange
        loan_amount = 100
        property_value = "NaN"
        max_ltv = 80

        # Act
        with pytest.raises(TypeError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "property_value must be a number"

    def test_property_value_AsFloat_ShouldInstantiateLTVCalculator(self):
        """ property_value as float returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 100
        property_value = 0.0001
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)

    def test_property_value_AsInt_ShouldInstantiateLTVCalculator(self):
        """ property_value as int returns an instantiated LTVcalculator """
        
        # Arrange
        loan_amount = 100
        property_value = 1
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert isinstance(calc, LTVCalculator)
    
    def test_property_value_BelowMinValue_ThrowsTypeErrorException(self):
        """ property_value below min configured value throws TypeError Exception """
        
        # Arrange
        loan_amount = 100
        property_value = 0
        max_ltv = 80
        
        # Act
        with pytest.raises(ValueError) as te:
            calc = LTVCalculator(loan_amount, property_value, max_ltv)
        
        # Assert
        assert str(te.value) == "property_value must be a number and be higher than zero"


class TestFunctionGetValue:
    def test_get_value_WhenTryingForLTVLowerThanZeroPointOne_WillReturnZero(self):
        """ Test rounding to 1 DP, result of this calculation would be 0.00002 """

        # Arrange
        loan_amount = 1
        property_value = 5000000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.get_value() == 0.0
    
    def test_get_value_WhenTryingForLTVHigherThanMaxValue_WillReturnMaxValue(self):
        """ Tests for the cap of 100% """

        # Arrange
        test_ltv_value = 100.0
        loan_amount = 10010
        property_value = 10000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.get_value() == test_ltv_value

    def test_get_value_WithLowerValues_WillReturnLowerLTV(self):
        """ Tests for 0.1% LTV """

        # Arrange
        test_ltv_value = 0.1
        loan_amount = 100
        property_value = 100000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.get_value() == test_ltv_value

    def test_get_value_WithHigherValues_WillReturnHigherLTV(self):
        """ Tests for 99.9% LTV """

        # Arrange
        test_ltv_value = 99.9
        loan_amount = 99940
        property_value = 100000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.get_value() == test_ltv_value

    def test_get_value_WithStandardValues_WillReturnCorrectLTV(self):
        """ Tests for 40% LTV """

        # Arrange
        test_ltv_value = 40
        loan_amount = 40000
        property_value = 100000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.get_value() == test_ltv_value


class TestFunctionIsAcceptable:
    def test_is_acceptable_WithValuesBelowMaxLTV_WillReturnTrue(self):

        # Arrange
        result = True
        loan_amount = 7000
        property_value = 10000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.is_acceptable() == result
    
    def test_is_acceptable_WithValuesAboveMaxLTV_WillReturnFalse(self):

        # Arrange
        result = False
        loan_amount = 9999
        property_value = 10000
        max_ltv = 80

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.is_acceptable() == result
    
    def test_is_acceptable_WithValuesEqualToMaxLTV_WillReturnTrue(self):

        # Arrange
        result = True
        loan_amount = 9990
        property_value = 10000
        max_ltv = 99.9

        # Act
        calc = LTVCalculator(loan_amount, property_value, max_ltv)

        # Assert
        assert calc.is_acceptable() == result