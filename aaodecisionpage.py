from bs4 import BeautifulSoup as soup  # HTML data structure
class AaoDecisionPage(object):

    """ Class for AAO Decision Page from USCIS site """
        
    def __init__(self):
        """
        [Initialize]
        """        
        self.__root_page = 'https://www.uscis.gov/'
        self.__search_page_prefix = 'https://www.uscis.gov/laws/admin-decisions?topic_id=1&newdir=D2+-+Temporary+Worker+in+a+Specialty+Occupation+or+Fashion+Model+%28H-1B%29%2FDecisions_Issued_in'
        self.links = []
    
    def getpage_for_year(self, year):
        """
        [returns year specific URL for input year]

        Arguments:
            year {[int]} -- [Year]

        Returns:
            [string] -- [Year specific URL]
        """        
        self.year = year
        return f'{self.__search_page_prefix}_{year}/'
    
    def parse_link(self, href):
        """
        [returns full URL for input relative href link]

        Arguments:
            href {[string]} -- [relative URL]

        Returns:
            [string] -- [full URL]
        """        
        return f'{self.__root_page}' + href[3:]

    def get_file_list(self, page_soup):
        """
        [parses input page soup and returns file list]

        Arguments:
            page_soup {[BeautifulSoup]} -- [html parsed Soup]

        Returns:
            [list[]] -- [list of files]
        """        
        resulset = page_soup.find_all("aside", attrs = {"id": "associated-links"})
        temp_soup = soup(str(resulset[0]), "html.parser")
        list_items = temp_soup.find_all('li')
        #print(f'Found {len(list_items)} file link(s) inside')

        links = []
        for li in list_items:
            href = li.a.get('href')
            links.append(self.parse_link(href))
            
        return links

if __name__ == "__main__":
    page = AaoDecisionPage()
    print(page.getpage_for_year(2019))