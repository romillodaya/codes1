import scrapy
from ..items import WebsiteItem

class NewSpider(scrapy.Spider):
    name = 'new'
    page = 5
    website = 'https://www.entrepreneur.com/topic/websites/'
    start_urls = []
    for i in range(page+1):
        start_urls.append(website + str(i))

    def parse(self, response): 

        item = WebsiteItem()
        all_div = response.css('div.flex-grow.flex-1')

        for div in all_div:
            title = div.css('.font-semibold::text').extract()
            author = div.css('.focus\:text-black.ga-click::text').extract()
            desc = div.css('.text-gray-500::text').extract()
            date = div.css('time , .slotPosition-10 .text-gray-500::text').extract()
            read_time = div.css('.text-gray-700 span , .slotPosition-10 .text-gray-500::text').extract()
            title = title[0].strip()
            author = author[0].strip()
            desc = desc[0].strip()
            item ['title'] = title
            item['author'] = author
            item['desc'] = desc

            yield item

