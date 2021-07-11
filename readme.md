## LTV Calculator v1.1

Accepts the following two values as JSON:

```python
{
    "loan_amount": 40000,
    "property_value": 100000
}
```

Returns the following data:

```python
{
    "statusCode": 200,
    "body": {
        "ltv_percentage": 40.0,
        "is_acceptable": true
    }
}
```

- LTV Percentage
- A Boolean value determining acceptance, based on maximum LTV value provided within an Environment Variable set on the Lambda function

## Changelog

### v1.1
- Added tighter Validation to passed parameters
- Removed in-situ validation from is_acceptable and get_value functions

### v1.0
- Initial Release
