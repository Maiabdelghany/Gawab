
from datetime import datetime, date
from decimal import Decimal
from typing import Optional, Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field



# User Schemas

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8)
    role: str
    national_id: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    role: str
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    is_verified: bool
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)



# Donation Post Schemas

class DonationPostCreate(BaseModel):
    category: str
    title: str
    details: Optional[dict[str, Any]] = None
    photo_path: Optional[str] = None
    location: Optional[str] = None


class DonationPostResponse(BaseModel):
    id: int
    donor_id: int
    category: str
    title: str
    details: Optional[dict[str, Any]] = None
    photo_path: Optional[str] = None
    location: Optional[str] = None
    status: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Claim Schemas

class ClaimCreate(BaseModel):
    post_id: int


class ClaimResponse(BaseModel):
    id: int
    post_id: int
    charity_id: int
    status: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Campaign Schemas

class CampaignCreate(BaseModel):
    title: str
    category: Optional[str] = None
    description: Optional[str] = None
    goal: Decimal = Field(gt=0)
    deadline: Optional[date] = None


class CampaignResponse(BaseModel):
    id: int
    charity_id: int
    title: str
    category: Optional[str] = None
    description: Optional[str] = None
    goal: Decimal
    raised: Decimal
    deadline: Optional[date] = None
    status: str

    model_config = ConfigDict(from_attributes=True)


# Money Donation Schemas

class MoneyDonationCreate(BaseModel):
    campaign_id: int
    amount: Decimal = Field(gt=0)


class MoneyDonationResponse(BaseModel):
    id: int
    donor_id: int
    campaign_id: int
    amount: Decimal
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Volunteer Opportunity Schemas

class VolunteerOpportunityCreate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    needed: Optional[int] = Field(default=None, ge=0)
    when_text: Optional[str] = None
    location: Optional[str] = None


class VolunteerOpportunityResponse(BaseModel):
    id: int
    charity_id: int
    title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    needed: Optional[int] = None
    when_text: Optional[str] = None
    location: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# Volunteer Application Schemas

class VolunteerApplicationCreate(BaseModel):
    opportunity_id: Optional[int] = None
    date: Optional[date] = None
    hours: Optional[str] = None
    area: Optional[str] = None
    note: Optional[str] = None


class VolunteerApplicationResponse(BaseModel):
    id: int
    opportunity_id: Optional[int] = None
    volunteer_id: int
    date: Optional[date] = None
    hours: Optional[str] = None
    area: Optional[str] = None
    note: Optional[str] = None
    status: str

    model_config = ConfigDict(from_attributes=True)


# Announcement Schemas

class AnnouncementCreate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    campaign_id: Optional[int] = None
    needs: Optional[str] = None


class AnnouncementResponse(BaseModel):
    id: int
    charity_id: int
    title: Optional[str] = None
    message: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    campaign_id: Optional[int] = None
    needs: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)



# Notification Schemas

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: Optional[str] = None
    message: Optional[str] = None
    link: Optional[str] = None
    is_read: bool
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
