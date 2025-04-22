from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_7kae4ChSvljo@ep-hidden-mountain-a437vuvq-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

# For async queries (databases package)
database = Database(DATABASE_URL)

# For SQLAlchemy model declarations
Base = declarative_base()

# Optional: Engine and SessionLocal if you need SQLAlchemy sessions
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
