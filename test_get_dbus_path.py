import unittest
# from solutions import bluezero
import bluezero


class GetPathTest(unittest.TestCase):
    def test_adapter(self):
        self.assertEqual(bluezero.get_dbus_path(adapter='00:00:00:00:5A:AD'),
                         '/org/bluez/hci0')

    def test_dev1(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD', 'E4:43:33:7E:54:1C'),
                         '/org/bluez/hci0/dev_E4_43_33_7E_54_1C')

    def test_dev2(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5a:ad', 'e4:43:33:7e:54:1c'),
                         '/org/bluez/hci0/dev_E4_43_33_7E_54_1C')

    def test_service(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD', 'F7:17:E4:09:C0:C6',
                                                'e95df2d8-251d-470a-a062-fa1922dfa9a8'),
                         '/org/bluez/hci0/dev_F7_17_E4_09_C0_C6/service0031')

    def test_service_toggle_case(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5a:ad',
                                                'f7:17:e4:09:c0:c6',
                                                'E95DF2D8-251D-470A-A062-FA1922DFA9A8'),
                         '/org/bluez/hci0/dev_F7_17_E4_09_C0_C6/service0031')

    def test_characteristic(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD',
                                                'FD:6B:11:CD:4A:9B',
                                                'e95d127b-251d-470a-a062-fa1922dfa9a8',
                                                'e95d5899-251d-470a-a062-fa1922dfa9a8'),
                         '/org/bluez/hci0/dev_FD_6B_11_CD_4A_9B/service0020/char0021')

    def test_descriptor(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD',
                                                'EB:F6:95:27:84:A0',
                                                'e95d0753-251d-470a-a062-fa1922dfa9a8',
                                                'e95dca4b-251d-470a-a062-fa1922dfa9a8',
                                                '00002902-0000-1000-8000-00805f9b34fb'),
                         '/org/bluez/hci0/dev_EB_F6_95_27_84_A0/service0013/char0014/desc0016')

    def test_descriptor_last(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD',
                                                'F7:17:E4:09:C0:C6',
                                                'e95df2d8-251d-470a-a062-fa1922dfa9a8',
                                                'e95dfb11-251d-470a-a062-fa1922dfa9a8',
                                                '00002902-0000-1000-8000-00805f9b34fb'),
                         '/org/bluez/hci0/dev_F7_17_E4_09_C0_C6/service0031/char0032/desc0034')

    def test_descriptor_first(self):
        self.assertEqual(bluezero.get_dbus_path('00:00:00:00:5A:AD',
                                                'FD:6b:11:cd:4a:9b',
                                                'e95df2d8-251d-470a-a062-fa1922dfa9a8',
                                                'e95dfb11-251d-470a-a062-fa1922dfa9a8',
                                                '00002902-0000-1000-8000-00805f9b34fb'),
                         '/org/bluez/hci0/dev_FD_6B_11_CD_4A_9B/service0031/char0032/desc0034')

    def test_descriptor_only(self):
        self.assertRaises(bluezero.InvalidSearch,
                          bluezero.get_dbus_path, descriptor='00002902-0000-1000-8000-00805f9b34fb')

if __name__ == '__main__':
    unittest.main()
