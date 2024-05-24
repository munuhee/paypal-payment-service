"""
models.py

This module defines the database Payment model model for the application.
"""

from datetime import datetime
from app import db

class Payment(db.Model):
    """ A model representing a payment in the system. """

    id = db.Column(db.Integer, primary_key=True)
    payer_id = db.Column(db.String(100), nullable=False)
    payment_id = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        """ Provides a string representation of the Payment instance. """
        return f'<Payment {self.payment_id}>'
