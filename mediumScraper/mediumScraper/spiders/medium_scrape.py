import scrapy
from mediumScraper.items import MediumscraperItem
from datetime import datetime
import re

class MediumScraper(scrapy.Spider):
	name = "my_scraper"
	base_url = 'https://medium.com/tag/data-science/archive/2018/01/'
	start_urls = []
	npages = 5

	for i in range(1, 2):
		if i < 10:
			day = "0"+str(i)
		else:
			day = str(i)
		start_urls.append(base_url+day+"")

	def parse(self, response):
		pathSet = set()
		xpaths = response.xpath("//div[contains(@class, 'streamItem streamItem--postPreview js-streamItem')]" +
			"/div[contains(@class, 'cardChromeless u-marginTop20 u-paddingTop10 u-paddingBottom15 u-paddingLeft20 u-paddingRight20')]"+
			"/div[contains(@class, 'postArticle postArticle--short js-postArticle js-trackedPost')]" +
			"/div/a//@href").extract()
		if len(xpaths) > 0:
			for url in xpaths:
				if url not in pathSet:
					pathSet.add(url)
					yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = MediumscraperItem()

		# Getting Article Title
		item['title'] = response.xpath("//meta[@property='og:title']/@content").extract()
		item['author'] = response.xpath("//meta[@property='author']/@content").extract()
		item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()
		item['author_url'] = response.xpath("//link[contains(@rel, 'author')]/@href").extract()


		yield item
