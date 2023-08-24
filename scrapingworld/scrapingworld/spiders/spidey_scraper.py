from pathlib import Path
import pandas as pd
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "scrapingworld"

    def start_requests(self):
        urls = [
            "http://www.worldgovernmentbonds.com/spread-historical-data/"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath("/html/body/div[1]/div[2]/div/article/div/div/div/div/div[2]/div[4]/table")
        rows = table.xpath("//tbody/tr")
        
        country_ = []
        yeild_ = []
        germany_ = []
        usa_ = []
        china_ = []
        aus_ = []
        last_upadated_ = []
        
        for row in rows:
            country = row.xpath("./td[2]/a/b/text()").get()
            yeild = row.xpath("./td[3]/a/b/text()").get()
            germany = row.xpath("./td[5]/a/b/text()").get()
            usa = row.xpath("./td[6]/a/b/text()").get()
            china = row.xpath("./td[7]/a/b/text()").get()
            aus = row.xpath("./td[8]/a/b/text()").get()
            last_updated = row.xpath("/html/body/div[1]/div[2]/div/article/div/div/div/div/div[2]/p[6]/text()").get()
            if  yeild == None:
                yeild = row.xpath("./td[3]/b/text()").get()
                germany = row.xpath("./td[5]/b/text()").get()
                usa = row.xpath("./td[6]/b/text()").get()
                china = row.xpath("./td[7]/b/text()").get()
                aus = row.xpath("./td[8]/b/text()").get()
            country_.append(country)
            yeild_.append(yeild)
            germany_.append(germany)
            usa_.append(usa)
            china_.append(china)
            aus_.append(aus)
            last_upadated_.append(last_updated)
        
        json = {"country": country_, "yeild":yeild_, "germany":germany_, "usa":usa_, "china":china_, "aus":aus_, "last_upadated": last_upadated_}
        df = pd.DataFrame(json)
        df.to_csv("world_ratings.csv", index=False)
        print("csv done")
            