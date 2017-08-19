#! /usr/bin/python

import boto3

class IAM():
    def __init__(self, aws_region):
        self.session = boto3.Session(profile_name=aws_region)

    def listOldIAMKeys(self):
        client = self.session.client('iam')
        paginator = client.get_paginator('list_users')
        for response in paginator.paginate():
            print(response)


#########################
# Main script starts here
#########################

iam = IAM('DevWest1')
iam.listOldIAMKeys()
