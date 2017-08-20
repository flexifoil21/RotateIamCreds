#! /usr/bin/python
#
# This script will list all IAM keys that have not been rotated in the last 90 days
#
#    Note: This script relies on AWS credentials being stored under ~/.aws/config and ~/.aws/credentials
#
# Usage:
#    python3 ./awsListOldIAMKeys.py <<profile>> <<numOfDays>>
#        profile = AWS account you want to run this against
#        numOfDays = flag key as needing to be rotated if more than this number of days old

import awsIAM
import sys

#########################
# Main script starts here
#########################

iam = awsIAM.IAM(sys.argv[1])
iam.listOldIAMKeys(sys.argv[2])
