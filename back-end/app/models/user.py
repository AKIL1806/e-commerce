from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("password", String, nullable=False),
    Column("Mobile",String, nullable=False),
)
