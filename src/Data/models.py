
from sqlalchemy import (
    DECIMAL,
    JSON,
    TIMESTAMP,
    Boolean,
    Column,
    Date,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    text,
)

from .database import Base


# 1. Users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(Enum("donor", "charity", "admin"), nullable=False)
    name = Column(String(120), nullable=False)
    national_id = Column(String(14), nullable=True)
    phone = Column(String(20))
    address = Column(String(255))
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_verified = Column(Boolean, server_default=text("0"))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# 2. Donation Posts
class DonationPost(Base):
    __tablename__ = "donation_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    donor_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(30), nullable=False)
    title = Column(String(150), nullable=False)
    details = Column(JSON)
    photo_path = Column(String(255))
    location = Column(String(255))
    status = Column(
        Enum("Draft", "Available", "Claimed", "Accepted"),
        server_default=text("'Available'")
    )
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# 3. Claims
class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("donation_posts.id", ondelete="CASCADE"), nullable=False)
    charity_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status = Column(
        Enum("Claimed", "Accepted", "Rejected"),
        server_default=text("'Claimed'")
    )
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# 4. Campaigns
class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    charity_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150), nullable=False)
    category = Column(String(30))
    description = Column(Text)
    goal = Column(DECIMAL(12, 2), nullable=False)
    raised = Column(DECIMAL(12, 2), server_default=text("0"))
    deadline = Column(Date)
    status = Column(
        Enum("Pending approval", "Active", "Rejected"),
        server_default=text("'Pending approval'")
    )


# 5. Money Donations
class MoneyDonation(Base):
    __tablename__ = "money_donations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    donor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    amount = Column(DECIMAL(12, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# 6. Volunteer Opportunities
class VolunteerOpportunity(Base):
    __tablename__ = "volunteer_opportunities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    charity_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150))
    category = Column(String(30))
    description = Column(Text)
    needed = Column(Integer)
    when_text = Column(String(100))
    location = Column(String(255))


# 7. Volunteer Applications
class VolunteerApplication(Base):
    __tablename__ = "volunteer_applications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    opportunity_id = Column(
        Integer,
        ForeignKey("volunteer_opportunities.id", ondelete="CASCADE"),
        nullable=True
    )
    volunteer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date)
    hours = Column(String(30))
    area = Column(String(255))
    note = Column(Text)
    status = Column(
        Enum("Pending", "Accepted", "Rejected"),
        server_default=text("'Pending'")
    )


# 8. Announcements
class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    charity_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150))
    message = Column(Text)
    event_date = Column(Date)
    location = Column(String(255))
    campaign_id = Column(Integer)
    needs = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


# 9. Notifications
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(150))
    message = Column(String(255))
    link = Column(String(50))
    is_read = Column(Boolean, server_default=text("0"))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
