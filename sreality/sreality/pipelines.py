from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Base, Estate


class SrealityPipeline:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        database_url = settings.get('DATABASE_URL')
        return cls(database_url)

    def process_item(self, item, spider):
        session = self.Session()

        try:
            estate = session.query(Estate).filter_by(hash_id=item['hash_id']).one_or_none()

            if estate:
                # Update existing object
                estate.title = item['title']
                estate.price = item['price']
                estate.image_url = item['image_url']
            else:
                # Create new object
                estate = Estate(
                    hash_id=item['hash_id'],
                    title=item['title'],
                    price=item['price'],
                    image_url=item['image_url']
                )

            session.add(estate)
            session.commit()

        except Exception as e:
            session.rollback()
            spider.log(f"Error saving/updating item to database: {e}")

        finally:
            session.close()

        return item
