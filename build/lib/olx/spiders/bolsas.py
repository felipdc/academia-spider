import scrapy


class BolsasSpider(scrapy.Spider):
    name = 'academia'
    start_urls = ['https://www.academia.edu/Documents/in/History?page=first']

    def parse(self, response):
        for item in response.css('.u-borderBottom1'):
            yield {
                'author': item.css('div > ul > li:nth-child(3) > ul > li:nth-child(1) > span > span > a::text').get(),
                'title': item.css('div > div.header > div > a::text').get(),
                'tags_number': item.css('div > ul > li:nth-child(3) > ul > li.InlineList-item.u-positionRelative > div > a::text').get(),
                'link': item.css('div > div.header > div > a::attr(href)').get(),
            }
        next_page_url = response.css('li.next_page > a::attr(href)').extract_first()
        if next_page_url is not None:
            print("ok")
            print(response.urljoin(next_page_url))
            yield scrapy.Request(response.urljoin(next_page_url))