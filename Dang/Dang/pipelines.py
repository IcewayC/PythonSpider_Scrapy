# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangPipeline(object):
    def process_item(self, item, spider):
        name = item['title'][0]
        comment_num = item['comment_num'][0]
        link = item['link']
        price = item['price'][0]
        img_url = item['img_url'][0]

        print u'商品名：' + name
        print u'商品评论数：' + comment_num
        print u'商品详情页：' + link
        print u'商品价格：' + price
        print u'商品图片链接：' + img_url
        print '-----------'

        return item
