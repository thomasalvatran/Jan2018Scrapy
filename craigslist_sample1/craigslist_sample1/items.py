#!/usr/bin/Python2.7
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CraigslistSample1Item(Item):
    title = Field()
    link = Field()
