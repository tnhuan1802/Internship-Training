# Spider 2
# ArticleScraper.py which scrape article headlies and bodies
# imports
import scrapy
from scrapy.http import Request
from VNExpress.items import VnexpressItem

import json
class ArticlescraperSpider(scrapy.Spider):
    name = 'ArticleScraper'
    allowed_domains = ['vnexpress.net']
    start_urls = ['http://vnexpress.net/']
    def start_requests(self):
    
    # Open the JSON file which contains article links
        with open('C:/Users/zPtsK/OneDrive/Desktop/New folder/Internship-Training/Week 3/VNExpress/article_links.json') as json_file:
            data = json.load(json_file)
        for p in data:
            # print('URL: ' + p['article_url'])
    # Request to get the HTML content
            request=Request(p['article_url'],
                            cookies={'store_language':'en'},
                            callback=self.parse_article_page)
            yield request
    def parse_article_page(self,response):
        item=VnexpressItem()
        a_body=""
        # Extracts the article_title and stores in scrapy item
        item['article_title']=response.xpath('//h1[@class="title-detail"]/text()').extract();
        item['article_title'] = item['article_title'][0]
        # Extracts the article_body in <p> elements
        for p in response.xpath('//article[@class="fck_detail "]//p/text()').extract():
            a_body=a_body+p
            item['article_body']= a_body
        yield(item)

    def parse(self, response):
        pass