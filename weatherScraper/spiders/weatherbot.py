# -*- coding: utf-8 -*-
from weatherScraper.items import TempData
import scrapy

class WeatherbotSpider(scrapy.Spider):
    name = 'weatherbot'
    allowed_domains = ['www.wunderground.com']
    start_urls = ['http://www.wunderground.com/history/']

    # def __init__(self, code='', month='', day='', year='',*args, **kwargs): # this will allow spider arguments
    #     super(WeatherbotSpider, self).__init__(*args, **kwargs)
    #     self.domain = domain

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formnumber=1, # formnumber set to 1 because location and date are the second form on history page
            formdata = {'code': 'hnd', 'month': '11', 'day': '7', 'year': '1994'},
            # formdata={'code': code, 'month': month, 'day': day, 'year': year},
            # clickdata = { "type": "submit" },
            callback = self.after_post
        )
        # return request

    def after_post(self, response):
        # check input successful before moving on
        if "location you entered was not found" in response.body:
            self.logger.error("Location not valid")
            return
        # only want first 8 of these numbers. use loop
        temperatures = TempData()
        temperatures['temperature'] = []
        for temp in response.css(".wx-value , tr:nth-child(2) .indent+ td"):
            temperatures['temperature'].append(temp.css('::text').extract())
        yield temperatures

        # return response.css(".wx-value , tr:nth-child(2) .indent+ td").extract()

