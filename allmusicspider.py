import scrapy
import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from core import models
# import pdb ; pdb.set_trace()


class AllMusicSpider(scrapy.Spider):
	name = 'allmusicspider'
	start_urls = ["https://www.allmusic.com/artist/do-make-say-think-mn0000169906"]

	def parse(self, response):
		print(response.css('section.moods ul a ::text').extract())

