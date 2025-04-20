# app/database.py
from databases import Database

DATABASE_URL = "postgresql://neondb_owner:npg_7kae4ChSvljo@ep-hidden-mountain-a437vuvq-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

database = Database(DATABASE_URL)
