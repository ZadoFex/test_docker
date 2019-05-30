# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlieniItem(scrapy.Item):
    # define the fields for your item here like:
    page = scrapy.Field()
    filename = scrapy.Field()

    href = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    datetime = scrapy.Field()

    subtitle = scrapy.Field()
    content  = scrapy.Field()
