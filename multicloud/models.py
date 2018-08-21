from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CreateVpc(models.Model):
    name_tag = models.CharField(max_length=40)
    ipv4_cidr_block = models.CharField(max_length=16)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name_tag

    class Meta:
        ordering = ["-update", "-timestamp"]


class GetVpcs(models.Model):
    vpc_id = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    cidr_state = models.CharField(max_length=50)
    cidr_block = models.CharField(max_length=50)


class GetSubnets(models.Model):
    subnet_id = models.CharField(max_length=100)
    vpc_id = models.CharField(max_length=50)
    cidr_block = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


class CreateEc2Instance(models.Model):
    image_id = models.CharField(max_length=50)
    instance_type = models.CharField(max_length=50)
    max_count = models.IntegerField(default=1)
    min_count = models.IntegerField(default=1)
    network = models.ForeignKey(GetVpcs)
    subnet_id = models.ForeignKey(GetSubnets)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    instance_id = models.CharField(max_length=100)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
