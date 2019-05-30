# -*- coding: utf-8 -*-
import scrapy

from alieni.items import AlieniItem

class UfoalieniSpider(scrapy.Spider):
    name = 'ufoalieni'
    allowed_domains = ['ufoalieni.it']
    start_urls = ['https://ufoalieni.it']

    def parseArticolo(self, response):
        ##print('parseArticolo----------------------->')
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        
        item = AlieniItem()
        item['page'] = page
        item['filename'] = filename
        item['title'] = response.css('h1.entry-title::text').get()
        item['subtitle'] = response.css('div.entry-content > h2::text').get()
        item['href'] = response.url

        content = ''
        for c in response.css('div.entry-content > p::text'):
            content += c.get()
        
        item['content'] = content
        item['datetime']  = ''
        item['img']  = ''
        #item['img'] = post.css('div.single-article > figure > a > img').xpath('@src').get()
        #item['datetime'] = post.css('time.entry-date').xpath('@datetime').get()
        
        #print(filename, titolo)
        yield(item)
        pass

    def parseHomePage(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        
        print ("filename %s" %filename)
        for post in response.css('div.first-post'):
            item = AlieniItem()
            item['page'] = page
            item['filename'] = filename
            item['href'] = post.css('div.single-article > figure > a').xpath('@href').get()
            item['title'] = post.css('div.single-article > figure > a').xpath('@title').get()
            item['img'] = post.css('div.single-article > figure > a > img').xpath('@src').get()
            item['datetime'] = post.css('time.entry-date').xpath('@datetime').get()
            #print (item['datetime'])
            yield(item)
        pass

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        
        if page:
            print("-------------------------->>>>>")
            #self.parseArticolo(response)
            item = AlieniItem()
            item['page'] = page
            item['filename'] = filename
            item['title'] = response.css('h1.entry-title::text').get()
            item['subtitle'] = response.css('div.entry-content > h2::text').get()
            item['href'] = response.url

            content = ''
            for c in response.css('div.entry-content > p::text'):
                content += c.get()
            
            item['content'] = content
           
            item['img'] = response.css('img.size-full,wp-image-6872,aligncenter').xpath('@src').get()
            item['datetime'] = response.css('time.entry-date').xpath('@datetime').get()
            
            #print(filename, titolo)
            yield(item)
        else:
            print ("------>>>>filename %s" %filename)
            for post in response.css('div.first-post'):
                next_page = post.css('div.single-article > figure > a').xpath('@href').get()

                if next_page is not None:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse)
        
        pass
