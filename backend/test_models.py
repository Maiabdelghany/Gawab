
from models import (
    User,
    DonationPost,
    Claim,
    Campaign,
    MoneyDonation,
    VolunteerOpportunity,
    VolunteerApplication,
    Announcement,
    Notification,
)

from database import Base

print("Models loaded successfully!")

print("\nRegistered tables:")

for table_name in Base.metadata.tables:
    print("-", table_name)

print("\nTotal tables:", len(Base.metadata.tables))
