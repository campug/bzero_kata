import mock_pydbus

# General Bluez D-Bus Interfaces
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


def get_dbus_path(adapter=None,
                  device=None,
                  service=None,
                  characteristic=None,
                  descriptor=None):
    """
    :param adapter: The address for the the adapter on which this device may be found.
                    For example "00:00:00:00:5A:AD"
    :param device: The address of the remote device. This must be specified in colon-separated form.
                   For example "FD:6B:11:CD:4A:9B"
    :param service: The UUID for the service on the remote device. 
                    For example "e95d5899-251d-470a-a062-fa1922dfa9a8".
    :param characteristic: The UUID for the characteristic associated with the service on the device.
                           For example "e95d93ee-251d-470a-a062-fa1922dfa9a8".
    :param descriptor: The UUID for the descriptor associated with the characteristic of the service.
                       For example "00002902-0000-1000-8000-00805f9b34fb".
    :return: The DBus object path for the requested adapter/device/service/characteristic/descriptor
    
    You may specify:

    * adapter
    * adapter, device
    * adapter, device, service
    * adapter, device, service, characteristic
    * adapter, device, service, characteristic, descriptor

    The case of the letters in the addresses and UUIDs is not relevant.

    The device path returned will always start "/org/bluez".
    """

    _mngd_objs = mock_pydbus.GetManagedObjects()

    _dbus_obj_path = None
    """
    Insert your code here to get the requested DBus object path
    """
    return _dbus_obj_path
