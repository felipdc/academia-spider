# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AcademiaItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    tags_number = scrapy.Field()
    link = scrapy.Field()
    pass
