from django import forms
from .validators import cidr_validator
from .models import GetSubnets, GetVpcs


vpc_ids = [(str(vpc.vpc_id), str(vpc.vpc_id)) for vpc in GetVpcs.objects.all()]
subnet_ids = [(str(i.subnet_id), str(i.subnet_id)) for i in GetSubnets.objects.all()]  # noqa


class CreateVpcForm(forms.Form):
    name_tag = forms.CharField(max_length=20)
    ipv4_cidr_block = forms.CharField(label="IPv4 CIDR block")

    def clean(self):
        cleaned_data = super(CreateVpcForm, self).clean()
        ipv = cleaned_data.get('ipv4_cidr_block')
        if cidr_validator(ipv) is None:
            raise forms.ValidationError("Invalid CIDR IPv4 (eg: 192.0.0.1/12)")
            return ipv


class CreateEc2InstanceForm(forms.Form):
    image_id = forms.CharField(max_length=50)
    instance_type = forms.CharField(max_length=50)
    max_count = forms.IntegerField(initial=1)
    min_count = forms.IntegerField(initial=1)
    network = forms.CharField(max_length=50, widget=forms.Select(choices=vpc_ids))  # noqa
    subnet_id = forms.CharField(max_length=50, widget=forms.Select(choices=subnet_ids))  # noqa
    key = forms.CharField(max_length=50)
    value = forms.CharField(max_length=50)
