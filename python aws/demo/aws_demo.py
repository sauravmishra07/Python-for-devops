import boto3

class AWSUtils:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.bucket = []

    def list_buckets(self):

        for bucket in self.s3_client.list_buckets()["Buckets"]:
            self.bucket.append(bucket["Name"])

class AwsEC2:
    def __init__(self):
        self.ec2_client = boto3.client("ec2")
        self.instances = []

    def list_instances(self):
        for reservation in self.ec2_client.describe_instances()["Reservations"]:
            for instance in reservation["Instances"]:
                self.instances.append(instance["InstanceId"])

if __name__ == "__main__":
    aws_utils = AWSUtils()
    aws_utils.list_buckets()
    print(aws_utils.bucket)

    aws_ec2 = AwsEC2()
    aws_ec2.list_instances()
    print(aws_ec2.instances)