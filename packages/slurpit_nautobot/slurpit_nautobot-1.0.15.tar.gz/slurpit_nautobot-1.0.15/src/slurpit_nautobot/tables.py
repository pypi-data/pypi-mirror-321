import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.db.models import ManyToManyField, ManyToManyRel, F, Q, Func, Value
from django_tables2 import Column
from django_tables2.columns import BoundColumn
from django_tables2.columns.base import LinkTransform
from django_tables2.utils import Accessor
from django.utils.translation import gettext_lazy as _
from nautobot.apps.tables import ToggleColumn, ButtonsColumn
from nautobot.dcim.models import Device

from .models import SlurpitImportedDevice, SlurpitIPAddress, SlurpitInterface, SlurpitPrefix
from nautobot.extras.tables import RoleTableMixin, StatusTableMixin
from nautobot.core.tables import BaseTable
from nautobot.tenancy.tables import TenantColumn
from nautobot.dcim.tables import InterfaceTable
from nautobot.ipam.tables import PrefixTable
from nautobot.ipam.models import IPAddress, Prefix
from nautobot.dcim.models import Interface

from . import models
import netaddr

def check_link(**kwargs):
    return {}


class ImportColumn(BoundColumn):
    pass


def importing(*args, **kwargs):
    raise Exception([args, kwargs])

def greenText(value):
    return f'<span style="background-color:#ecfdf0; color: black">{value}</span>'

def greenLink(link):
    return f'<span class="greenLink" style="background-color:#ecfdf0; color: blue">{link}</span>'


class ConditionalToggle(ToggleColumn):
    def render(self, value, bound_column, record):
        if record.mapped_device_id is None or (
            record.mapped_device._custom_field_data['slurpit_devicetype'] != record.device_type or
            record.mapped_device._custom_field_data['slurpit_hostname'] != record.hostname or
            record.mapped_device._custom_field_data['slurpit_fqdn'] != record.fqdn or
            record.mapped_device._custom_field_data['slurpit_platform'] != record.device_os or 
            record.mapped_device._custom_field_data['slurpit_manufacturer'] != record.brand or
            record.mapped_device._custom_field_data['slurpit_location'] != record.location
        ):
            return super().render(value, bound_column, record)
        return super().render(value, bound_column, record)
        # return '✔'


class ConditionalLink(Column):
    def render(self, value, bound_column, record):
        if record.mapped_device_id is None:
            return value
        link = LinkTransform(attrs=self.attrs.get("a", {}), accessor=Accessor("mapped_device"))
        return link(value, value=value, record=record, bound_column=bound_column)

class ConflictedColumn(Column):
    def render(self, value, bound_column, record):
        device = Device.objects.filter(name__iexact=record.hostname).first()

        if device is None:
            masked_hosts = bytes(netaddr.IPNetwork(f'{record.ipv4}/32').ip)
            masked_prefixes = netaddr.IPNetwork(f'{record.ipv4}/32').prefixlen
            device = Device.objects.filter(Q(primary_ip4__host=masked_hosts, primary_ip4__mask_length=masked_prefixes)).first()

        original_value = ""
        column_name = bound_column.verbose_name

        if column_name == "Manufacturer":
            original_value = device.device_type.manufacturer
        elif column_name == "Platform":
            original_value = device.platform

        elif column_name == "FQDN":
            if "slurpit_fqdn" in device._custom_field_data:
                original_value = device._custom_field_data['slurpit_fqdn']
        elif column_name == "IPv4":
            if device.primary_ip4:
                original_value = str(device.primary_ip4.address)
                original_value = original_value.split("/")[0]
        else:
            original_value = device.device_type

            if record.mapped_devicetype_id is not None:
                link = LinkTransform(attrs=self.attrs.get("a", {}), accessor=Accessor("mapped_devicetype"))
                return mark_safe(f'{greenLink(link(escape(value), value=escape(value), record=record, bound_column=bound_column))}<br />{escape(original_value)}') #nosec 
            
        return mark_safe(f'<span">{greenText(escape(value))}<br/>{escape(original_value)}</span>') #nosec 
    

class DeviceTypeColumn(Column):
    def render(self, value, bound_column, record):
        if record.mapped_devicetype_id is None:
            return value
        link = LinkTransform(attrs=self.attrs.get("a", {}), accessor=Accessor("mapped_devicetype"))
        return link(record.mapped_devicetype.model, value=record.mapped_devicetype.model, record=record, bound_column=bound_column)


class SlurpitImportedDeviceTable(BaseTable):
    actions = ButtonsColumn(
        model = SlurpitImportedDevice,
        buttons=dict()
    )
    pk = ConditionalToggle()
    hostname = ConditionalLink()
    device_type = DeviceTypeColumn()

    brand = tables.Column(
        verbose_name = _('Manufacturer')
    )

    device_os = tables.Column(
        verbose_name = _('Platform')
    )

    ipv4 = tables.Column(
        verbose_name = _('IPv4')
    )

    location = tables.Column(
        verbose_name = _('Location')
    )

    last_updated = tables.Column(
        verbose_name = _('Last seen')
    )

    class Meta(BaseTable.Meta):
        model = SlurpitImportedDevice
        fields = ('pk', 'id', 'hostname', 'fqdn','brand', 'IP', 'ipv4', 'location', 'device_os', 'device_type', 'last_updated')
        default_columns = ('hostname', 'fqdn', 'device_os', 'brand' , 'device_type', 'ipv4', 'location', 'last_updated')

class PlatformTypeColumn(Column):
    def render(self, value, bound_column, record):
        if record.mapped_device:
            return record.mapped_device.device_type.default_platform
        return "-"

class ManufactureColumn(Column):
    def render(self, value, bound_column, record):
        if record.mapped_device:
            return record.mapped_device.device_type.manufacturer
        return "-"

class SlurpitOnboardedDeviceTable(BaseTable):
    actions = ButtonsColumn(
        model = SlurpitImportedDevice,
        buttons=dict()
    )
    pk = ConditionalToggle()
    hostname = ConditionalLink()
    device_type = DeviceTypeColumn()

    brand = ManufactureColumn(
        verbose_name = _('Manufacturer')
    )

    device_os = tables.Column(
        verbose_name = _('Platform')
    )

    ipv4 = tables.Column(
        verbose_name = _('IPv4')
    )

    location = tables.Column(
        verbose_name = _('Location')
    )

    last_updated = tables.Column(
        verbose_name = _('Last seen')
    )

    class Meta(BaseTable.Meta):
        model = SlurpitImportedDevice
        fields = ('pk', 'id', 'hostname', 'fqdn','brand', 'IP', 'ipv4', 'device_os', 'device_type', 'location', 'last_updated')
        default_columns = ('hostname', 'fqdn', 'device_os', 'brand' , 'device_type', 'ipv4', 'location', 'last_updated')


class ConflictDeviceTable(BaseTable):
    actions = ButtonsColumn(
        model = SlurpitImportedDevice,
        buttons=dict()
    )
    pk = ConditionalToggle()
    hostname = ConditionalLink()
    device_type = ConflictedColumn()

    brand = ConflictedColumn(
        verbose_name = _('Manufacturer')
    )

    device_os = ConflictedColumn(
        verbose_name = _('Platform')
    )

    ipv4 = ConflictedColumn(
        verbose_name = _('IPv4')
    )

    fqdn = ConflictedColumn(
        verbose_name = _('FQDN')
    )

    last_updated = tables.Column(
        verbose_name = _('Last seen')
    )

    class Meta(BaseTable.Meta):
        model = SlurpitImportedDevice
        fields = ('pk', 'id', 'hostname', 'fqdn','brand', 'IP', 'device_os', 'device_type', 'ipv4', 'last_updated')
        default_columns = ('hostname', 'fqdn', 'device_os', 'brand' , 'device_type', 'ipv4', 'last_updated')


class MigratedDeviceTable(BaseTable):
    actions = ButtonsColumn(
        model = SlurpitImportedDevice,
        buttons=dict()
    )
    pk = ConditionalToggle()
    hostname = ConditionalLink()
    device_type = DeviceTypeColumn()

    brand = tables.Column(
        verbose_name = _('Manufacturer')
    )

    device_os = tables.Column(
        verbose_name = _('Platform')
    )

    location = tables.Column(
        verbose_name = _('Location')
    )

    ipv4 = tables.Column(
        verbose_name = _('IPv4')
    )


    last_updated = tables.Column(
        verbose_name = _('Last seen')
    )

    # slurpit_devicetype = tables.Column(
    #     accessor='slurpit_device_type', 
    #     verbose_name='Original Device Type'
    # )

    class Meta(BaseTable.Meta):
        model = SlurpitImportedDevice
        fields = ('pk', 'id', 'hostname', 'fqdn','brand', 'IP', 'device_os', 'device_type', 'location', 'ipv4', 'last_updated')
        default_columns = ('hostname', 'fqdn', 'device_os', 'brand' , 'device_type', 'location', 'ipv4', 'last_updated')

    def render_device_os(self, value, record):
        return mark_safe(f'<span">{greenText(escape(value))}<br/>{escape(record.mapped_device._custom_field_data["slurpit_platform"])}</span>') #nosec
    
    def render_ipv4(self, value, record):
        return mark_safe(f'<span">{greenText(escape(value))}<br/>{escape(record.mapped_device._custom_field_data["slurpit_ipv4"])}</span>') #nosec
    
    def render_brand(self, value, record):
        return mark_safe(f'<span">{greenText(escape(value))}<br/>{escape(record.mapped_device._custom_field_data["slurpit_manufacturer"])}</span>') #nosec
    
    def render_device_type(self, value, bound_column, record):
        if record.mapped_devicetype_id is None:
            return value
        link = LinkTransform(attrs=self.attrs.get("a", {}), accessor=Accessor("mapped_devicetype"))
        return mark_safe(f'<span>{greenLink(link(escape(record.mapped_devicetype.model), value=escape(record.mapped_devicetype.model), record=record, bound_column=bound_column))}<br/>{escape(record.mapped_device._custom_field_data["slurpit_devicetype"])}</span>') #nosec 
   
    def render_location(self, value, record):
        original_val = record.mapped_device._custom_field_data["slurpit_location"]
        if str(value) == str(original_val):
            return mark_safe(f'<span">{escape(value)}<br/>{escape(original_val)}</span>') #nosec
        
        return mark_safe(f'<span">{greenText(escape(value))}<br/>{escape(original_val)}</span>') #nosec
    

class SlurpitPlanningTable(tables.Table):

    class Meta:
        attrs = {
            "class": "table table-hover object-list",
        }
        empty_text = _("No results found")

    def __init__(self, data, **kwargs):
        super().__init__(data, **kwargs)

# IPADDRESS_COPY_LINK = """
#     <span class="hover_copy">
#         <a href="{{ record.get_absolute_url }}" id="copy_{{record.id}}">
#             {{ record.address }}</a>
#         <button type="button" class="btn btn-inline btn-default hover_copy_button" data-clipboard-target="#copy_{{record.id}}">
#             <span class="mdi mdi-content-copy"></span>
#         </button>
#     </span>
# """

EDIT_LINK = """
{% if record.name != '' %}
    <a href="{{record.get_edit_url}}" id="edit_{{ record.pk }}" type="button" class="btn btn-yellow">
        <i class="mdi mdi-pencil"></i>
    </a>
{% else %}
    <span></span>
{% endif %}
"""

IPADDRESS_COPY_LINK = """
    <span class="hover_copy">
        <a id="ipaddress_{{ record.pk }}" pk={{record.pk}} class="reconcile-detail-btn">
            {{ record.address }}</a>
    </span>
"""

class SlurpitIPAddressTable(StatusTableMixin, RoleTableMixin, BaseTable):
    pk = ToggleColumn()
    address = tables.TemplateColumn(
        template_code=IPADDRESS_COPY_LINK, verbose_name="IP Address", order_by=("host", "mask_length")
    )
    tenant = TenantColumn()
    namespace = tables.Column(linkify=True)
    last_updated = tables.Column(
        verbose_name = _('Last updated')
    )

    edit = tables.TemplateColumn(
        template_code=EDIT_LINK,
        verbose_name=_('')
    )
    commit_action = tables.Column(
        verbose_name = _('Commit Action'),
        empty_values=(),
        orderable=False
    )

    class Meta(BaseTable.Meta):
        model = SlurpitIPAddress
        fields = (
            "pk",
            "address",
            "namespace",
            "type",
            "status",
            "commit_action",
            "role",
            "tenant",
            "dns_name",
            "description",
            "last_updated"
        )
        default_columns = (
            "pk",
            "address",
            "namespace",
            "type",
            "status",
            "commit_action",
            "role",
            "tenant",
            "dns_name",
            "description",
            "last_updated",
            "edit"
        )
        row_attrs = {
            "class": lambda record: "success" if not isinstance(record, SlurpitIPAddress) else "",
        }
    
    def render_commit_action(self, record):
        obj = IPAddress.objects.filter(address=record.address, parent__namespace=record.namespace)
        if obj:
            return 'Changing'
        return 'Adding'

class SlurpitInterfaceTable(InterfaceTable):
    last_updated = tables.Column(
        verbose_name = _('Last updated')
    )
    name = tables.TemplateColumn(
        template_code='<i class="mdi mdi-{% if iface.mgmt_only %}wrench{% elif iface.is_lag %}drag-horizontal-variant'
        "{% elif iface.is_virtual %}circle{% elif iface.is_wireless %}wifi{% else %}ethernet"
        '{% endif %}"></i> <a id="prefix_{{ record.pk }}" pk={{record.pk}} class="reconcile-detail-btn">{{ value }}</a>',
        attrs={"td": {"class": "text-nowrap"}},
    )
    edit = tables.TemplateColumn(
        template_code=EDIT_LINK,
        verbose_name=_('')
    )
    commit_action = tables.Column(
        verbose_name = _('Commit Action'),
        empty_values=(),
        orderable=False
    )

    class Meta(InterfaceTable.Meta):
        model = SlurpitInterface
        fields = (
            "pk",
            "name",
            "device",
            "status",
            "label",
            "enabled",
            "type",
            "description",
            "last_updated",
            "commit_action"
        )
        default_columns = (
            "pk",
            "name",
            "device",
            "status",
            "commit_action",
            "label",
            "enabled",
            "type",
            "description",
            "last_updated",
            "edit"
        )
    def render_commit_action(self, record):
        obj = Interface.objects.filter(name=record.name, device=record.device)
        if obj:
            return 'Changing'
        return 'Adding'

# PREFIX_COPY_LINK = """
# {% load helpers %}
# {% tree_hierarchy_ui_representation record.ancestors.count|as_range table.hide_hierarchy_ui%}
# <span class="hover_copy">
#   <a href="\
# {% if record.present_in_database %}\
# ?tab=prefix&pk={{ record.pk }}\
# {% else %}\
# {% url 'ipam:prefix_add' %}\
# ?prefix={{ record }}&namespace={{ object.namespace.pk }}\
# {% for loc in object.locations.all %}&locations={{ loc.pk }}{% endfor %}\
# {% if object.tenant %}&tenant_group={{ object.tenant.tenant_group.pk }}&tenant={{ object.tenant.pk }}{% endif %}\
# {% endif %}\
# " id="copy_{{record.id}}">{{ record.prefix }}</a>
#   <button type="button" class="btn btn-inline btn-default hover_copy_button" data-clipboard-target="#copy_{{record.id}}">
#     <span class="mdi mdi-content-copy"></span>
#   </button>
# </span>
# """

PREFIX_COPY_LINK = """
{% load helpers %}
{% tree_hierarchy_ui_representation record.ancestors.count|as_range table.hide_hierarchy_ui%}
<span class="hover_copy">
  <a id="prefix_{{ record.pk }}" pk={{record.pk}} class="reconcile-detail-btn">{{ record.prefix }}</a>
</span>
"""


class SlurpitPrefixTable(PrefixTable):
    last_updated = tables.Column(
        verbose_name = _('Last updated')
    )

    prefix = tables.TemplateColumn(
        template_code=PREFIX_COPY_LINK, attrs={"td": {"class": "text-nowrap"}}, order_by=("network", "prefix_length")
    )
    edit = tables.TemplateColumn(
        template_code=EDIT_LINK,
        verbose_name=_('')
    )
    commit_action = tables.Column(
        verbose_name = _('Commit Action'),
        empty_values=(),
        orderable=False
    )

    class Meta(PrefixTable.Meta):
        model = SlurpitPrefix
        fields = (
            "pk",
            "prefix",
            "type",
            "status",
            "vrf",
            "commit_action",
            "namespace",
            "tenant",
            "role",
            "description",
             "last_updated"
        )
        default_columns = (
            "pk",
            "prefix",
            "type",
            "status",
            "vrf",
            "commit_action",
            "namespace",
            "tenant",
            "role",
            "description",
            "last_updated",
            "edit"
        )
        row_attrs = {
            "class": lambda record: "success" if not record.present_in_database else "",
        }
    
    def render_commit_action(self, record):
        obj = Prefix.objects.filter(network=record.network, prefix_length=record.prefix_length, namespace=record.namespace)
        if obj:
            return 'Changing'
        return 'Adding'

