## LTV Calculator v1.0

Accepts the following two values as JSON:

```python
{
    "loan_amount": 20000,
    "property_value": 100000
}
```

Returns the following data:

- LTV Percentage
- A Boolean value determining acceptance, based on minimum LTV value provided within an Environment Variable set on the Lambda function
