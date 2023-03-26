#!/usr/bin/env python3

import boto3

mgn = boto3.client('mgn')

response = mgn.create_data_replication_job(
    sourceServerID='server-1234567890abcdef',
    sourceLocation={
        'serverGroupId': 'group-1234567890abcdef',
        'subnetIds': ['subnet-0123456789abcdef'],
        'securityGroupIds': ['sg-0123456789abcdef']
    },
    targetServerID='server-0987654321fedcba',
    targetLocation={
        'subnetIds': ['subnet-fedcba9876543210'],
        'securityGroupIds': ['sg-fedcba9876543210']
    }
)

print(response['dataReplicationJob']['dataReplicationJobID'])
