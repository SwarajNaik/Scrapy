from pathlib import Path
import pandas as pd
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "burnmaker"

    def start_requests(self):
        urls = [
            "https://makerburn.com/#/"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        table = response.xpath("/html/body")
        
        print(table.get())
        
        # rows = table.xpath("//tbody/tr")
        # print(len(rows))
        # for row in rows:
        #     print(len(rows))
        #     print(row)#.xpath('.//td[1]/div[1]/text()').get())
        
        
        # pass