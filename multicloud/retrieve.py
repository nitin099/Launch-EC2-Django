import boto3
from .models import GetVpcs, GetSubnets


def retrive_vpcs():
    ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
    client = boto3.client('ec2')
    filters = [{'Name': 'tag:Name', 'Values': ['*']}]
    vpcs = list(ec2.vpcs.filter(Filters=filters))
    VpcId_list_api = list()
    VpcId_list_model = list()
    for vpc in vpcs:
        response = client.describe_vpcs(
            VpcIds=[
                vpc.id,
            ]
        )
        vpc_id = response["Vpcs"][0]["VpcId"]
        VpcId_list_api.append(vpc_id)
        value = response["Vpcs"][0]["Tags"][0]["Value"]
        cidr_state = response["Vpcs"][0]["CidrBlockAssociationSet"][0]["CidrBlockState"]["State"]  # noqa
        cidr_block = response["Vpcs"][0]['CidrBlock']
        new_vpc, created = GetVpcs.objects.get_or_create(
            vpc_id=vpc_id,
            value=value,
            cidr_state=cidr_state,
            cidr_block=cidr_block,
            )
    query = GetVpcs.objects.all()
    for i in query:
        VpcId_list_model.append(str(i.vpc_id))
    for i in VpcId_list_model:
        if i not in VpcId_list_api:
            GetVpcs.objects.get(vpc_id=i).delete()
    return True


def retrive_subnet():
    ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
    client = boto3.client('ec2')
    filters = [{'Name': 'tag:Name', 'Values': ['*']}]
    subnets = list(ec2.subnets.filter(Filters=filters))
    SubnetId_list_api = list()
    SubnetId_list_models = list()
    for subnet in subnets:
        response = client.describe_subnets(
            SubnetIds=[
                subnet.id,
            ]
        )
        subnet_id = response["Subnets"][0]["SubnetId"]
        SubnetId_list_api.append(subnet_id)
        vpc_id = response["Subnets"][0]["VpcId"]
        cidr_block = response["Subnets"][0]["CidrBlock"]
        state = response["Subnets"][0]["State"]
        new_subnet, created = GetSubnets.objects.get_or_create(
            subnet_id=subnet_id,
            vpc_id=vpc_id,
            state=state,
            cidr_block=cidr_block,
            )
    query = GetSubnets.objects.all()
    for i in query:
        SubnetId_list_models.append(str(i.subnet_id))
    for i in SubnetId_list_models:
        if i not in SubnetId_list_api:
            GetSubnets.objects.get(subnet_id=i).delete()
    return SubnetId_list_api
