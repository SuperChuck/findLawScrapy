#encoding=utf-8
import scrapy
import codecs
import chardet
import os

from lawSpider.items import LawSpiderItem

class LawSpider(scrapy.Spider):
    name = 'lawSpider'
    allowed_domains = ['china.findlaw.cn']
    start_urls = ['http://china.findlaw.cn/mdm/?p=1']

    def parse(self, response):
	for sel in response.xpath('//div[@class="mdm-zj-left"]')[0]:
	    
            topicNum = sel.xpath('div[@class="mdm-zj-ico"]/div[@class="mdm-zj-ico-btn"]/span/text()').extract()[0].encode('utf-8')
            topicPath = './data/' + str(topicNum)
            if not os.path.exists(topicPath):
                os.mkdir( topicPath )
            
            topicLink = sel.xpath('dl/dd/h3/a/@href').extract()[0].encode('utf-8')
            if topicLink:
	        yield scrapy.Request(topicLink, callback=self.parse_QandA)
            #read content page
            #read following page

            #item['topic'] = sel.xpath('dl/dd/h3/a/text()').extract()[0]
        ''' 
        nextPage = response.xpath('//div[@class="Paging"]/a')[-1]
        nextUrl = nextPage.xpath('@href').extract()[0]
        if nextUrl:
	   yield scrapy.Request(nextUrl, callback=self.parse)
        '''
    def parse_QandA(self, response):
        for sel in response.xpath('//ul[@class="mdm-tw-list-border"]'):
	    item = LawSpiderItem()
            item['topic'] = response.xpath('//li[@class="title-txt"]/h3/a/text()').extract()
            item['topicNum'] = response.xpath('//li[@class="title-txt"]/span/text()').extract()
	    item['topicDesc'] = response.xpath('//div[@class="suggest"]/p/text()').extract()
            item['question'] =  sel.xpath('//li')[0].xpath('//dd[@class="tw-bg"]/p/text()').extract()
	    item['answer'] = sel.xpath('//li')[1].xpath('//dd[@class="tw-bg2"]/p/text()').extract()
	    yield item
	'''
	nextPage = response.xpath('//div[@class="Paging"]/a')[-1]
	nextUrl = nextPage.xpath('@href').extract()[0]
	if nextUrl:
	    yield scrapy.Request(nextUrl, callback=self.parse_QandA)
	'''     
	    
