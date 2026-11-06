import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_fractional_weight_rates(self):
        for zone, expected in (("local", 6.85), ("regional", 9.85)):
            with self.subTest(zone=zone):
                self.assertEqual(shipping_quote(1.234, zone), expected)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
