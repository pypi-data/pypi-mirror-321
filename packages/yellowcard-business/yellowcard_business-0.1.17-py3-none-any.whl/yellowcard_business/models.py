from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class AccountType(str, Enum):
    BANK = 'bank'
    MOMO = 'momo'


class Sender(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    idNumber: Optional[str] = None
    idType: Optional[str] = None
    additionalIdNumber: Optional[str] = None
    additionalIdType: Optional[str] = None
    businessName: Optional[str] = None
    businessId: Optional[str] = None
    verifiableCredentials: Optional[dict] = None


class Destination(BaseModel):
    accountBank: Optional[str] = None
    accountNumber: str
    accountType: AccountType
    networkId: Optional[str] = None
    networkName: Optional[str] = None
    country: Optional[str] = None
    accountName: Optional[str] = None
    phoneNumber: Optional[str] = None
    branch: Optional[str] = None
    branchCode: Optional[str] = None


class Payment(BaseModel):
    partnerId: str = Field(description='The ID of the partner')
    currency: str
    rate: float
    status: str
    createdAt: datetime
    sequenceId: str
    country: str
    reason: str
    sender: Sender
    convertedAmount: int
    channelId: str
    expiresAt: datetime
    updatedAt: datetime
    amount: float
    destination: Destination
    id: str


class PaymentResponse(BaseModel):
    payment: Payment


class PaymentReasons(str, Enum):
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
    RETAIL = 'retail'
    INSTITUTION = 'institution'


class RequestSource(str, Enum):
    API = 'api'
    WIDGET = 'widget'
    FIREBLOCKS = 'fireblocks'
    TBDEX = 'tbdex'


class Recipient(Sender):
    phone: Optional[str] = None


class PaymentSettlementInfo(BaseModel):
    walletAddress: Optional[str] = None
    cryptoCurrency: Optional[str] = None
    cryptoNetwork: Optional[str] = None
    cryptoAmount: Optional[float] = None
    cryptoUSDRate: Optional[float] = None
    originalQuoteUSD: Optional[float] = None
    originalQuoteCrypto: Optional[float] = None
    expiresAt: Optional[datetime] = None
    transactionHash: Optional[str] = None
    lnInvoice: Optional[str] = None


class CreatePaymentRequest(BaseModel):
    channelId: str
    amount: Optional[float] = None
    localAmount: Optional[float] = None
    reason: PaymentReasons
    sequenceId: str
    sender: Sender
    destination: Destination
    paymentReason: Optional[str] = None
    paymentCategory: Optional[str] = None
    incomeSource: Optional[str] = None
    forceAccept: Optional[bool] = None
    customerType: Optional[CustomerType] = None
    widgetUserId: Optional[str] = None
    directSettlement: Optional[bool] = None
    settlementInfo: Optional[PaymentSettlementInfo] = None
    attempt: Optional[int] = None


class CollectionSettlementInfo(BaseModel):
    walletAddress: str
    cryptoCurrency: str
    cryptoNetwork: str
    cryptoAmount: Optional[float] = None
    cryptoLocalRate: Optional[float] = None
    cryptoUSDRate: Optional[float] = None
    txHash: Optional[str] = None
    senderWalletAddress: Optional[str] = None
    walletTag: Optional[str] = None


class CreateCollectionRequest(BaseModel):
    channelId: str
    amount: Optional[float] = None
    localAmount: Optional[float] = None
    sequenceId: str
    recipient: Recipient
    source: Destination
    paymentReason: Optional[str] = None
    paymentCategory: Optional[str] = None
    incomeSource: Optional[str] = None
    apiKey: str
    forceAccept: Optional[bool] = None
    directSettlement: Optional[bool] = None
    settlementId: Optional[str] = None
    settlementStatus: Optional[str] = None
    settlementInfo: Optional[CollectionSettlementInfo] = None
    customerType: Optional[CustomerType] = None
    requestSource: Optional[RequestSource] = None
    widgetUserId: Optional[str] = None
    kycComplete: Optional[bool] = None
    redirectUrl: Optional[str] = None


class BankInfo(BaseModel):
    name: str
    accountNumber: Optional[str] = None
    accountName: Optional[str] = None
    branchCode: Optional[str] = None
    paymentLink: Optional[str] = None


class Collection(BaseModel):
    id: str = Field(description='ID of the collection object')
    channelId: str
    partnerId: str
    currency: str
    country: str
    amount: float
    convertedAmount: float
    rate: float
    recipient: Recipient
    source: Destination
    sequenceId: str
    createdAt: datetime
    updatetimedAt: datetime
    expiresAt: datetime
    status: str
    depositId: str
    withdrawalId: str
    apiKey: str
    bankInfo: BankInfo
    reference: str
    refundRetry: float
    refundSessionId: str
    serviceFeeAmountUSD: float
    serviceFeeAmountLocal: float
    serviceFeeId: str
    networkFeeAmountUSD: float
    networkFeeAmountLocal: float
    networkFeeId: str
    partnerFeeAmountUSD: float
    partnerFeeAmountLocal: float
    partnerFeeId: str
    refundFeeAmountUSD: float
    refundFeeAmountLocal: float
    refundFeeId: str
    forceAccept: bool
    directSettlement: bool
    settlementInfo: CollectionSettlementInfo
    requestSource: RequestSource
    widgetUserId: str
    sessionId: str
    settlementStatus: str
    errorCode: str
    redirectUrl: str
