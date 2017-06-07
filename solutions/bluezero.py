import mock_pydbus

# General Bluez D-Bus Object Paths
#: BlueZ DBus Service Name
BLUEZ_SERVICE_NAME = 'org.bluez'
#: BlueZ DBus adapter interface
ADAPTER_INTERFACE = 'org.bluez.Adapter1'
#: BlueZ DBus device Interface
DEVICE_INTERFACE = 'org.bluez.Device1'

# Bluez GATT D-Bus Object Paths
#: BlueZ DBus GATT manager Interface
GATT_MANAGER_IFACE = 'org.bluez.GattManager1'
#: BlueZ DBus GATT Profile Interface
GATT_PROFILE_IFACE = 'org.bluez.GattProfile1'
#: BlueZ DBus GATT Service Interface
GATT_SERVICE_IFACE = 'org.bluez.GattService1'
#: BlueZ DBus GATT Characteristic Interface
GATT_CHRC_IFACE = 'org.bluez.GattCharacteristic1'
#: BlueZ DBus GATT Descriptor Interface
GATT_DESC_IFACE = 'org.bluez.GattDescriptor1'


class InvalidSearch(Exception):
    pass


def _get_dbus_path(mngrd_objs, parent_path, iface, prop, value):
    rtrn_val = None
    for d_path in mngrd_objs:
        if parent_path in d_path:
            if iface in mngrd_objs[d_path]:
                mngrd_objs[d_path][iface][prop]
                if value.lower() in mngrd_objs[d_path][iface][prop].lower():
                    rtrn_val = d_path
    return rtrn_val


def _get_dbus_path2(objects, parent_path, iface_in, prop, value):
    if parent_path is None:
        raise InvalidSearch
    for path, iface in objects.items():
        props = iface.get(iface_in)
        if props is None:
            continue
        if props[prop].lower() == value.lower() and path.startswith(parent_path):
            return path


def get_dbus_path(adapter=None,
                  device=None,
                  service=None,
                  characteristic=None,
                  descriptor=None):

    mngd_objs = mock_pydbus.GetManagedObjects()

    _dbus_obj_path = None

    if adapter is not None:
        _dbus_obj_path = _get_dbus_path2(mngd_objs,
                                         '/org/bluez',
                                         ADAPTER_INTERFACE,
                                         'Address',
                                         adapter)

    if device is not None:
        _dbus_obj_path = _get_dbus_path2(mngd_objs,
                                         _dbus_obj_path,
                                         DEVICE_INTERFACE,
                                         'Address',
                                         device)

    if service is not None:
        _dbus_obj_path = _get_dbus_path2(mngd_objs,
                                         _dbus_obj_path,
                                         GATT_SERVICE_IFACE,
                                         'UUID',
                                         service)

    if characteristic is not None:
        _dbus_obj_path = _get_dbus_path2(mngd_objs,
                                         _dbus_obj_path,
                                         GATT_CHRC_IFACE,
                                         'UUID',
                                         characteristic)

    if descriptor is not None:
        _dbus_obj_path = _get_dbus_path2(mngd_objs,
                                         _dbus_obj_path,
                                         GATT_DESC_IFACE,
                                         'UUID',
                                         descriptor)
    return _dbus_obj_path