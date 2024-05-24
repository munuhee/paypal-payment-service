"""
services.py

This module defines the services for interacting with the PayPal API.
It includes functions for obtaining an OAuth 2.0 access token, creating
a payment, and executing a payment.

Functions:
    - get_access_token: Obtains an OAuth 2.0 access token from PayPal
    - create_payment: Creates a PayPal payment
    - execute_payment: Executes a PayPal payment after user approval
"""

import requests
from app import app

def get_access_token():
    """
    Obtains an OAuth 2.0 access token from PayPal.

    Returns:
        str: The access token.
    """
    client_id = app.config['PAYPAL_CLIENT_ID']
    client_secret = app.config['PAYPAL_CLIENT_SECRET']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(
        'https://api-m.sandbox.paypal.com/v1/oauth2/token',
        auth=(client_id, client_secret),
        headers=headers,
        data=data,
        timeout=10
        )
    print(response)
    return response.json()['access_token']

def create_payment(payment_data):
    """
    Creates a PayPal payment.

    Args:
        payment_data (dict): The payment data to be sent to PayPal.

    Returns:
        dict: The response from the PayPal API.
    """
    access_token = get_access_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.post(
        'https://api-m.sandbox.paypal.com/v1/payments/payment',
        headers=headers,
        json=payment_data,
        timeout=10
        )
    return response.json()

def execute_payment(payment_id, payer_id):
    """
    Executes a PayPal payment after user approval.

    Args:
        payment_id (str): The PayPal payment ID.
        payer_id (str): The PayPal payer ID.

    Returns:
        dict: The response from the PayPal API.
    """
    access_token = get_access_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'payer_id': payer_id
    }
    response = requests.post(
        f'https://api-m.sandbox.paypal.com/v1/payments/payment/{payment_id}/execute',
        headers=headers,
        json=data,
        timeout=10
        )
    return response.json()
