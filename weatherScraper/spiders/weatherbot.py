# -*- coding: utf-8 -*-
from weatherScraper.items import TempData
from weatherScraper.items import InputData
import scrapy

class WeatherbotSpider(scrapy.Spider):
    name = 'weatherbot'
    allowed_domains = ['www.wunderground.com']
    start_urls = ['http://www.wunderground.com/history/']


    def __init__(self, code='', month='', day='', year='', *args, **kwargs): # this will allow spider arguments
        super(WeatherbotSpider, self).__init__(*args, **kwargs)
        # self.code = code
        # self.month = month
        # self.day = day
        # self.year = year
        global user_input
        user_input = InputData()
        user_input['code'] = code
        user_input['month'] = month
        user_input['day'] = day
        user_input['year'] = year

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formnumber=1, # formnumber set to 1 because location and date are the second form on history page
            # formdata = {'code': 'hnd', 'month': '11', 'day': '7', 'year': '2017'},
            formdata={'code': user_input['code'], 'month': user_input['month'], 'day': user_input['day'], 'year': user_input['year']},
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
            # can add label field in item, append here
            temperatures['temperature'].append(temp.css('::text').extract())
            # temperatures['temperature'].append(temp.extract())
        yield temperatures

        # return response.css(".wx-value , tr:nth-child(2) .indent+ td").extract()

        # F or C? might want to parse unit in case it swiches

        # scrapy runspider weatherbot.py -a code=hnd -a month=11 -a day=7 -a year=2017




