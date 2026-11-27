
import sys
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = str(Path(__file__).resolve().parents[1])
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.Data.database import DB_NAME, engine


def test_database_connection():
    with engine.connect() as connection:
        assert connection.execute(text("SELECT 1")).scalar_one() == 1
        assert connection.execute(text("SELECT DATABASE()")).scalar_one() == DB_NAME


if __name__ == "__main__":
    test_database_connection()
    print(f"Database connected successfully: {DB_NAME}")
