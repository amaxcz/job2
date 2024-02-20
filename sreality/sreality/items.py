import scrapy

class EstateItem(scrapy.Item):
    hash_id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()


