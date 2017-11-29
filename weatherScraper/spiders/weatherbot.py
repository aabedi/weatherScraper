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
        global user_input
        user_input = InputData()
        user_input['code'] = code
        user_input['month'] = month
        user_input['day'] = day
        user_input['year'] = year

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formnumber=1,  # formnumber set to 1 because location and date are the second form on history page
            formdata={'code': user_input['code'],
                      'month': user_input['month'],
                      'day': user_input['day'],
                      'year': user_input['year']},
            callback=self.after_post
        )

    def after_post(self, response):
        # check input successful before moving on
        if "location you entered was not found" in response.body:
            self.logger.error("Location not valid")
            return
        temperatures = TempData()
        # Extract each temperature needed using corresponding css tags
        temperatures['actual_mean_temp'] = response.css('#historyTable tr:nth-child(2) .wx-value::text').extract()
        temperatures['avg_mean_temp'] = response.css('tr:nth-child(2) .indent~ td+ td .wx-value::text').extract()
        temperatures['actual_max_temp'] = response.css('tr:nth-child(3) .indent+ td .wx-value::text').extract()
        temperatures['avg_max_temp'] = response.css('#historyTable tr:nth-child(3) td:nth-child(3) .wx-value::text')\
            .extract()
        temperatures['record_max_temp'] = response.css('tr:nth-child(3) td:nth-child(4) .wx-value::text').extract()
        temperatures['actual_min_temp'] = response.css('tr:nth-child(4) .indent+ td .wx-value::text').extract()
        temperatures['avg_min_temp'] = response.css('#historyTable tr:nth-child(4) td:nth-child(3) .wx-value::text')\
            .extract()
        temperatures['record_min_temp'] = response.css('#historyTable tr:nth-child(4) td:nth-child(4) .wx-value::text')\
            .extract()
        # Check if Fahrenheit or Celsius, then append correct unit
        if 'C' in response.css('tr:nth-child(3) .indent+ td .wx-unit::text'):
            for key, value in temperatures.iteritems():
                value.append('C')
        else:
            for key, value in temperatures.iteritems():
                value.append('F')
        yield temperatures
