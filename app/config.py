"""
config.py

This module contains the configuration settings for the Flask application.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration settings for the Flask application.

    Attributes
    ----------
    SECRET_KEY : str
        Secret key used by Flask for session management and other security-related purposes.
    PAYPAL_CLIENT_ID : str
        Client ID for accessing the PayPal API.
    PAYPAL_CLIENT_SECRET : str
        Client secret for accessing the PayPal API.
    SQLALCHEMY_DATABASE_URI : str
        URI for connecting to the database. Defaults to the value of the environment variable
        'SQLALCHEMY_DATABASE_URI'. For testing purposes, if the environment variable 'FLASK_ENV'
        is set to 'testing', the URI is set to 'sqlite:///:memory:'.

    Raises
    ------
    ValueError
        If any of the required environment variables (SECRET_KEY, PAYPAL_CLIENT_ID,
        PAYPAL_CLIENT_SECRET) are missing.
    """

    SECRET_KEY = os.getenv('SECRET_KEY')
    PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
    PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    if os.getenv('FLASK_ENV') == 'testing':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    if not SECRET_KEY or not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET or \
        not SQLALCHEMY_DATABASE_URI:
        raise ValueError("Missing one or more required environment variables.")
