# RotateIamCreds

This repository contains Python code to scan thru AWS IAM configuration and identify any accounts with keys older than X days (typically 90 days) so they can be rotated.

### Prerequisites

It is assumed the system running this script has Python3 and PIP installed.  On top of that, the following modules need to be installed:

```
pip install awscli
pip install boto3
```

This script relies on AWS credentials being configured as is described at [http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html]

## Running the script

```
python3 ./awsListOldIAMKeys.py <<profile>> <<numOfDays>>

    # profile = AWS account you want to run this against
    # numOfDays = flag key as needing to be rotated if more than this number of days old
```

## Authors

* **Russ Wilson** - *Initial work*

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
