"""App config.
"""
import os

from dotenv import load_dotenv

load_dotenv()


# database
DB_DRIVER = os.environ.get("DB_DRIVER", "postgresql+psycopg2")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_NAME = os.environ.get("DB_NAME", "User")
# This is a postgresql specific paramter, https://www.postgresql.org/docs/9.1/libpq-ssl.html
DB_SSLMODE = os.environ.get("DB_SSLMODE", "disable")


