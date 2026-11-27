
from schemas import UserCreate, UserLogin, CampaignCreate

user = UserCreate(
    name="Mai",
    email="mai@example.com",
    password="password123",
    role="donor"
)

print("User schema:", user.model_dump())

login = UserLogin(
    email="mai@example.com",
    password="password123"
)

print("Login schema:", login.model_dump())

campaign = CampaignCreate(
    title="Food Donation Campaign",
    goal=10000
)

print("Campaign schema:", campaign.model_dump())

print("\nAll schemas imported successfully!")
