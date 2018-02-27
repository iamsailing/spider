# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['read.douban.com']
    # start_urls = ['https://read.douban.com/']

    def start_requests(self):
        url = 'https://read.douban.com/kind/185'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        info_list = response.xpath('//div[@class="info"]')
        # print(info_list)

        for info in info_list:
            item = DoubanbookItem()
            item['title'] = info.xpath('.//div[@class="title"]/a/text()').extract_first()
            item['author'] = info.xpath('.//span[1]/span[2]/a/text()').extract_first()
            item['category'] = info.xpath('.//span[@itemprop="genre"]/text()').extract_first()
            item['rate'] = info.xpath('.//span[@class="rating-average"]/text()').extract_first()
            item['count'] = info.xpath('.//a[@class="ratings-link"]/span/text()').extract_first()
            item['brief'] = info.xpath('.//div[@class="article-desc-brief"]/text()').extract_first()
            yield item

        next_temp_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_temp_url:
            next_url = response.urljoin(next_temp_url)
            yield scrapy.Request(next_url,callback=self.parse)


