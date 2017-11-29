# weatherScraper
weatherScraper is a web scraper built with Scrapy. It takes in a city, month, day, and year and 
outputs historical temperature values in JSON format. Scrapes from the weatherunderground website.

## Instructions for use
### Pre-boot configuration
* git clone repository
* pip install Scrapy

### Start up
* cd weatherScraper
* scrapy crawl  weatherbot -a code=hnd -a month=11 -a day=7 -a year=2017 -o outputData.json
* modify the above command's input arguments for desired airport/city code, month, day, and year.
* you can also modify the output argument. default is outputData.json

###Output Example:
`[
 {"actual_min_temp": ["55", "F"], "avg_max_temp": ["57", "F"], "actual_mean_temp": ["63", "F"], "avg_min_temp": ["47", "F"], "actual_max_temp": ["71", "F"], "record_max_temp": ["75", "F"], "record_min_temp": ["46", "F"], "avg_mean_temp": ["F"]}
 ]` 



