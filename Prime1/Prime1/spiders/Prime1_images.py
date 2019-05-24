# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Prime1.items import Prime1Item


class Prime1ImagesSpider(Spider):
    name = 'Prime1_images'
    allowed_domains = ['prime1studio.com/new-products.html']
    start_urls = ['http://prime1studio.com/new-products.html/']

    def parse(self, response):
    	Figures = response.xpath('//*[@class = "c-card"]/a/@href').extract()
    	for figure in Figures:
    		Link = response.urljoin(figure)
    		yield Request(Link,callback = self.parse_Figures,dont_filter = True)

    def parse_Figures(self,response):
    	I = ItemLoader(item = Prime1Item(),response=response)

    	image_urls = response.xpath('//*[@id = "image"]/@src').extract_first()
    	title = response.xpath('//*[@class = "product"]/strong/text()').extract_first()

    	I.add_value('image_urls',image_urls)
    	I.add_value('title',title)

    	return I.load_item()

