# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from musicape.items import MusicapeItem
import re


class ApecrawlSpider(CrawlSpider):
    name = 'apecrawl'
    allowed_domains = ['www.zsczys.com']
    start_urls = ['http://51ape.com/']
    # start_urls = ['https://www.zsczys.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhuanji/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'zhuanji/'), follow=True),
        Rule(LinkExtractor(allow=r'/ape/[0-9]{1,10}.html'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/Play/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/ConTent/'), follow=True),
        # Rule(LinkExtractor(allow=r'/Classify/'), follow=True),
        # Rule(LinkExtractor(allow=r'm=vod-list-id'), follow=True),
    )

    def parse_item(self, response):
        # i = {}
        item = MusicapeItem()
        # print("地址：{}".format(response.url))
        # com = re.compile(r'"http://.*?\.mp4')
        # u = re.findall(com, response.text)
        # print(u)

        # com = re.compile(r'href="thunder://.*?">')
        # hre = re.findall(com, response.text)
        # print(hre)
        # down = response.xpath('//*[@id="downul"]/li/a/href').extract()
        # name = response.xpath('//*[@id="downul"]/li/font/text()').extract()

        # print(down,name)

        item["name"] = response.xpath('/html/body/div[1]/div/div[6]/h1/text()')[0].extract()  # 歌曲名
        item["names"] = response.xpath('/html/body/div[1]/div/div[6]/ul/li[5]/text()')[0].extract()
        item["area"] = response.xpath('//div[@class="fl over w638"]/ul/li[3]/a/text()')[0].extract()  # 所属分类
        if item["area"] == "":
            item["area"] = response.xpath('//div[@class="fl over w638"]/ul/li[3]/a/@title')[0].extract()  # 所属分类
        item["form"] = response.xpath('/html/body/div[1]/div/div[6]/h3[1]/text()')[0].extract()  # 选自 来源
        item["types"] = response.xpath('/html/body/div[1]/div/div[6]/h3[2]/text()')[0].extract()  # 音质类型
        item["length"] = response.xpath('/html/body/div[1]/div/div[6]/h3[3]/text()')[0].extract()  # 文件的大小
        item["language"] = response.xpath('/html/body/div[1]/div/div[6]/h3[4]/text()')[0].extract()  # 语言
        item["data_time"] = response.xpath('/html/body/div[1]/div/div[6]/h3[5]/text()')[0].extract()  # 更新时间
        item["baidu_url"] = response.xpath('/html/body/div[1]/div/div[6]/a/@href')[0].extract()  # 网盘链接
        item["baidu_se"] = response.xpath('/html/body/div[1]/div/div[6]/b/text()')[1].extract()  # 网盘提取密码
        item["words"] = response.xpath('//*[@id="newstext_2"]/h3[1]/a/text()')[0].extract()  #
        item["music"] = response.xpath('//*[@id="newstext_2"]/h3[2]/a/text()')[0].extract()
        item["music_info"] = "\n".join(response.xpath('//*[@id="newstext_2"]/p').extract())
        item["url"] = response.url

        return item


"""
name = response.xpath('/html/body/div[1]/div/div[6]/h1/text()')
form = response.xpath('/html/body/div[1]/div/div[6]/h3[1]/text()').extract()
types = response.xpath('/html/body/div[1]/div/div[6]/h3[2]/text()').extract()
length = response.xpath('/html/body/div[1]/div/div[6]/h3[3]/text()').extract()
language = response.xpath('/html/body/div[1]/div/div[6]/h3[4]/text()').extract()
data_time = response.xpath('/html/body/div[1]/div/div[6]/h3[5]/text()').extract()
baidu_url = response.xpath('/html/body/div[1]/div/div[6]/a/@href').extract()
baidu_se = response.xpath('/html/body/div[1]/div/div[6]/b/text()').extract()
print(name, form, types, length, language, data_time, baidu_url, baidu_se, url, )
"""
