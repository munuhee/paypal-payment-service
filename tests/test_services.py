"""Unit tests for the services module."""
import unittest
from unittest.mock import patch, MagicMock
from app.services import get_access_token, create_payment, execute_payment

class TestServices(unittest.TestCase):
    """
    This class contains test cases for the functions in the services module.
    """
    @patch('app.services.requests.post')
    @patch('app.services.app')
    def test_get_access_token(self, mock_app, mock_post):
        """
        Test get_access_token function.

        This test case verifies that the get_access_token function correctly
        obtains an OAuth 2.0 access token from PayPal.

        It mocks the app.config and requests.post to simulate the API call.

        Args:
            mock_app: Mock object for the app module.
            mock_post: Mock object for the requests.post function.
        """
        # Mocking app.config
        mock_app.config = {
            'PAYPAL_CLIENT_ID': 'mock_client_id',
            'PAYPAL_CLIENT_SECRET': 'mock_client_secret'
        }

        # Mocking requests.post response
        mock_response = MagicMock()
        mock_response.json.return_value = {'access_token': 'mock_access_token'}
        mock_post.return_value = mock_response

        # Call the function
        access_token = get_access_token()

        # Assertions
        self.assertEqual(access_token, 'mock_access_token')
        mock_post.assert_called_once_with(
            'https://api-m.sandbox.paypal.com/v1/oauth2/token',
            auth=('mock_client_id', 'mock_client_secret'),
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={'grant_type': 'client_credentials'},
            timeout=10
        )

    @patch('app.services.get_access_token')
    @patch('app.services.requests.post')
    def test_create_payment(self, mock_post, mock_get_access_token):
        """
        Test create_payment function.

        This test case verifies that the create_payment function correctly
        creates a PayPal payment.

        It mocks the get_access_token function and requests.post to simulate the API call.

        Args:
            mock_post: Mock object for the requests.post function.
            mock_get_access_token: Mock object for the get_access_token function.
        """
        # Mocking get_access_token response
        mock_get_access_token.return_value = 'mock_access_token'

        # Mocking requests.post response
        mock_response = MagicMock()
        mock_response.json.return_value = {'id': 'mock_payment_id'}
        mock_post.return_value = mock_response

        # Call the function
        payment_data = {'amount': '30.00', 'currency': 'USD'}
        payment_response = create_payment(payment_data)

        # Assertions
        self.assertEqual(payment_response, {'id': 'mock_payment_id'})
        mock_post.assert_called_once_with(
            'https://api-m.sandbox.paypal.com/v1/payments/payment',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer mock_access_token'
            },
            json=payment_data,
            timeout=10
        )

    @patch('app.services.get_access_token')
    @patch('app.services.requests.post')
    def test_execute_payment(self, mock_post, mock_get_access_token):
        """
        Test execute_payment function.

        This test case verifies that the execute_payment function correctly
        executes a PayPal payment after user approval.

        It mocks the get_access_token function and requests.post to simulate the API call.

        Args:
            mock_post: Mock object for the requests.post function.
            mock_get_access_token: Mock object for the get_access_token function.
        """
        # Mocking get_access_token response
        mock_get_access_token.return_value = 'mock_access_token'

        # Mocking requests.post response
        mock_response = MagicMock()
        mock_response.json.return_value = {'state': 'approved'}
        mock_post.return_value = mock_response

        # Call the function
        payment_id = 'mock_payment_id'
        payer_id = 'mock_payer_id'
        execution_response = execute_payment(payment_id, payer_id)

        # Assertions
        self.assertEqual(execution_response, {'state': 'approved'})
        mock_post.assert_called_once_with(
            f'https://api-m.sandbox.paypal.com/v1/payments/payment/{payment_id}/execute',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer mock_access_token'
            },
            json={'payer_id': payer_id},
            timeout=10
        )

if __name__ == '__main__':
    unittest.main()
