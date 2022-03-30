from datetime import datetime
from database.conn import db_engine, db_metadata
from sqlalchemy import Table, Column, String, Integer, DateTime


# search_keyword = Table(
#     "search_keyword",
#     db_metadata,
#     Column("search_id", Integer, primary_key=True, autoincrement=True),
#     Column("user_id", Integer, nullable=True),
#     Column("search_keyw", String(255), nullable=True),
#     Column("create_date", DateTime(timezone=True), nullable=False, default=datetime.now)
# )
#
# search_keyword.metadata.create_all(db_engine)