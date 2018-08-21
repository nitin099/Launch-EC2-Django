from django.contrib import admin
from .models import CreateVpc, CreateEc2Instance, GetVpcs, GetSubnets


class CreateVpcAdmin(admin.ModelAdmin):

    list_display = ["name_tag", "ipv4_cidr_block", "id", "timestamp", "update"]

    class Meta:
        model = CreateVpc


class CreateEc2InstanceAdmin(admin.ModelAdmin):
    list_display = ["image_id", "instance_type", "max_count", "min_count",
                    "network", "subnet_id", "timestamp",
                    "update", "instance_id"]


class GetVpcsAdmin(admin.ModelAdmin):
    list_display = ["vpc_id", "value", "cidr_state", "cidr_block"]


class GetSubnetsAdmin(admin.ModelAdmin):
    list_display = ["subnet_id", "vpc_id", "state", "cidr_block"]


admin.site.register(CreateVpc, CreateVpcAdmin)
admin.site.register(CreateEc2Instance, CreateEc2InstanceAdmin)
admin.site.register(GetVpcs, GetVpcsAdmin)
admin.site.register(GetSubnets, GetSubnetsAdmin)
