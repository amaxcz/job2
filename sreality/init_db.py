import os
from sqlalchemy import create_engine
from sreality.models import Base

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
else:
    print("DATABASE_URL not specified")
