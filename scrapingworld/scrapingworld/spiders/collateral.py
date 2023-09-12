import scrapy


class CollateralSpider(scrapy.Spider):
    name = "collateral"

    def start_requests(self):
        urls = [
            "https://makerburn.com/#/rundown"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        table = response.xpath("/html/body/div[1]/main/div[2]/section[1]/table")
        rows = table.xpath("//tbody/tr")
        
        for row in rows:
            print(row.xpath('.//td[1]/div[1]/text()').get())
