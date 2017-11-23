# -*- coding: utf-8 -*-
import scrapy


class WeatherbotSpider(scrapy.Spider):
    name = 'weatherbot'
    allowed_domains = ['www.wunderground.com/history']
    start_urls = ['http://www.wunderground.com/history/']

    # def __init__(self, code='', month='', day='', year='',*args, **kwargs): # this will allow spider arguments 
    #     super(WeatherbotSpider, self).__init__(*args, **kwargs)
    #     self.domain = domain

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formnumber=1, # formnumber set to 1 because location and date are the second form on history page
            formdata={'code': 'hnd', 'month': 'November', 'day': '7', 'year': '1994'},
            # formdata={'code': code, 'month': month, 'day': day, 'year': year},
            clickdata = { "type": "Submit" },
            callback=self.after_post
        )

    def after_post(self, response):
        # check input successful before moving on
        if "location you entered was not found" in response.body:
            self.logger.error("Location not valid")
            return
        # only want first 8 of these numbers. use loop
        return response.css(".wx-value , tr:nth-child(2) .indent+ td").extract()

