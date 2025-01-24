from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class AccountType(str, Enum):
    BANK = 'bank'
    MOMO = 'momo'

class Sender(BaseModel):
    name: Optional[str] 
    country: Optional[str] 
    address: Optional[str] 
    dob: Optional[str] 
    email: Optional[str] 
    idNumber: Optional[str] 
    idType: Optional[str] 
    additionalIdNumber: Optional[str] 
    additionalIdType: Optional[str] 
    businessName: Optional[str] 
    businessId: Optional[str] 
    verifiableCredentials: Optional[dict] 

class Destination(BaseModel):
    accountBank: Optional[str] 
    accountNumber: str
    accountType: AccountType
    networkId: Optional[str] 
    networkName: Optional[str] 
    country: Optional[str] 
    accountName: Optional[str] 
    phoneNumber: Optional[str] 
    branch: Optional[str] 
    branchCode: Optional[str] 


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


class PaymentSettlementInfo(BaseModel):
    walletAddress: Optional[str] 
    cryptoCurrency: Optional[str] 
    cryptoNetwork: Optional[str] 
    cryptoAmount: Optional[float] 
    cryptoUSDRate: Optional[float] 
    originalQuoteUSD: Optional[float] 
    originalQuoteCrypto: Optional[float] 
    expiresAt: Optional[datetime] 
    transactionHash: Optional[str] 
    lnInvoice: Optional[str] 

class CreatePaymentRequest(BaseModel):
    channelId: str
    amount: Optional[float] 
    # localAmount: Optional[float] 
    reason: PaymentReasons
    sequenceId: str
    sender: Sender
    destination: Destination
    # paymentReason: Optional[str] 
    # paymentCategory: Optional[str] 
    # incomeSource: Optional[str] 
    forceAccept: Optional[bool] 
    # customerType: Optional[CustomerType] 
    # widgetUserId: Optional[str] 
    directSettlement: Optional[bool] 
    # settlementInfo: Optional[PaymentSettlementInfo] 
    # attempt: Optional[int] 