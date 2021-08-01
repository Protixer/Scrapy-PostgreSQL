import scrapy
from ..items import MytestspiderItem

class ZeldaItemsSpider(scrapy.Spider):
    name = 'quotes_toscrape_com'
    start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.get_articles)

    def get_articles(self, response):
        art_urls = [
            x.xpath("./@href").get()
            for x in response.xpath("//div[@class='quote']/span/a[contains(.,'about')]")
        ]
        for art_url in art_urls:
            art_url = "http://quotes.toscrape.com/" + art_url
            yield scrapy.Request(art_url, self.parse_article)

    def parse_article(self, response):

        item = MytestspiderItem()
        title = response.xpath(
            "//h3[@class='author-title']//text()"
        ).get()
        body = response.xpath(
            "//div[@class='author-description']"
        ).get()
        
        item["title"] = title
        item["url"] = response.url
        item["body"] = body

        if len(body) and len(title) > 5:
            print(item)
            yield item

