#! /usr/bin/python
#
# This class contains IAM access and manipulation functions

import boto3
from botocore.exceptions import ClientError
import datetime

class IAM():
    def __init__(self, aws_region):
        self.session = boto3.Session(profile_name=aws_region)

    def listOldIAMKeys(self, num_days_old):
        try:
            client = self.session.client('iam')
            now = datetime.datetime.now().replace(tzinfo=None)

            paginator = client.get_paginator('list_users')
            for response in paginator.paginate():
                print(response)
                for users in response['Users']:
                    userName = users['UserName']
                    paginator2 = client.get_paginator('list_access_keys')
                    for response in paginator2.paginate(UserName=userName):
                        try:
                            ref = response['AccessKeyMetadata'][0]
                            username = ref['UserName']
                            accessKeyID = ref['AccessKeyId']
                            createDate = ref['CreateDate'].strftime('%m/%d/%Y')
                            diff = now - ref['CreateDate'].replace(tzinfo=None)
                            if (diff.days > int(num_days_old) and (len(accessKeyID) > 1)):
                                print(username + ', ' + accessKeyID + ', ' + createDate)
                        except (IndexError):
                            print(">>>IAM configuration details missing for " + userName)
        except ClientError as e:
            print("Unexpected API error")
