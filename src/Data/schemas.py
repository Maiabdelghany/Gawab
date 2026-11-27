
from datetime import date as Date
from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field

# User Schemas

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8)
    role: str
    national_id: str | None = None
    phone: str | None = None
    address: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    role: str
    name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None
    is_verified: bool
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)



# Donation Post Schemas

class DonationPostCreate(BaseModel):
    category: str
    title: str
    details: dict[str, Any] | None = None
    photo_path: str | None = None
    location: str | None = None


class DonationPostResponse(BaseModel):
    id: int
    donor_id: int
    category: str
    title: str
    details: dict[str, Any] | None = None
    photo_path: str | None = None
    location: str | None = None
    status: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


# Claim Schemas

class ClaimCreate(BaseModel):
    post_id: int


class ClaimResponse(BaseModel):
    id: int
    post_id: int
    charity_id: int
    status: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


# Campaign Schemas

class CampaignCreate(BaseModel):
    title: str
    category: str | None = None
    description: str | None = None
    goal: Decimal = Field(gt=0)
    deadline: Date | None = None


class CampaignResponse(BaseModel):
    id: int
    charity_id: int
    title: str
    category: str | None = None
    description: str | None = None
    goal: Decimal
    raised: Decimal
    deadline: Date | None = None
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
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


# Volunteer Opportunity Schemas

class VolunteerOpportunityCreate(BaseModel):
    title: str | None = None
    category: str | None = None
    description: str | None = None
    needed: int | None = Field(default=None, ge=0)
    when_text: str | None = None
    location: str | None = None


class VolunteerOpportunityResponse(BaseModel):
    id: int
    charity_id: int
    title: str | None = None
    category: str | None = None
    description: str | None = None
    needed: int | None = None
    when_text: str | None = None
    location: str | None = None

    model_config = ConfigDict(from_attributes=True)


# Volunteer Application Schemas

class VolunteerApplicationCreate(BaseModel):
    opportunity_id: int | None = None
    date: Date | None = None
    hours: str | None = None
    area: str | None = None
    note: str | None = None


class VolunteerApplicationResponse(BaseModel):
    id: int
    opportunity_id: int | None = None
    volunteer_id: int
    date: Date | None = None
    hours: str | None = None
    area: str | None = None
    note: str | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)


# Announcement Schemas

class AnnouncementCreate(BaseModel):
    title: str | None = None
    message: str | None = None
    event_date: Date | None = None
    location: str | None = None
    campaign_id: int | None = None
    needs: str | None = None


class AnnouncementResponse(BaseModel):
    id: int
    charity_id: int
    title: str | None = None
    message: str | None = None
    event_date: Date | None = None
    location: str | None = None
    campaign_id: int | None = None
    needs: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)



# Notification Schemas

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str | None = None
    message: str | None = None
    link: str | None = None
    is_read: bool
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
