from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

class StackSpider(Spider):
    name = 'stack'
    allowed_domains = ['capfriendly.com']
    start_urls = [
    'https://www.capfriendly.com/teams/sharks',
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="odd c"]')

        for question in questions:
            item = StackItem()
            item['name'] = question.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = question.xpath('td[@class="tm_yrr hide"]/text()').extract()[0]
            item['cont_19'] = question.xpath('td[7]/span[@class="cap rel mtv"]/span[@class="num"]/text()').extract()[0]
            yield item

        questions2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="even c"]')

        for question in questions2:
            item = StackItem()
            item['name'] = question.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = question.xpath('td[@class="tm_yrr hide"]/text()').extract()[0]
            item['cont_19'] = question.xpath('td[7]/span[@class="cap rel mtv"]/span[@class="num"]/text()').extract()[0]
            yield item
