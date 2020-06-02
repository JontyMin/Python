# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/21 11:05
# 文件名称 ：spider.py
# 开发工具 ：PyCharm

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 定义爬虫名称
    allowed_domains = ['https://www.xicidaili.com/']  # 允许采集的域名
    # start_urls = ['https://www.xicidaili.com/nn/5']  # 开始采集网页
    start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1,3685)]  # 开始采集网页
    # custom_settings = None

    def parse(self, response):
        # 提取数据
        # 提取IP PORE
        selectors = response.xpath('//tr')  # 选择所有tr标签
        # 循环遍历标签下的td标签
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()  # . 在当前目录下继续选择
            port = selector.xpath('./td[3]/text()').get()
            # print(ip,port)
            # items={
            #     'ip':ip,
            #     'port':port
            # }
            # yield items

        # 翻页操作
        next_page= response.xpath('//a[@class="next_page"]/@href').get()
        print(next_page)
        if next_page:
            next_url = response.urljoin(next_page)
            # 回调
            yield scrapy.Request(next_url,callback=self.parse)



# 运行爬虫 命令行输入 scrapy crawl quotes


# 程序中启动爬虫
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('quotes')
    process.start()
