# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from tutorial.items import TutorialItem


class RietilifeSpider(scrapy.Spider):
    name = 'rietilife'
    allowed_domains = ['rietilife.com']
    start_urls = ['http://rietilife.com/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
       
        item = TutorialItem()
        item['title'] = response.css('title::text').getall()
        questions = response.css('a::attr(href)').getall()
        for question in questions:
            self.log("Qui dentro")
            self.log("CC", question) 

        #clear
        # yield item

        #title = response.css('title::text').getall()
        #self.log('Filename %s, title %s ' % (filename, title))
        #print(title)
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
