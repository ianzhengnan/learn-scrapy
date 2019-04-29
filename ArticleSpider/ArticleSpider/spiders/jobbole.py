# -*- coding: utf-8 -*-
import scrapy
import re

# 1~3->35:09
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114641/']

    def parse(self, response):
        # chrome: //*[@id="post-114605"]/div[1]/h1
        # firefox: /html/body/div[1]/div[3]/div[1]/div[1]/h1
        # re_selector = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        # re2_selector = response.xpath('//*[@id="post-114605"]/div[1]/h1/text()')

        title = response.xpath('//*[@class="entry-header"]/h1/text()').extract()[0]
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        # 获取点赞数
        vote_number = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        # 获取收藏数
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        # 获取收藏数
        comments_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(".*(\d+).*", comments_nums)
        if match_re:
            comments_nums = match_re.group(1)

        content = response.xpath("//div[@class='entry']").extract()[0]

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)

        pass
