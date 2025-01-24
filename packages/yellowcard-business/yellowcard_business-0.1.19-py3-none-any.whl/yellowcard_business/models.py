from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime


class AccountType(str, Enum):
    """Enumeration of valid account types"""
    BANK = 'bank'
    MOMO = 'momo'


class Sender(BaseModel):
    name: Optional[str] = Field(None, description="The full name of the sender")
    country: Optional[str] = Field(None, description="The country code of the sender (e.g., 'NG' for Nigeria)")
    address: Optional[str] = Field(None, description="Physical address of the sender")
    dob: Optional[str] = Field(None, description="Date of birth in YYYY-MM-DD format")
    email: Optional[str] = Field(None, description="Email address of the sender")
    idNumber: Optional[str] = Field(None, description="Government-issued ID number")
    idType: Optional[str] = Field(None, description="Type of ID document provided")
    additionalIdNumber: Optional[str] = Field(None, description="Secondary ID number if required")
    additionalIdType: Optional[str] = Field(None, description="Type of secondary ID")
    businessName: Optional[str] = Field(None, description="Name of the business if sender is a business entity")
    businessId: Optional[str] = Field(None, description="Business registration number")
    verifiableCredentials: Optional[dict] = Field(None, description="Additional verification credentials")


class Destination(BaseModel):
    accountBank: Optional[str] = Field(None, description="Name of the receiving bank")
    accountNumber: str = Field(..., description="Bank account or mobile money number")
    accountType: AccountType = Field(..., description="Type of account (bank or mobile money)")
    networkId: Optional[str] = Field(None, description="Unique identifier for the payment network")
    networkName: Optional[str] = Field(None, description="Name of the payment network")
    country: Optional[str] = Field(None, description="Country code of the destination")
    accountName: Optional[str] = Field(None, description="Name of the account holder")
    phoneNumber: Optional[str] = Field(None, description="Phone number associated with the account")
    branch: Optional[str] = Field(None, description="Bank branch name")
    branchCode: Optional[str] = Field(None, description="Bank branch code")


class Payment(BaseModel):
    partnerId: str = Field(..., description="Unique identifier for the partner")
    currency: str = Field(..., description="Currency code for the transaction")
    rate: float = Field(..., description="Exchange rate applied to the transaction")
    status: str = Field(..., description="Current status of the payment")
    createdAt: datetime = Field(..., description="Timestamp when payment was created")
    sequenceId: str = Field(..., description="Unique sequence identifier for the transaction")
    country: str = Field(..., description="Country where the payment is being processed")
    reason: str = Field(..., description="Purpose of the payment")
    sender: Sender = Field(..., description="Details of the payment sender")
    convertedAmount: int = Field(..., description="Amount after currency conversion")
    channelId: str = Field(..., description="Identifier for the payment channel")
    expiresAt: datetime = Field(..., description="Timestamp when payment expires")
    updatedAt: datetime = Field(..., description="Last update timestamp")
    amount: float = Field(..., description="Original payment amount")
    destination: Destination = Field(..., description="Payment destination details")
    id: str = Field(..., description="Unique identifier for the payment")


class PaymentResponse(BaseModel):
    payment: Payment = Field(..., description="The complete payment object containing all transaction details")


class PaymentReasons(str, Enum):
    """Enumeration of valid payment reasons for transaction categorization"""
    GIFT = 'gift'
    BILLS = 'bills'
    GROCERIES = 'groceries'
    TRAVEL = 'travel'
    HEALTH = 'health'
    ENTERTAINMENT = 'entertainment'
    HOUSING = 'housing'
    SCHOOL_FEES = 'school-fees'
    OTHER = 'other'
    FIREBLOCKS = 'fireblocks'


class CustomerType(str, Enum):
    """Defines the type of customer making the transaction"""
    RETAIL = 'retail'
    INSTITUTION = 'institution'


class RequestSource(str, Enum):
    """Identifies the source of the transaction request"""
    API = 'api'
    WIDGET = 'widget'
    FIREBLOCKS = 'fireblocks'
    TBDEX = 'tbdex'


class Recipient(Sender):
    phone: Optional[str] = Field(None, description="Contact phone number of the recipient")


class PaymentSettlementInfo(BaseModel):
    walletAddress: Optional[str] = Field(None, description="Cryptocurrency wallet address for settlement")
    cryptoCurrency: Optional[str] = Field(None, description="Type of cryptocurrency (e.g., BTC, ETH)")
    cryptoNetwork: Optional[str] = Field(None, description="Blockchain network for the transaction")
    cryptoAmount: Optional[float] = Field(None, description="Amount in cryptocurrency")
    cryptoUSDRate: Optional[float] = Field(None, description="Exchange rate between crypto and USD")
    originalQuoteUSD: Optional[float] = Field(None, description="Original quoted amount in USD")
    originalQuoteCrypto: Optional[float] = Field(None, description="Original quoted amount in cryptocurrency")
    expiresAt: Optional[datetime] = Field(None, description="Expiration timestamp for the settlement quote")
    transactionHash: Optional[str] = Field(None, description="Blockchain transaction hash")
    lnInvoice: Optional[str] = Field(None, description="Lightning Network invoice string")


class CreatePaymentRequest(BaseModel):
    channelId: str = Field(..., description="Identifier for the payment channel to be used")
    amount: Optional[float] = Field(None, description="Payment amount in base currency")
    localAmount: Optional[float] = Field(None, description="Payment amount in local currency")
    reason: PaymentReasons = Field(..., description="Purpose of the payment from predefined categories")
    sequenceId: str = Field(..., description="Unique identifier for payment sequencing")
    sender: Sender = Field(..., description="Details of the payment sender")
    destination: Destination = Field(..., description="Payment destination details")
    paymentReason: Optional[str] = Field(None, description="Additional details about payment purpose")
    paymentCategory: Optional[str] = Field(None, description="Category classification for the payment")
    incomeSource: Optional[str] = Field(None, description="Source of funds for the payment")
    forceAccept: Optional[bool] = Field(None, description="Flag to force payment acceptance")
    customerType: Optional[CustomerType] = Field(None, description="Type of customer making the payment")
    widgetUserId: Optional[str] = Field(None, description="User ID when payment is initiated from widget")
    directSettlement: Optional[bool] = Field(None, description="Flag for direct settlement processing")
    settlementInfo: Optional[PaymentSettlementInfo] = Field(None, description="Details for payment settlement")
    attempt: Optional[int] = Field(None, description="Number of payment attempt")


class CollectionSettlementInfo(BaseModel):
    walletAddress: str = Field(..., description="Cryptocurrency wallet address for collection")
    cryptoCurrency: str = Field(..., description="Type of cryptocurrency being collected")
    cryptoNetwork: str = Field(..., description="Blockchain network for the collection")
    cryptoAmount: Optional[float] = Field(None, description="Amount in cryptocurrency")
    cryptoLocalRate: Optional[float] = Field(None, description="Local currency to crypto exchange rate")
    cryptoUSDRate: Optional[float] = Field(None, description="USD to crypto exchange rate")
    txHash: Optional[str] = Field(None, description="Transaction hash on the blockchain")
    senderWalletAddress: Optional[str] = Field(None, description="Sender's wallet address")
    walletTag: Optional[str] = Field(None, description="Additional identifier for the wallet")


class BankInfo(BaseModel):
    name: str = Field(..., description="Name of the bank")
    accountNumber: Optional[str] = Field(None, description="Bank account number")
    accountName: Optional[str] = Field(None, description="Name on the bank account")
    branchCode: Optional[str] = Field(None, description="Bank branch identifier code")
    paymentLink: Optional[str] = Field(None, description="Link for payment processing")

class Collection(BaseModel):
    id: str = Field(..., description="Unique identifier for the collection transaction")
    channelId: str = Field(..., description="Identifier for the payment channel used for collection")
    partnerId: str = Field(..., description="Unique identifier for the partner processing the collection")
    currency: str = Field(..., description="Three-letter currency code (e.g., 'USD', 'NGN')")
    country: str = Field(..., description="Two-letter country code where collection is processed (e.g., 'NG')")
    amount: float = Field(..., description="Original amount of the collection in specified currency")
    convertedAmount: float = Field(..., description="Amount after applying exchange rate conversion")
    rate: float = Field(..., description="Exchange rate used for currency conversion")
    recipient: Recipient = Field(..., description="Detailed information about the collection recipient")
    source: Destination = Field(..., description="Source account information for the collection")
    sequenceId: str = Field(..., description="Unique sequence identifier for transaction ordering")
    createdAt: str = Field(..., description="ISO 8601 timestamp of collection creation")
    updatedAt: str = Field(..., description="ISO 8601 timestamp of last update")
    expiresAt: str = Field(..., description="ISO 8601 timestamp when collection expires")
    status: str = Field(..., description="Current status of the collection (e.g., 'pending', 'completed')")
    depositId: Optional[str] = Field(None, description="Identifier for the deposit transaction if applicable")
    withdrawalId: Optional[str] = Field(None, description="Identifier for the withdrawal transaction if applicable")
    bankInfo: Optional[BankInfo] = Field(None, description="Bank account details for the collection")
    reference: Optional[str] = Field(None, description="External reference number for the collection")
    refundRetry: float = Field(..., description="Number of refund attempts made")
    refundSessionId: Optional[str] = Field(None, description="Session identifier for refund processing")
    serviceFeeAmountUSD: Optional[float] = Field(None, description="Service fee amount in USD")
    serviceFeeAmountLocal: Optional[float] = Field(None, description="Service fee amount in local currency")
    serviceFeeId: Optional[str] = Field(None, description="Unique identifier for the service fee")
    networkFeeAmountUSD: Optional[float] = Field(None, description="Network transaction fee in USD")
    networkFeeAmountLocal: Optional[float] = Field(None, description="Network transaction fee in local currency")
    networkFeeId: Optional[str] = Field(None, description="Unique identifier for the network fee")
    partnerFeeAmountUSD: Optional[float] = Field(None, description="Partner's fee amount in USD")
    partnerFeeAmountLocal: Optional[float] = Field(None, description="Partner's fee amount in local currency")
    partnerFeeId: Optional[str] = Field(None, description="Unique identifier for the partner fee")
    refundFeeAmountUSD: Optional[float] = Field(None, description="Refund processing fee in USD")
    refundFeeAmountLocal: Optional[float] = Field(None, description="Refund processing fee in local currency")
    refundFeeId: Optional[str] = Field(None, description="Unique identifier for the refund fee")
    forceAccept: bool = Field(..., description="Flag indicating if collection should be forcefully accepted")
    directSettlement: bool = Field(..., description="Flag indicating if collection uses direct settlement")
    settlementInfo: Optional[CollectionSettlementInfo] = Field(None, description="Details about the settlement process")
    requestSource: RequestSource = Field(..., description="Source of the collection request (API, Widget, etc.)")
    widgetUserId: Optional[str] = Field(None, description="User identifier when collection is initiated from widget")
    sessionId: Optional[str] = Field(None, description="Unique session identifier for the collection process")
    settlementStatus: Optional[str] = Field(None, description="Current status of the settlement process")
    errorCode: Optional[str] = Field(None, description="Error code if collection encountered issues")
    redirectUrl: Optional[str] = Field(None, description="URL to redirect after collection processing")