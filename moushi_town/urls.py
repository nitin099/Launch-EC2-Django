"""multicloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from multicloud.views import home, create_vpc, get_vpc, get_subnet, create_ec2_instance, instance_launched  # noqa

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^create/$', create_vpc, name="create_vpc"),
    url(r'^get_vpcs/$', get_vpc, name="get_vpc"),
    url(r'^get_subnets/$', get_subnet),
    url(r'^ec2_instance/$', create_ec2_instance),
    url(r'^instance_launces/$', instance_launched, name="instance_launched"),

]
