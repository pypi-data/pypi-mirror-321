from pydantic import BaseModel
from datetime import datetime


class Resource(BaseModel):
    id: str
    name: str
    status: str

class Sender(BaseModel):
    country: str
    address: str
    idType: str
    phone: str
    dob: str
    name: str
    idNumber: str
    email: str

class Destination(BaseModel):
    networkName: str
    networkId: str
    accountNumber: str
    accountName: str
    accountType: str

class Payment(BaseModel):
    partnerId: str
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