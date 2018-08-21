from django.shortcuts import render, redirect
from .forms import CreateVpcForm, CreateEc2InstanceForm
from .models import CreateVpc, CreateEc2Instance, GetVpcs, GetSubnets
from .retrieve import retrive_vpcs, retrive_subnet
import boto3


def home(request):
    return render(request, "home.html", {})


def create_vpc(request):
    form = CreateVpcForm(request.POST or None)
    if form.is_valid():
        name_tag = request.POST.get("name_tag")
        ipv4_cidr_block = request.POST.get("ipv4_cidr_block")
        new_vpc, created = CreateVpc.objects.get_or_create(
            name_tag=name_tag,
            ipv4_cidr_block=ipv4_cidr_block,
            )
        return redirect("create_vpc")
    context = {
        "form": form,
    }
    return render(request, "create_vpc.html", context)


def get_vpc(request):
    retrive_vpcs()
    query = GetVpcs.objects.all()
    context = {
        "query": query
    }
    return render(request, "get_vpc.html", context)


def get_subnet(request):
    retrive_subnet()
    query = GetSubnets.objects.all()
    context = {
        "subnets": query
    }
    return render(request, "get_subnets.html", context)


def create_ec2_instance(request):
    retrive_subnet()
    retrive_vpcs()
    form = CreateEc2InstanceForm(request.POST or None)
    ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
    #query = CreateEc2Instance.objects.all()
    instances = None

    if form.is_valid():
        image_id = form.cleaned_data.get("image_id")
        instance_type = form.cleaned_data.get("instance_type")
        max_count = form.cleaned_data.get("max_count")
        min_count = form.cleaned_data.get("min_count")
        network = form.cleaned_data.get("network")
        subnet_id = form.cleaned_data.get("subnet_id")
        key = form.cleaned_data.get("key")
        value = form.cleaned_data.get("value")
        instances = ec2.create_instances(
            ImageId=form.cleaned_data.get("image_id"),
            MinCount=form.cleaned_data.get("max_count"),
            MaxCount=form.cleaned_data.get("min_count"),
            InstanceType=form.cleaned_data.get("instance_type"),
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': str(key),
                            'Value': str(value)
                        },
                    ]
                },
            ],
        )
        new_vpc, created = CreateEc2Instance.objects.get_or_create(
            image_id=image_id,
            instance_type=instance_type,
            max_count=max_count,
            min_count=min_count,
            network=network,
            subnet_id=subnet_id,
            key=key,
            value=value,
            instance_id=instances[0].id
            )
        if instances:
            return redirect("instance_launched")
    context = {
        "form": form,
    }
    return render(request, "create_ec2.html", context)


def instance_launched(request):
    query = CreateEc2Instance.objects.all()
    for i in query:
        instance_id = i.instance_id
        break
    context = {
        "instance_id": instance_id
    }
    return render(request, "success.html", context)
