import scrapy
from sreality.items import EstateItem

class SRealitySpider(scrapy.Spider):
    name = "sreality_spider"
    base_url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&per_page=50&page="

    def start_requests(self):
        # Генерируем URL'ы для запросов
        start_urls = [f"{self.base_url}{page}" for page in range(1, 11)]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.json()
        estates = data.get('_embedded', {}).get('estates', [])

        for estate_data in estates[:500]:
            item = EstateItem()
            item['hash_id'] = estate_data.get('hash_id')
            item['title'] = estate_data.get('name')
            item['price'] = estate_data.get('price')
            item['image_url'] = estate_data['_links']['images'][0]['href']
            yield item
