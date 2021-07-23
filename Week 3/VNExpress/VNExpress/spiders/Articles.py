import scrapy
from scrapy.http import Request
from VNExpress.items import VnexpressItem

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['vnexpress.net']
    start_urls = ['http://vnexpress.net/']

    def start_requests(self):
        url = "https://vnexpress.net/suc-khoe-p{}"
        link_urls = [url.format(i) for i in range(1,500)]
        for link_url in link_urls:
            print(link_url)
            request=Request(link_url, cookies={'store_language':'en'}, callback=self.parse_main_pages)
            yield request

    def parse_main_pages(self,response):
        item=VnexpressItem()
        content=response.xpath('//article//div[@class="thumb-art"]')
        for article_link in content.xpath('.//a'):
            item['article_url'] = article_link.xpath('.//@href').extract_first()
        yield(item)

    def parse(self, response):
        pass
