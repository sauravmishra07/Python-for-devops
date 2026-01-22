import boto3

#  Get all ec2 instace with all regions 
def get_all_regions():
    ec2 = boto3.client("ec2")
    regions = ec2.describe_regions()["Regions"]
    return [region["RegionName"] for region in regions]

def list_instances_all_regions():
    regions = get_all_regions()

    for region in regions:
        print(f"\n🔹 Region: {region}")
        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_instances()

        instances_found = False
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances_found = True
                instance_id = instance["InstanceId"]
                state = instance["State"]["Name"]
                instance_type = instance["InstanceType"]

                print(f"  InstanceId: {instance_id}")
                print(f"  State: {state}")
                print(f"  Type: {instance_type}")
                print("-" * 30)

        if not instances_found:
            print("  No instances found")
            

if __name__ == "__main__":
    list_instances_all_regions()

    