# -*- coding: utf-8 -*-
import scrapy


class PfgSpider(scrapy.Spider):
    name = 'pfg'
    allowed_domains = ['www.glassdoor.co.in/Benefits/Principal-Financial-Group-Health-Care-and-Insurance-India-BNFT104_E2941_N115.ht']
    start_urls = ['https://www.glassdoor.co.in/Benefits/Principal-Financial-Group-Health-Care-and-Insurance-India-BNFT104_E2941_N115.htm']

    def parse(self, response):
        description=response.css(".description::text").extract()
        print(description)
        count=response.css(".minor::text").extract_first()
        rating=response.css(".h1::text").extract()
        Other_info = {
                'Number Of Employees' : count,
                'Overall Rating' : rating[1],
            }
        #yield Other_info
        for item in description:
            print("gfh",item)
            #create a dictionary to store the scraped info
            scraped_info = {
                'Insurance review' : item,
            }
            yield scraped_info

