import scrapy
from mediumScraper.items import MediumscraperItem

class MediumScraper(scrapy.Spider):
	name = "my_scraper"

	def __init__(self, tag='datescience', date='2018/08/16'):
		self.tag = tag
		self.date = date
		self.start_urls = ['https://medium.com/tag/{tag}/archive/{date}'.format(tag=tag, date=date)]

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

		item['title'] = response.xpath("//meta[@property='og:title']/@content").extract()
		item['publish_time'] = response.xpath("//meta[@property='article:published_time']/@content").extract()
		item['author'] = response.xpath("//meta[@property='author']/@content").extract()
		item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()
		item['author_url'] = response.xpath("//link[contains(@rel, 'author')]/@href").extract()
		item['headings'] = response.xpath("//*[self::h1 or self::h2 or self::h3]/text()").extract()
		item['contents'] = response.xpath("//p/descendant::text()").extract()
		item['mins_read'] = response.xpath("//meta[@name='twitter:data1']/@value").extract()
		item['claps'] = response.xpath("//aside[contains(@class, 'u-marginAuto u-maxWidth1000 js-postLeftSidebar')]//ul/li/div[contains(@class, 'multirecommend js-actionMultirecommend u-flexColumn u-marginBottom10 u-width60')]/span/button/text()").extract()
		item['lang'] = response.xpath("//main/article/@lang").extract()
		item['tag'] = self.tag
		yield item
