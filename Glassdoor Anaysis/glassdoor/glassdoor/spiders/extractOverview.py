# -*- coding: utf-8 -*-
import scrapy


class ExtractoverviewSpider(scrapy.Spider):
    name = 'extractOverview'

    def start_requests(self):
        urls = ['https://www.glassdoor.co.in/Reviews/company-reviews.htm/']
        tag = getattr(self, 'companyName', None)
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0'
        data={'sc.keyword':companyName}
        link="https://www.glassdoor.co.in/Reviews/company-reviews.htm"
        response = s.post(link, data=data)
        print(response.url)
        yield scrapy.Request(url=url,method='POST',body=data,callback=self.parse)


    def parse(self, response):
        print("ghh")
