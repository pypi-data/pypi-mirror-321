from django.db import models

"""
"hostname": "SW-PLC-33.amphia.zh",
"fqdn": "10.64.144.31",
"device_os": "cisco_ios",
"device_type": "CATALYST 4510R+E",
"added": "finder",
"createddate": "2023-10-30 13:29:17",
"changeddate": "2023-11-01 23:02:51"
"""

from nautobot.apps.models import PrimaryModel
from nautobot.dcim.models import  Device
from django.db.models import Q
from nautobot.core.models.managers import BaseManager
from nautobot.core.models.querysets import RestrictedQuerySet

class SlurpitStagedDevice(PrimaryModel):
    slurpit_id = models.BigIntegerField (unique=True)
    disabled = models.BooleanField(default=False)
    hostname = models.CharField(max_length=255, unique=True)
    fqdn = models.CharField(max_length=128)
    ipv4 = models.CharField(max_length=23, null=True)
    device_os = models.CharField(max_length=128)
    device_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255)
    createddate = models.DateTimeField()
    changeddate = models.DateTimeField()

    def __str__(self):
        return f"{self.hostname}"
    
    def get_absolute_url(self):
        return '/'
    
    class Meta:
        ordering = ("hostname",)  # Name may be null
        unique_together = (
            ("hostname"),
        )
        verbose_name = "device"
        verbose_name_plural = "device"
    


class SlurpitImportedDeviceQuerySet(RestrictedQuerySet):
    def conflicted_devices(self):
        primary_ipv4_hosts = Device.objects.filter(
            Q(primary_ip4__mask_length=32)
        ).values('primary_ip4__host')
        primary_ipv4_hosts = [str(item.get('primary_ip4__host')) for item in primary_ipv4_hosts]

        return self.filter(
            Q(hostname__in=Device.objects.values('name')) |
            Q(ipv4__in=primary_ipv4_hosts)
        )
    
class SlurpitImportedDevice(PrimaryModel):
    slurpit_id = models.BigIntegerField(unique=True)
    disabled = models.BooleanField(default=False)
    hostname = models.CharField(max_length=255, unique=True)
    fqdn = models.CharField(max_length=128)
    ipv4 = models.CharField(max_length=23, null=True)
    device_os = models.CharField(max_length=128)
    device_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255)
    createddate = models.DateTimeField()
    changeddate = models.DateTimeField()
    mapped_devicetype = models.ForeignKey(to="dcim.DeviceType", null=True, on_delete=models.SET_NULL, related_name="slurpit_imported_devices")
    mapped_device = models.OneToOneField(to="dcim.Device", null=True, on_delete=models.CASCADE, related_name="slurpit_imported_devices")

    objects = BaseManager.from_queryset(SlurpitImportedDeviceQuerySet)()

    class Meta:
        ordering = ("hostname",)  # Name may be null
        unique_together = (
            ("hostname"),
        )
        verbose_name = "device"
        verbose_name_plural = "device"

    def get_absolute_url(self):
        return '/'
    
    def __str__(self):
        return f"{self.hostname}"
    
    @property
    def slurpit_device_type(self):
        # Returns the 'slurpit_devicetype' value from the mapped_device's _custom_field_data or None if not present.
        return self.mapped_device._custom_field_data.get('slurpit_devicetype')

    def copy_staged_values(self, device: SlurpitStagedDevice):
        self.slurpit_id = device.slurpit_id
        self.disabled = device.disabled
        self.hostname = device.hostname
        self.ipv4 = device.ipv4
        self.fqdn = device.fqdn
        self.device_os = device.device_os
        self.device_type = device.device_type
        self.brand = device.brand
        self.location = device.location
        self.createddate = device.createddate
        self.changeddate = device.changeddate

    
