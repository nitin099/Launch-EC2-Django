import iptools


def cidr_validator(cidr):
    return iptools.ipv4.cidr2block(cidr)
