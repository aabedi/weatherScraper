# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TempData(scrapy.Item):
    actual_mean_temp = scrapy.Field()
    avg_mean_temp = scrapy.Field()
    actual_max_temp = scrapy.Field()
    avg_max_temp = scrapy.Field()
    record_max_temp = scrapy.Field()
    actual_min_temp = scrapy.Field()
    avg_min_temp = scrapy.Field()
    record_min_temp = scrapy.Field()


class InputData(scrapy.Item):
    code = scrapy.Field()   # location. airport or city code
    month = scrapy.Field()  # month, a number b/w 1 and 12 inclusive
    day = scrapy.Field()    # day, a number b/w 1 and 31 inclusive (february ends at 29?)
    year = scrapy.Field()   # year, a 4 digit number (how far back is valid?)