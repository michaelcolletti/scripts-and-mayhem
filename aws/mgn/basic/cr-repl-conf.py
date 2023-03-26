#!/usr/bin/env python3
# This creates a new replication configuration for a virtual machine server with ID server-1234567890abcdef, 
# using a VMware vCenter VM # manager with ID `vmmanager-1234567890abcdef`, and a replication configuration 
# template with ID template-1234567890abcdef.
import boto3

mgn = boto3.client('mgn')

response = mgn.create_replication_configuration(
    serverId='server-1234567890abcdef',
    serverType='VIRTUAL_MACHINE',
    vmServer={
        'vmManagerName': 'VMware vCenter',
        'vmManagerType': 'VSPHERE',
        'vmManagerId': 'vmmanager-1234567890abcdef',
        'vmId': 'vm-1234567890abcdef'
    },
    replicationConfigurationTemplateID='template-1234567890abcdef'
)

print(response['replicationConfigurationId'])
