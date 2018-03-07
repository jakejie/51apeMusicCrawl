# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 歌曲名
    names = scrapy.Field()  # 歌曲名
    area = scrapy.Field()  # 所属分类
    form = scrapy.Field()  # 来源
    types = scrapy.Field()  # 音质类型
    length = scrapy.Field()  # 长度
    language = scrapy.Field()  # 语言
    data_time = scrapy.Field()  # 更新时间
    baidu_url = scrapy.Field()  # 网盘链接
    baidu_se = scrapy.Field()  # 网盘密码
    url = scrapy.Field()  # 来源链接
    music_info = scrapy.Field()  # 歌词
    words = scrapy.Field()  # 作词
    music = scrapy.Field()  # 作曲
