"""Module for testing Payment class."""

import unittest
from app.models import Payment


class TestPayment(unittest.TestCase):
    """Test case for the Payment class."""

    def setUp(self):
        """Set up a Payment instance."""
        self.payment = Payment(
            payer_id="12345",
            payment_id="67890",
            amount=100,
            currency="USD",
            status="pending",
            email="test@example.com"
        )

    def test_attributes(self):
        """Test if attributes are set correctly."""
        self.assertEqual(self.payment.payer_id, "12345")
        self.assertEqual(self.payment.payment_id, "67890")
        self.assertEqual(self.payment.amount, 100)
        self.assertEqual(self.payment.currency, "USD")
        self.assertEqual(self.payment.status, "pending")
        self.assertEqual(self.payment.email, "test@example.com")

    def test_repr(self):
        """Test the __repr__ method."""
        expected_repr = (
            "<Payment 67890>"
        )
        self.assertEqual(repr(self.payment), expected_repr)

if __name__ == '__main__':
    unittest.main()
