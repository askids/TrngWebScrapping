import aaodecisionpage as adp # Class with AAO Decision Page URL
import urlscrapper as uScr # Class to scrape URL
print('Starting Web Scrapping')

aao_page = adp.AaoDecisionPage()
all_links = []
start_year = 2010
end_year = 2019

# Get file list for input year range
for year in range(start_year, end_year + 1):
    # Get full URL for given year
    url = aao_page.getpage_for_year(year)
    print(f'URL for {year} - {url}')

    # Get raw content for URL
    urlscr = uScr.UrlScrapper(url)

    links = aao_page.get_file_list(urlscr.get_soup_html())
    
    all_links.extend(links)
    print(f'For {year}, found {len(links)} file link(s)')

print(f'Total files found {len(all_links)}')

