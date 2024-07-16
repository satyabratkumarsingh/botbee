import json
import scrapy
from urllib.parse import urljoin
import re
import time
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#from .langchain_save_chroma import store_in_chroma


class UniversityCrawler(CrawlSpider):
    name = "UniversityCrawler"

    allowed_domains = ['ucl.ac.uk']

    start_urls = [
        'https://www.ucl.ac.uk/',
    ]

    rules = (
            Rule(LinkExtractor(allow = 'prospective-students', deny = 'graduate')),
            Rule(LinkExtractor(allow = 'graduate'), callback = 'parse_item')
            )


    def parse_item(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        
        page = {
            'url': response.url,
            'text': text,
        }
        print(text)
        print('Storing in chroma...')
        #store_in_chroma(text)
        yield page

