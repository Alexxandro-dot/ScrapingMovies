# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//tbody/tr/td[2]/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
      yield{
          'name': response.xpath("normalize-space(//div[@class='title_wrapper']/h1/text())").get(),
          'year': response.xpath("normalize-space(//a[@title='See more release dates']/text())").get(),
          'duration': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
          'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
          'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
          'movie_url': response.url
     
      }