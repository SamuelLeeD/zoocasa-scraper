import scrapy

class ListingsSpider(scrapy.Spider):
    name = "listings"

    def start_requests(self):
        # Change this if you want something other than Toronto
        urls = ["https://www.zoocasa.com/real-estate"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Get next page
        nextPage = response.xpath("//a[@class='icon-arrow-right-open active']/@href").get()
        nextPage = response.urljoin(nextPage)

        # Get all the listing URLs in current page
        listingUrls = response.xpath("//listing-card//a[@class='ember-view']/@href").getall()
        for url in listingUrls:
            
            # Call the listing information scraper on the listing URL
            link = response.urljoin(url)
            yield scrapy.Request(url = link,
                                 callback = self.parse_listing) # This means to call parse_listing on the url given
        
        # Repeat all this for the next page
        yield scrapy.Request(nextPage)
    
    def parse_listing(self, response):
        # Selecting price and address based on the XPath selectors
        list_price = response.xpath("//div[@class='list-price']/span/text()").get()
        sold_price = response.xpath("//div[@class='sold-price']/span/text()").get()
        street_address = response.xpath("//span[@itemprop='streetAddress']/text()").get()

        # Selecting XPath selectors for property details from the "Property Details" table
        listing_types = response.xpath("//details-table/section/div/span[1]")
        
        # Create dictionary of property details
        # The column name is given by [Table header]: [Attribute name]
        # For example, "building: Pets"
        # Header is necessary since some attributes may have the same name like "Heat" which appears twice
        details_dict = dict((selector.xpath("parent::div/preceding-sibling::header/span/text()").get() + ": " + selector.xpath("text()").get(),
                             selector.xpath("following-sibling::span/text()").get()) for selector in listing_types)

        # Merge price and address with property details
        result_dict = {"link": response.url,
                       "list_price": list_price,
                       "sold_price": sold_price,
                       "street_address": street_address}
                       
        result_dict.update(details_dict)

        # Keys of result_dict are column names, values are values
        yield result_dict
