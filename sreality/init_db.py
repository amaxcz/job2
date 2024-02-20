from sqlalchemy import create_engine
from sreality.models import Base

DATABASE_URL = 'postgresql://demo1_user:demo1_pass@127.0.0.1:5432/demo1_db'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
