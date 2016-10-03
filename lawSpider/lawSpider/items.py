# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LawSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topicNum = scrapy.Field()
    topic = scrapy.Field()
    topicDesc = scrapy.Field()

    question = scrapy.Field()
    answer = scrapy.Field()
