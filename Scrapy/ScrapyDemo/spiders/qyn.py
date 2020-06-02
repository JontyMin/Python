# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/21 14:30
# 文件名称 ：qyn.py
# 开发工具 ：PyCharm

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "qynspider"  # 定义爬虫名称
    # allowed_domains = ['https://www.qidian.com/']  # 允许采集的域名
    # start_urls = ['https://read.qidian.com/chapter/kpwCq4fKJk01/LGKHGy9k73Q1']  # 开始采集网页
    # custom_settings = None

    urls = [
        'https://read.qidian.com/chapter/kpwCq4fKJk01/LGKHGy9k73Q1',
    ]

    def start_requests(self):
        for url in QuotesSpider.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        span = response.xpath('//h3[@class="j_chapterName"]/span[1]/text()').extract_first()

        content = response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract()
        content.insert(0, str(span))
        for c in content:
            with open('庆余年.txt', 'a') as f:
                c += '\r\n'
                # c = c.encode("utf-8")
                print(c)
                f.write(c)

        site = response.xpath('//*[@id="j_chapterNext"]/@href').extract_first()
        site = 'https:' + site
        print(site)
        yield response.follow(site, self.parse)


# 运行爬虫 命令行输入 scrapy crawl quotes


# 程序中启动爬虫
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('qynspider')
    process.start()
