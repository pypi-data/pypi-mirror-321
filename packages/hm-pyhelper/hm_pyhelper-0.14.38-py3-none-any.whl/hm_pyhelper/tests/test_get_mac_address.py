from hm_pyhelper.miner_param import get_mac_address
import unittest
from unittest.mock import mock_open, patch
import sys
sys.path.append("..")


class TestGetEthMac(unittest.TestCase):
    def test_get_data(self):
        m = mock_open(read_data='Unknown')
        with patch('builtins.open', m):
            result = get_mac_address("random/path")
            self.assertEqual(result, 'UNKNOWN')

    def test_available_file(self):
        m = mock_open()
        m.side_effect = PermissionError
        with patch("builtins.open", mock_open()) as mf:
            fh_mock = mf.return_value.__enter__.return_value
            fh_mock.write.side_effect = FileNotFoundError
            get_mac_address("random/path")
            self.assertRaises(FileNotFoundError)

    def test_permissions_error(self):
        m = mock_open()
        m.side_effect = PermissionError
        with patch("builtins.open", mock_open()) as mf:
            fh_mock = mf.return_value.__enter__.return_value
            fh_mock.write.side_effect = PermissionError
            get_mac_address("random/path")
            self.assertRaises(PermissionError)

    def test_types(self):
        self.assertRaises(TypeError, get_mac_address, 1)
        self.assertRaises(TypeError, get_mac_address, ["123", "456"])
