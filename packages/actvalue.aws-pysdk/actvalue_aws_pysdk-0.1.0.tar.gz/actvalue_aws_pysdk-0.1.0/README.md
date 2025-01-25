# AWS Python SDK

Simple wrapper for AWS boto3 sdk commonly used functions.

Provide the following environment variables:

- ENV: development | production | ...
- AWSPROFILE: A named profile (non default) in the credential file, e.g.: 'myprofile'
- AWSREGION: A region name, e.g.: 'eu-west-1

AWSPROFILE and AWSREGION are needed in development only, production uses the default session / client configuration.

## Installation

```bash
pip install actvalue.aws-pysdk
```

## Usage

```python
from aws_pysdk import s3_write, s3_read

# Write to S3
s3_write('my-bucket', 'hello.txt', 'Hello World', 'text/plain')

# Read from S3
response = s3_read('my-bucket', 'hello.txt')
content = response['Body'].read()
```

## Develpment and test

### Create and activate virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### Install package in development mode
```bash
pip install -e .
```