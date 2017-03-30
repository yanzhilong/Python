# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SooxieItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()  # 网址
    title = scrapy.Field()  # 标题
    shoeno = scrapy.Field()  # 货号
    price = scrapy.Field()  # 价格
    popularity = scrapy.Field()  # 人气
    update = scrapy.Field()  # 更新时间
    sizes = scrapy.Field()  # 尺码
    colors = scrapy.Field()  # 颜色
    images = scrapy.Field()  # 图片链接地址
    property = scrapy.Field()  # 属性
    market = scrapy.Field()  # 市场





