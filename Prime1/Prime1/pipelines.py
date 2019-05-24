# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class Prime1Pipeline(object):
	def process_item(self, item, spider):
		os.chdir('F:/Prime1')

		if item['images'][0]['path']:
			new_image_name = item['title'][0] + '.jpg'
			new_image_path = 'full/' + new_image_name

			os.rename(item['images'][0]['path'], new_image_path)


 
