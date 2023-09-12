from pathlib import Path
import pandas as pd
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "home_page"

    def start_requests(self):
        urls = [
            "https://makerburn.com/#/rundown"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # table = response.xpath("/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table")
        # rows = table.xpath("//tbody/tr")

        # country_ = []
        # snp = []
        # mody = []
        # fitch = []
        # dBRS = []
        
    
        # for row in rows:
        #     country = row.xpath('.//td[2]//a//text()').get() #/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table/thead/tr/th[2]/b
        #     S_p = row.xpath('.//td[3]//b//text() | .//td[3]//a//text()').get() #/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table/thead/tr/th[3]/b
        #     Moody = row.xpath('.//td[4]//b//text() | .//td[4]//a//text()').get() #/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table/thead/tr/th[4]/b
        #     Fitch = row.xpath('.//td[5]//b//text() | .//td[5]//a//text()').get() #/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table/thead/tr/th[5]/b
        #     DBRS = row.xpath('.//td[6]//b//text() | .//td[6]//a//text()').get() #/html/body/div/div[2]/div/article/div/div/div/div/div[2]/div[9]/table/thead/tr/th[6]/b
            
        #     country_.append(country)
        #     snp.append(S_p)
        #     mody.append(Moody)
        #     fitch.append(Fitch)
        #     dBRS.append(DBRS)
        
        # json = {"Country": country_, "S&P":snp, "Moody":mody, "Fitch":fitch, "DBRS":dBRS}
        # df = pd.DataFrame(json)
        # df.to_csv("home_page_country_rating.csv", index=False)
        
        table = response.xpath("/html/body/div[1]/main/div[2]/section[1]/table")
        rows = table.xpath("//tbody/tr")
        
        for row in rows:
            # print(row.xpath('.//td[1]/div[1]/text()').get())
            pass
        # /html/body/div[1]/main/div[2]/section[1]/table/tbody/tr[1]/td[1]/div[1]
        print(response.xpath("/html/body/div[1]/main/div[2]").get())
        

