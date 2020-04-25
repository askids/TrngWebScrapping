from urllib.request import urlopen as uReq  # Web client
from bs4 import BeautifulSoup as soup  # HTML data structure

class UrlScrapper(object):
    """
    [Class to scrape input URL]

    Arguments:
        object {[Custom type]} -- [URL Scrapper]
    """    
    
    def __init__(self, url):
        self.__url = url
        
    def get_page_content(self):
        """
        [opens the connection and downloads html page for url]

        Returns:
            [type] -- [description]
        """        
        uClient = uReq(self.__url)
        page_html = uClient.read()
        uClient.close()
        return page_html
    
    def get_soup_html(self):
        """
        [returns html content parsed as BeautifulSoup]

        Returns:
            [BeautifulSoup] -- [Soup]
        """        
        return soup(self.get_page_content(), "html.parser")
    