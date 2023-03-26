#!/usr/bin/env python3

import boto3

mgn = boto3.client('mgn')

response = mgn.describe_replication_configurations()

for config in response['items']:
    print(config['replicationConfigurationId'])
