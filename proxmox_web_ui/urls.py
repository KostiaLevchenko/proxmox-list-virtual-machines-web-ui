from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^virtual/machines/all/$', views.proxmox, name='virtual_machines_list'),
    url(r'^login/$', views.proxmox, name='login'),
]