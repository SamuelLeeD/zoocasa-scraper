# Zoocasa crawler
Scrapes the listings from Zoocasa for property information and prices.

For it to work, you need to install Scrapy (probably using "pip install scrapy").

The crawler is currently set to get listings from `https://www.zoocasa.com/real-estate`. If you want it to just get listings for a specific city, for example, just replace the URL in `listings.py` with the search page for that city. For example, to get sold listings for Toronto, replace the URL with `https://www.zoocasa.com/toronto-on-sold-listings`

To get a .csv file of all the listings with their attributes, you need to navigate to the "zoocasa" folder in your command prompt (probably using "cd"). Then, with Scrapy installed, you need to run "scrapy crawl listings -o [FILENAME].csv". The crawler will automatically go through the listings and spit out a .csv file with the listing prices and details.

Note, if you use the filename of an existing .csv file, it will append to the end of that file. You might want to pick a unique name each time.

Also, if you just want to test the .csv output and don't want to go through all the 400+ pages, just press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop the crawler after a while. It will take a few seconds but it should stop eventually and you'll get the output thus far. *
