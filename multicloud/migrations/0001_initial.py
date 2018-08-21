# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-08-18 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEc2Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('image_id', models.CharField(max_length=50)),
                ('instance_type', models.CharField(max_length=50)),
                ('max_count', models.IntegerField(default=1)),
                ('min_count', models.IntegerField(default=1)),
                ('network', models.CharField(max_length=50)),
                ('subnet_id', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('instance_id', models.CharField(max_length=100)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreateVpc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('name_tag', models.CharField(max_length=40)),
                ('ipv4_cidr_block', models.CharField(max_length=16)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-update', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='GetSubnets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('subnet_id', models.CharField(max_length=100)),
                ('vpc_id', models.CharField(max_length=50)),
                ('cidr_block', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GetVpcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('vpc_id', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=50)),
                ('cidr_state', models.CharField(max_length=50)),
                ('cidr_block', models.CharField(max_length=50)),
            ],
        ),
    ]
