#!/usr/bin/Python2.7
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items

# class MySpider(scrapy.Spider):
#         name = "craig"
#         allowed_domains = ["craigslist.org"]
#         start_urls = [
#             "http://sfbay.craigslist.org/search/sfc/npo"    ]

#         def parse(self, response):
#           items = []
#           for sel in response.xpath('//p//a[@class="hdrlnk"]'):
#                item = CraigslistSampleItem()
#                item['title'] =  sel.xpath('text()').extract()
#                item['link'] = sel.xpath('@href').extract()
#                print(  sel.xpath('text()').extract())
#                print (sel.xpath('@href').extract())
#                items.append(item)
#                self.log.info("-------------")
#            return items
# class MySpider(BaseSpider):
#     name = "craig"
#     allowed_domains = ["craigslist.org"]
#     start_urls = ["http://sfbay.craigslist.org/sfc/npo/"]
#     # start_urls = ["http://columbusga.craigslist.org/search/reo"]

#     def parse(self, response):
#         hxs = HtmlXPathSelector(response)
#         titles = hxs.xpath("//span[@class='pl']")  #start trigger tag class='pl'
#         # titles = hxs.select("//p")
#         items = []
#         for titles in titles:
#             item = CraigslistSampleItem()
#             item["title"] = titles.select("a//text()").extract()  #tag a text 
#             item["link"] = titles.select("a/@href").extract()     #tag a href
#             items.append(item)

#             title = response.xpath("//span/text()").extract();
#             print("Title is: " + title);
#         return items


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
