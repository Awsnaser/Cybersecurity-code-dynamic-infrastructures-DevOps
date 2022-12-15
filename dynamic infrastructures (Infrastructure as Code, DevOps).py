import boto3

# Create an IAM client
iam = boto3.client('iam')

# Define the policy
policy_document = {
    'Version': '2012-10-17',
    'Statement': [{
        'Effect': 'Allow',
        'Action': 's3:*',
        'Resource': 'arn:aws:s3:::my-secure-bucket/*',
        'Condition': {
            'IpAddress': {
                'aws:SourceIp': '1.2.3.4/32'
            }
        }
    }]
}

# Create the IAM policy
policy_name = 'my-secure-policy'
iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document)
)

# Attach the policy to an IAM user
user_name = 'my-user'
iam.attach_user_policy(
    UserName=user_name,
    PolicyArn=f'arn:aws:iam::aws:policy/{policy_name}'
)
