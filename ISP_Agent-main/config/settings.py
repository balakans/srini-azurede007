import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    # MySQL Individual Parameters
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

    # Reconstructed Connection String for SQLAlchemy
    @property
    def MYSQL_URI(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    # Pinecone Parameters
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_HOST = os.getenv("PINECONE_HOST")

    # Gemini Parameters
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-pro")

    @classmethod
    def validate(cls):
        """Ensure all required environment configurations are present."""
        instance = cls()
        required_vars = [
            "MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DB",
            "PINECONE_API_KEY", "PINECONE_HOST", "GOOGLE_API_KEY"
        ]

        missing = [var for var in required_vars if not os.getenv(var)]
        if missing:
            raise ValueError(f"Missing required environment configuration variables: {', '.join(missing)}")


# Validate configuration on import
Settings.validate()
settings = Settings()