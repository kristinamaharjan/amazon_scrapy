import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.com/gp/bestsellers/books/4736?ref_=Oct_d_obs_S&pd_rd_w=l1HVO&pf_rd_p=8000bc8c-c3b0-4816-9f00-5038ff54385c&pf_rd_r=9PPEJA47A2W0WYF5T93S&pd_rd_r=d3eaf516-c6e5-47c8-9f92-3902dbe332e1&pd_rd_wg=IkdWA']

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-link-normal ._p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y::text').extract()
        product_author = response.css('.a-size-small ._p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y').css('::text').extract()
        product_price = response.css('._p13n-zg-list-grid-desktop_price_p13n-sc-price__3mJ9Z').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.amazon.com/Best-Sellers-Books/zgbs/books/4736/ref=zg_bs_pg_2?_encoding=UTF8&pg=' + str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <= 100:
            yield response.follow(next_page, callback = self.parse)



