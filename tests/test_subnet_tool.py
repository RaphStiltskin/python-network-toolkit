import unittest
from subnet_tool import describe_network


class SubnetToolTests(unittest.TestCase):
    def test_common_slash_24(self):
        result = describe_network("192.0.2.10/24")
        self.assertEqual(result["Network"], "192.0.2.0/24")
        self.assertEqual(result["Netmask"], "255.255.255.0")
        self.assertEqual(result["Broadcast"], "192.0.2.255")
        self.assertEqual(result["Usable host count"], 254)

    def test_slash_31_has_two_addresses(self):
        result = describe_network("192.0.2.10/31")
        self.assertEqual(result["Usable host count"], 2)

    def test_slash_32_has_one_address(self):
        result = describe_network("192.0.2.10/32")
        self.assertEqual(result["Usable host count"], 1)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            describe_network("999.2.2.1/24")


if __name__ == "__main__":
    unittest.main()
