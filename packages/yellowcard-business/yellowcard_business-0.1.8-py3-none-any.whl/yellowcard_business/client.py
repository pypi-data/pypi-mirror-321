import os
import json
import base64
import hmac
import hashlib
import requests
from datetime import datetime
from dotenv import load_dotenv
from .models import Payment, CreatePaymentRequest, PaymentResponse

load_dotenv()


class YellowCard:
    def __init__(self, api_key, secret_key, env):
        """
        Initializes the YellowCard.

        Args:
            env (str): The environment stage ('sandbox', 'production').
            api_key (str): The API key for authentication.
            secret_key (str): The API secret for authentication.
        """
        self.base_url = self._get_base_url(env)
        self.api_key = api_key
        self.api_secret = secret_key.encode('utf-8')

    def _get_base_url(self, stage):
        """
        Retrieves the base URL based on the provided stage.

        Args:
            stage (str): The environment stage ('sandbox', 'production').

        Returns:
            str: The base URL for the given stage.

        Raises:
            ValueError: If the stage is invalid or the base URL is not set.
        """
        base_urls = {
            "sandbox": "https://sandbox.api.yellowcard.io",
            "production": os.getenv("PRODUCTION_BASE_URL"),
        }
        if stage not in base_urls or not base_urls[stage]:
            raise ValueError(f"Invalid stage or missing base URL for stage: {stage}")
        return base_urls[stage]

    def _yellowcard_auth(self, path, method, body):
        """
        Generates the authentication headers for the YellowCard API.

        Args:
            path (str): The API endpoint path.
            method (str): The HTTP method (e.g., 'GET', 'POST').
            body (dict): The request body (if any).

        Returns:
            dict: The headers with authentication information.
        """
        # Get the current timestamp in ISO format
        date = datetime.utcnow().isoformat() + 'Z'

        # Create an HMAC object using SHA256 and the provided secret
        hmac_object = hmac.new(key=self.api_secret, digestmod=hashlib.sha256)

        # Update the HMAC with the timestamp, path, and method
        hmac_object.update(date.encode('utf-8'))
        hmac_object.update(path.encode('utf-8'))
        hmac_object.update(method.encode('utf-8'))

        # Check if the body is present and has more than one key
        if body and len(body) > 1:
            # Calculate the SHA256 hash of the JSON-serialized body and update the HMAC
            body_json = json.dumps(body)
            body_bytes = body_json.encode('utf-8')
            body_hmac = base64.b64encode(hashlib.sha256(body_bytes).digest()).decode('utf-8')
            hmac_object.update(body_hmac.encode('utf-8'))

        # Calculate the final HMAC and convert to Base64
        signature = base64.b64encode(hmac_object.digest()).decode('utf-8')

        headers = {
            "X-YC-Timestamp": date,
            "Authorization": f"YcHmacV1 {self.api_key}:{signature}"
        }
        return headers

    def _request(self, method, endpoint, params=None, data=None):
        """
        Makes an HTTP request to the API.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint.
            params (dict): Query parameters for the request.
            data (dict): JSON payload for the request.

        Returns:
            dict: The API response as a dictionary.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self._yellowcard_auth(path=endpoint, method=method, body=data)

        response = requests.request(method, url, headers=headers, params=params, json=data)
        if not response.ok:
            raise Exception(f"API call failed: {response.status_code} - {response.text}")
        return response.json()

    def get_resource(self, resource_path):
        """
        Fetches a resource from the API.

        Args:
            resource_path (str): The resource endpoint path.

        Returns:
            dict: The API response.
        """
        return self._request("GET", resource_path)

    def create_resource(self, endpoint, data):
        """
        Creates a resource via the API.

        Args:
            endpoint (str): The API endpoint for creating resources.
            data (dict): The payload for the resource creation.

        Returns:
            dict: The API response.
        """
        return self._request("POST", endpoint, data=data)

    def get_payment(self, payment_id: str) -> Payment:
        """
        Gets a payment by its ID.

        Args:
            payment_id (str): The ID of the payment to retrieve.

        Returns:
            Payment: A Payment object containing the payment details.
        """
        response = self._request("GET", f"/business/payments/{payment_id}")
        return Payment.model_validate(response)

    def accept_payment(self, payment_id: str) -> PaymentResponse:
        """
        Accepts a payment by its ID.

        Args:
            payment_id (str): The ID of the payment to accept.

        Returns:
            Payment: An object containing the payment details, accessed via .payment
        """
        response = self._request("POST", f"/business/payments/{payment_id}/accept")
        return PaymentResponse.model_validate(response)

    # Then update the deny_payment method in client.py:
    def deny_payment(self, payment_id: str) -> PaymentResponse:
        """
        Denies a payment by its ID.

        Args:
            payment_id (str): The ID of the payment to deny.

        Returns:
            PaymentResponse: An object containing the payment details, accessed via .payment
        """
        response = self._request("POST", f"/business/payments/{payment_id}/deny")
        return PaymentResponse.model_validate(response)

    def create_payment(self, payment_data: CreatePaymentRequest) -> Payment:
        """
        Submits a payment request
        Args:
            payment_data (CreatePaymentRequest): The data for the payment.
        Returns:
            Payment: A Payment object containing the payment details.
        """
        response = self._request("POST", "/business/payments/", data=payment_data.model_dump(
            exclude_none=True,  # Remove None values
            mode='json'  # Properly serialize Enums to their values
        ))
        return Payment.model_validate(response)
