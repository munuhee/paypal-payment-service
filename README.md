# Flask PayPal Payments API

![Flask PayPal Payments API](https://www.paypalobjects.com/webstatic/en_US/i/buttons/pp-acceptance-medium.png)

Welcome to the Flask PayPal Payments API! This project provides a robust RESTful API built with Flask for handling PayPal payments. Whether you're integrating PayPal payments into your e-commerce platform, donation portal, or any other application, this API serves as a reliable backend solution.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

PayPal is one of the most popular payment gateways worldwide, offering secure and convenient online transactions. Integrating PayPal into your application can enhance user experience and streamline payment processes. However, building a robust payment system from scratch can be complex and time-consuming. That's where the Flask PayPal Payments API comes in.

This API simplifies the integration of PayPal payments into your Flask application. It abstracts away the complexity of PayPal's API and provides a clean, easy-to-use interface for initiating, executing, and managing payments. Whether you're a seasoned developer or just starting with Flask, this API makes PayPal integration a breeze.

## Features

### Seamless Integration
- Integrate PayPal payments into your Flask application with minimal effort.
- Abstracts away the intricacies of PayPal's API, allowing you to focus on your application logic.

### Flexible Configuration
- Easily configure payment details such as currency, amount, and description.
- Adapt the API to suit various use cases, including e-commerce, donations, subscriptions, and more.

### Robust Security
- Implements OAuth 2.0 authentication for secure communication with PayPal's servers.
- Ensures the confidentiality and integrity of payment transactions.

### Comprehensive Documentation
- Well-documented endpoints and usage examples for easy integration.
- Clear explanations of API functionality and best practices for developers.

## Setup

Getting started with the Flask PayPal Payments API is straightforward. Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/munuhee/paypal-payment-service.git
   cd paypal-payment-service
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the project root and add the following variables:
   ```dotenv
   PAYPAL_CLIENT_ID=your_paypal_client_id
   PAYPAL_CLIENT_SECRET=your_paypal_client_secret
   ```

4. **Run the Application**:
   ```bash
   python run.py
   ```

5. **Access the API**:
   The API will be available at `http://localhost:5000`.

## Usage

Once the API is up and running, you can start using it to handle PayPal payments in your application. Here's a basic example of how to initiate a payment using cURL:

```bash
curl -X POST http://localhost:5000/payments \
-H "Content-Type: application/json" \
-d '{"amount": 10.0, "currency": "USD", "description": "Sample payment"}'
```

For more detailed usage instructions and examples, refer to the [Endpoints](#endpoints) section below.

## Endpoints

The Flask PayPal Payments API provides the following endpoints for interacting with PayPal:

### Initiate Payment

- **URL**: `/payments`
- **Method**: `POST`
- **Description**: Initiates a PayPal payment with the specified amount, currency, and description.
- **Request Body**:
  ```json
  {
      "amount": 10.0,
      "currency": "USD",
      "description": "Sample payment description"
  }
  ```
- **Response**:
  ```json
  {
      "approval_url": "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-123456789"
  }
  ```

### Execute Payment

- **URL**: `/payments/execute?paymentId={paymentId}&PayerID={PayerID}`
- **Method**: `POST`
- **Description**: Executes a PayPal payment after user approval.
- **Response**:
  ```json
  {
      "message": "Payment successful",
      "payment": {
          "id": "PAY-123456789",
          "state": "approved",
          ...
      }
  }
  ```

### Cancel Payment

- **URL**: `/payments/cancel`
- **Method**: `GET`
- **Description**: Handles payment cancellation.
- **Response**:
  ```json
  {
      "message": "Payment cancelled by user"
  }
  ```

For more information on each endpoint, including request parameters and response formats, consult the API documentation or the source code.

## Contributing

Contributions are welcome! Whether you're fixing a bug, adding a feature, or improving documentation, your contributions help make this project better for everyone. To contribute, simply fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
