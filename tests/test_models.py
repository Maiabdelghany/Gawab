
import sys
from pathlib import Path

PROJECT_ROOT = str(Path(__file__).resolve().parents[1])
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.Data import models
from src.Data.database import Base

MODEL_CLASSES = (
    models.User,
    models.DonationPost,
    models.Claim,
    models.Campaign,
    models.MoneyDonation,
    models.VolunteerOpportunity,
    models.VolunteerApplication,
    models.Announcement,
    models.Notification,
)

EXPECTED_MODEL_TABLES = {
    "users",
    "donation_posts",
    "claims",
    "campaigns",
    "money_donations",
    "volunteer_opportunities",
    "volunteer_applications",
    "announcements",
    "notifications",
}


def test_models_are_registered():
    assert {model.__tablename__ for model in MODEL_CLASSES} == EXPECTED_MODEL_TABLES
    assert set(Base.metadata.tables) == EXPECTED_MODEL_TABLES


if __name__ == "__main__":
    print("Models loaded successfully!")
    print("\nRegistered tables:")
    for table_name in Base.metadata.tables:
        print("-", table_name)
    print("\nTotal tables:", len(Base.metadata.tables))
