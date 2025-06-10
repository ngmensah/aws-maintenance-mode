import boto3

client = boto3.client('ec2')

# Find and stop running instances except production
for reservation in client.describe_instances()['Reservations']:
    for instance in reservation['Instances']:
        tags = {t['Key']: t['Value'] for t in instance.get('Tags', [])}
        if tags.get('Environment') != 'Production':
            client.stop_instances(InstanceIds=[instance['InstanceId']])
            print(f"Stopped instance: {instance['InstanceId']}")