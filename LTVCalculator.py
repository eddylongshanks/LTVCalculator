""" LTV Calculator v1.1  """
# pylint: disable=invalid-name


class LTVCalculator():
    """ Calculates the LTV value when given Loan Amount and Property Value """

    def __init__(self, loan_amount, property_value, max_ltv):
        """ Validate the incoming values and assign them to internal variables """

        if not isinstance(loan_amount, (int, float)):
            raise TypeError("loan_amount must be a number")
        if not isinstance(property_value, (int, float)):
            raise TypeError("property_value must be a number")
        if not isinstance(max_ltv, (int, float)):
            raise TypeError("max_ltv must be a number")

        if not loan_amount > 0:
            raise ValueError("loan_amount must be a number and be higher than zero")
        if not property_value > 0:
            raise ValueError("property_value must be a number and be higher than zero")
        if not 0 <= max_ltv <= 100:
            raise ValueError("max_ltv must be a number between 1 and 100")

        self.max_ltv = max_ltv
        self.loan_amount = loan_amount
        self.property_value = property_value

    def get_value(self):
        """ Calculate ratio of loan to value, then cap at 1.0 (≡100%) """

        ltv_result = min(float(self.loan_amount) / float(self.property_value), 1.0)
        ltv_percentage = ltv_result * 100

        # Format to one decimal place
        ltv_formatted = float(f'{ltv_percentage:.1f}')

        return ltv_formatted

    def is_acceptable(self):
        """ Return boolean dependent on acceptability within specified MAX_LTV value """

        ltv_value = self.get_value()
        max_acceptable_ltv = float(f'{self.max_ltv:.1f}')

        # Apply floor and ceiling values (0 and 100)
        max_ltv = min(100, max(0, max_acceptable_ltv))

        if ltv_value <= max_ltv:
            return True

        return False

    def __str__(self):
        return f'LTV: { self.get_value() }'

    def __repr__(self):
        return "LTVCalculator()"
