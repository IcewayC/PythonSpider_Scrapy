import scrapy
from Dang.items import DangItem
from scrapy.http import Request


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domins = ['dangdang.com']
    start_urls = ['http://3c.dangdang.com/pc']

    def parse(self, response):
        category = response.xpath('//div[@class="level_one "]/dl/dd/a/@href').extract()
        # print category
        for url in category:
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        link = response.xpath('//a[@class="pic"]/@href').extract()
        next_link = response.xpath('//li[@class="next"]/a/@href')[0].extract()
        if next_link:
            yield Request('http://category.dangdang.com/'+next_link, callback=self.parse_detail)

        for detail_url in link:
            yield Request(detail_url, callback=self.parse_price)

    def parse_price(self, response):
        item = DangItem()
        item['title'] = response.xpath('//div[@class="name_info"]/h1/@title').extract()
        item['comment_num'] = response.xpath('//a[@id="comm_num_down"]/text()').extract()
        item['link'] = response.url
        item['price'] = response.xpath('//p[@id="dd-price"]/text()').extract()
        item['img_url'] = response.xpath('//img[@id="modalBigImg"]/@src').extract()

        yield item
