import scrapy
from ..items import GoodreadItem


class GoodreadsSpider(scrapy.Spider):
    name = "goodreads"
    page_number = 2
    start_urls = ["https://www.goodreads.com/list/show/1.Best_Books_Ever"]

    def parse(self, response):

        items = GoodreadItem()
        
        book_name = response.css(".bookTitle span::text").extract()
        book_author = response.css(".authorName span::text").extract()
        book_score = response.css(".uitext a:nth-child(1)::text").extract()
        book_vote = response.css(".greyText+ a::text").extract()
        book_ratings = response.css(".minirating::text").extract()
        book_link = response.css(".bookCover::attr(src)").extract()

        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_score'] = book_score
        items['book_vote'] = book_vote
        items['book_ratings'] = book_ratings
        items['book_link'] = book_link

        yield items

        next_page = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page="+str(GoodreadsSpider.page_number)
        
        if GoodreadsSpider.page_number <= 100:
            GoodreadsSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
