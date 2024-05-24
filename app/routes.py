"""
routes.py

This module defines the RESTful API endpoints for handling PayPal payments
within the Flask application. It includes endpoints for initiating payments,
executing payments after user approval, and handling payment cancellations.

Endpoints:
    - /payments [POST]: Initiates a PayPal payment
    - /payments/execute [POST]: Executes a PayPal payment after user approval
    - /payments/cancel [GET]: Handles payment cancellation
"""

from flask import request, jsonify, url_for
from app import app, db
from app.models import Payment
from app.services import create_payment, execute_payment

@app.route('/payments', methods=['POST'])
def initiate_payment():
    """
    RESTful endpoint to initiate a PayPal payment.

    Expects JSON data with:
        - amount: The payment amount
        - currency (optional): The currency code (default: USD)
        - description (optional): The payment description

    Returns:
        JSON response with approval URL for redirecting the user to PayPal.
    """
    payment_data = request.get_json()
    amount = payment_data.get('amount')
    currency = payment_data.get('currency', 'USD')
    description = payment_data.get('description', 'Payment transaction description')

    payment_request_data = {
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [
            {
                "amount": {
                    "total": amount,
                    "currency": currency
                },
                "description": description,
            }
        ],
        "redirect_urls": {
            "return_url": url_for('execute_payment_route', _external=True),
            "cancel_url": url_for('cancel_payment', _external=True)
        }
    }

    paypal_response = create_payment(payment_request_data)
    approval_url = next(
        (link['href'] for link in paypal_response['links'] if link['rel'] == 'approval_url'),
        None
    )

    if approval_url:
        return jsonify({"approval_url": approval_url})
    return jsonify({"error": "Failed to create payment"}), 500

@app.route('/payments/execute', methods=['POST'])
def execute_payment_route():
    """
    RESTful endpoint to execute PayPal payment after user approval.

    Query parameters:
        - paymentId: The PayPal payment ID
        - PayerID: The PayPal payer ID

    Returns:
        JSON response indicating the success or failure of the payment execution.
    """
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    result = execute_payment(payment_id, payer_id)

    if result.get('state') == 'approved':
        payment = Payment.query.filter_by(payment_id=payment_id).first()
        if payment:
            payment.status = 'approved'
            db.session.commit()

        return jsonify({"message": "Payment successful", "payment": result})
    return jsonify({"error": "Payment failed", "details": result}), 400

@app.route('/payments/cancel', methods=['GET'])
def cancel_payment():
    """
    RESTful endpoint to handle payment cancellation.

    Returns:
        JSON response indicating that the payment was cancelled by the user.
    """
    return jsonify({"message": "Payment cancelled by user"}), 200
