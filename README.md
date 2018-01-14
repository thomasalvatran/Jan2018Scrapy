http://www.tovantran.com/blog/?p=3082
<pre><code>

scrapy crawl craig 
2018-01-13 19:28:14 [scrapy] INFO: Scrapy 1.0.7 started (bot: tutorial)
2018-01-13 19:28:14 [scrapy] INFO: Optional features available: ssl, http11, boto
2018-01-13 19:28:14 [scrapy] INFO: Overridden settings: {'NEWSPIDER_MODULE': 'tutorial.spiders', 'SPIDER_MODULES': ['tutorial.spiders'], 'ROBOTSTXT_OBEY': True, 'BOT_NAME': 'tutorial'}
2018-01-13 19:28:14 [scrapy] INFO: Enabled extensions: CloseSpider, TelnetConsole, LogStats, CoreStats, SpiderState
2018-01-13 19:28:14 [scrapy] INFO: Enabled downloader middlewares: RobotsTxtMiddleware, HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, ChunkedTransferMiddleware, DownloaderStats
2018-01-13 19:28:14 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2018-01-13 19:28:14 [scrapy] INFO: Enabled item pipelines: 
2018-01-13 19:28:14 [scrapy] INFO: Spider opened
2018-01-13 19:28:14 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2018-01-13 19:28:14 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-01-13 19:28:14 [scrapy] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2018-01-13 19:28:14 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2018-01-13 19:28:14 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2018-01-13 19:28:14 [quotes] DEBUG: Saved file quotes-1.html
================
2018-01-13 19:28:14 [quotes] DEBUG: Saved file quotes-2.html
================
2018-01-13 19:28:14 [scrapy] INFO: Closing spider (finished)
2018-01-13 19:28:14 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 675,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 5976,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 1, 14, 0, 28, 14, 592799),
 'log_count/DEBUG': 6,
 'log_count/INFO': 7,
 'response_received_count': 3,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2018, 1, 14, 0, 28, 14, 161198)}
2018-01-13 19:28:14 [scrapy] INFO: Spider closed (finished

scrapy crawl craig -o items.csv -t csv
more items.csv
link,title
https://sfbay.craigslist.org/sfc/npo/d/on-call-residential-counselor/6458923241.html,On-Call Residential Counselor - S
helter Program
https://sfbay.craigslist.org/sfc/npo/d/intake-specialist-bilingual/6458922363.html,Intake Specialist (Bilingual Spanis
h Preferred)
https://sfbay.craigslist.org/sfc/npo/d/shift-coordinator-swing-shift/6458921112.html,Shift Coordinator - Swing Shift
https://sfbay.craigslist.org/sfc/npo/d/housing-navigation-specialist/6458918546.html,Housing Navigation Specialist
https://sfbay.craigslist.org/sfc/npo/d/housing-stability-specialist/6458917961.html,Housing Stability Specialist - Hea
ding Home


</code>
