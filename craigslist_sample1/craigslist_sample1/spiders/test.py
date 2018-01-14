#!/usr/bin/Python2.7
import scrapy
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample1.items import CraigslistSample1Item
# class MySpider(BaseSpider):
#     name = "craig"
#     allowed_domains = ["craigslist.org"]
#     start_urls = ["http://sfbay.craigslist.org/search/npo"]

#     def parse(self, response):
#         hxs = HtmlXPathSelector(response)
#         titles = hxs.xpath("//span[@class='pl']")
#         items = []
#         for titles in titles:
#             item = CraigslistSampleItem()
#             item["title"] = titles.select("a/text()").extract()
#             item["link"] = titles.select("a/@href").extract()
#             items.append(item)
#         return items
class MySpider(scrapy.Spider):
        name = "craig"
        allowed_domains = ["craigslist.org"]
        start_urls = [
            "http://sfbay.craigslist.org/search/sfc/npo"    ]

        def parse(self, response):
            # self.log.info("-------------")
            # hxs = HtmlXPathSelector(response) # deprecated now
            print("1-------------")
            self.log("Begin to parse")
            items = []
            for sel in response.xpath('//p//a[@class="result-title hdrlnk"]'):
                   print("2-------------")  # print on the screen
                   item = CraigslistSample1Item()
                   item['title'] =  sel.xpath('text()').extract()
                   item['link'] = sel.xpath('@href').extract()
                   print(  sel.xpath('text()').extract())
                   print (sel.xpath('@href').extract())
                   items.append(item)
            return items
# class MySpider(scrapy.Spider):
#     name = "craig"
#     allowed_domains = ["craigslist.org"]
#     start_urls = [
#         "http://sfbay.craigslist.org/search/sfc/npo"    ]

    # def parse(self, response):
    #     print ("================+++++++++++++++")
    #     items = []
    #     for sel in response.xpath('//p//a[@class="hdrlnk"]'):
    #        print ("================")
    #        item = CraigslistSample1Item()
    #        item['title'] =  sel.xpath('text()').extract()
    #        item['link'] = sel.xpath('@href').extract()
    #        items.append(item)
    #     return items
# class MySpider(BaseSpider):
#     name = "craigs"
#     allowed_domains = ["craigslist.org"]
#     start_urls = ["http://sfbay.craigslist.org/sfc/npo/"]
#     # start_urls = ["http://columbusga.craigslist.org/search/reo"]

    # def parse(self, response):
    #     print ("+++++++++")
    #     # hxs = HtmlXPathSelector(response)
    #     # titles = hxs.xpath("//span[@class='pl']")  #start trigger tag class='pl'
    #     # titles = hxs.select("//p")
    #     items = []
    #     for title in response.xpath('//p//a[@class="hdrlnk"]'):
    #         item = CraigslistSample1Item()
    #         item["title"] = titles.select("a//text()").extract()  #tag a text 
    #         item["link"] = titles.select("a/@href").extract()     #tag a href
    #         items.append(item)

    #         title = response.xpath("//span/text()").extract();
    #         print("Title is: " + title);
    #         self.log.info('===============')
    #         print ("+++++++++BBBBBBBBBB")
    #     return items
#     def parse(self, response):
#           items = []
#           for sel in response.xpath('//p//a[@class="hdrlnk"]'):
#             print sel.xpath('text()').extract()
#             print sel.xpath('@href').extract()


# response.xpath('//title/text()').extract()
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import HtmlXPathSelector
# from craigslist_sample.items import CraigslistSampleItem

# class MySpider(CrawlSpider):
#     name = "craigs"
#     allowed_domains = ["sfbay.craigslist.org"]
#     start_urls = ["http://sfbay.craigslist.org/search/npo"]

#     rules = (
#         Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
#     )

#     def parse_items(self, response):
#         hxs = HtmlXPathSelector(response)
#         titles = hxs.xpath('//span[@class="pl"]')
#         items = []
#         for titles in titles:
#             item = CraigslistSampleItem()
#             item["title"] = titles.xpath("a/text()").extract()
#             item["link"] = titles.xpath("a/@href").extract()
#             items.append(item)
#         return(items)
