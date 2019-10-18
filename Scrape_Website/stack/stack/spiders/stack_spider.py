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
        forward1 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="odd c"]')
        forward2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="even c"]')

        for forward in forward1:
            item = StackItem()
            item['name'] = forward.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = forward.xpath('td[@class="tm_yrr hide"]/text()').extract()[0]
            item['cont_19'] = forward.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item

        #questions2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="even c"]')
        #questions2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[1]/tr[@class="even c"]')

        for forward in forward2:
            item = StackItem()
            item['name'] = forward.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = forward.xpath('td[@class="tm_yrr hide"]/text()').extract()[0]
            item['cont_19'] = forward.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item

        defense1 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[2]/tr[@class="odd c"]')
        defense2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[2]/tr[@class="even c"]')

        for defd in defense1:
            item = StackItem()
            item['name'] = defd.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = defd.xpath('td[@class="left"]/a/text()').extract()[0]
            item['cont_19'] = defd.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item

        for defd in defense2:
            item = StackItem()
            item['name'] = defd.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = defd.xpath('td[@class="left"]/a/text()').extract()[0]
            item['cont_19'] = defd.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item

        goalie1 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[3]/tr[@class="odd c"]')
        goalie2 = Selector(response).xpath('//div[@class="cb team_c"]/table[@class="tbl fixed"]/tbody[3]/tr[@class="even c"]')

        for goal in goalie1:
            item = StackItem()
            item['name'] = goal.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = goal.xpath('td[@class="left"]/a/text()').extract()[0]
            item['cont_19'] = goal.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item

        for goal in goalie2:
            item = StackItem()
            item['name'] = goal.xpath('td[@class="left"]/a/text()').extract()[0]
            item['yrs_rem'] = goal.xpath('td[@class="left"]/a/text()').extract()[0]
            item['cont_19'] = goal.xpath('td[7]/span[1]/span[@class="num"]/@data-num').extract()[0]
            yield item
