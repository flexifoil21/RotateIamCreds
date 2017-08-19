#! /usr/bin/python
#
# This script will list all IAM keys that have not been rotated in the last 90 days
#
#    Note: This script relies on AWS credentials being stored under ~/.aws/config and ~/.aws/credentials
#
# Usage:
#    ./awsListOldIAMKeys.py <<profile>>
#        profile = AWS account you want to run this against

import awsIAM
import sys

#########################
# Main script starts here
#########################

iam = awsIAM.IAM(sys.argv[1])
iam.listOldIAMKeys()
