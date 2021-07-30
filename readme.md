# LTV Calculator v1.1

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


## Pipeline Details

* "main" branch locked, can only be merged to via Pull Request.
* CI pipeline runs on creation of PR and PR can not be complete until CI is successful
* CD pipeline runs on successful merge to "main" branch.

### CI.yml:
- Runs with v3.8 and v3.9 of Python
- Installs Safety and Bandit manually (not contained within Requirements file, personal choice for the developer over whether to run these modules locally)
- Runs Unit Tests
- Performs Linting Check
- Performs Safety Check
- Performs Bandit Check (Excludes Unit Tests due to PyLint technique of using `assert`, creates false positive results)

### Main.yml:
* Sets up Python v3.8
* Runs Unit Tests
* Creates zip file containing relevant code only
* Configures AWS Credentials using GitHub Secrets
* Uses AWS CLI to deploy directly to Lambda

### Develop.yml:
* Failed experiment, runs on merge to "develop" branch
* Intended to push direct to a version of Lambda but seemingly impossible
* ... requires research