# botbee


## Run the crawler first by going to the folder  crawler/websitecrawler and then running the command scrapy crawl UniversityCrawler. This will extract texts and dum into chroma db.
## Then comeout of the folder and go to root level and then run bot_qa_ans.py
## I have made it to answer only from context, so if it cant scrape, it will say I don't know. Ask example qths like "What are the taught degrees in UCL?"
## If it's not scrapping, include in rule .. Rule(LinkExtractor(allow = 'graduate'), callback = 'parse_item')


