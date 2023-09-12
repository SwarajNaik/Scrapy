from pathlib import Path
import pandas as pd
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "central_bank_rates"

    def start_requests(self):
        urls = [
            "http://www.worldgovernmentbonds.com/central-bank-rates/"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath("/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[4]/table")
        rows = table.xpath("//tbody/tr")

        paese_ = []
        central_bank_rates_ = []
        variation_ = []
        period_= []
      
        
    
        for row in rows:
            paese = row.xpath('.//td[2]/b/a/text()').get() 
            central_bank_rates = row.xpath('.//td[3]/b/text()').get() 
            variation = row.xpath('.//td[4]/b/text()').get()
            period = row.xpath('.//td[5]/div/b/text()').get()
            
            paese_.append(paese)
            central_bank_rates_.append(central_bank_rates)
            variation_.append(variation)
            period_.append(period)
            
            
            
        
        
        json = {"paese": paese_, "central_bank_rates":central_bank_rates_, "variation":variation_, "period":period_}
        df = pd.DataFrame(json)
        df.to_csv("central_bank_rates1.csv", index=False)
        print("CSV")
