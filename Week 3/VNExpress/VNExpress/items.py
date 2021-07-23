from scrapy.item import Item, Field


class VnexpressItem(Item):
    article_url = Field() 
    article_title = Field()
    article_description = Field() 
    article_body = Field()
