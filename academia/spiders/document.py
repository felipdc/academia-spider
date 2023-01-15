import scrapy
import json


class DocumentSpider(scrapy.Spider):
    name = 'document'
    start_urls = [f'https://www.academia.edu/{n}' for n in range(94000000, 94000100)]

    def parse(self, response):
      yield {
          'title': response.css('meta[property="og:title"]::attr(content)').get(),
          'description': response.css('meta[property="og:description"]::attr(content)').get(),
          'url': response.css('meta[property="og:url"]::attr(content)').get(),
          'type': response.css('meta[property="og:type"]::attr(content)').get(),
          'author': response.css('.AuthorsCard-AvatarGroup-cls2-2GHN.AuthorsCard-AvatarGroup-cls1-1D0L > div > div > a::text').get(),
          'author_url': response.css('meta[property="article:author"]::attr(content)').get(),
          'author_picture': response.css('#swp-tcr--top-inner-wrapper > div.work-card--authors-list > div > a > div > img::attr(src)').get(),
          'journal_title': response.css('meta[name="citation_journal_title"]::attr(content)').get(),
          'views': response.css('div.work-card--stats-outer-wrapper > span:nth-child(1) > span::text').get(),
          'pages': response.css('div.work-card--stats-outer-wrapper > span:nth-child(2) > span::text').get(),
          'tags': response.css('#swp-tcr--top-inner-wrapper > div.work-card--research-interest-outer-wrapper > div > div:nth-child(1) > a > div::text').get(),
          'publication_date': response.css('meta[name="citation_publication_date"]::attr(content)').get(),
      }