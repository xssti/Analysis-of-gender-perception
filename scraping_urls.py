from sys import prefix
from bs4 import BeautifulSoup as bs
import re
import csv
import ssl

from helpers import get_response_from_url, parallelize_function_calls_to_map

ssl._create_default_https_context = ssl._create_unverified_context

START_YR = 1900
END_YR = 1924
years = [str(yr) for yr in range(START_YR,END_YR+1)]
BASE_URL = 'https://api.parliament.uk'
DIRECTORY_BASE = '/historic-hansard/'
DIRECTORY_NAME = '%ssittings/' % DIRECTORY_BASE
urls_file = open('urls.csv', 'a')

month_prefixes = []


# get all webpages' responses from years concurrently
store = parallelize_function_calls_to_map(
   [ '%s/%s%s/index.html' % (BASE_URL,DIRECTORY_NAME,yr) for yr in years]
    ,get_response_from_url
)

for yr in years:
    prefix = '%s%s/' % (DIRECTORY_NAME , yr)
    url = '%s/%sindex.html' % (BASE_URL,prefix)
    res = store[url]
    if res == None: continue
    soup = bs(res,features='html.parser')
    for link in soup.findAll('a', href=True):
        href = link['href']
        match = re.search(prefix + '(.+)' ,href) 
        if match is None or len(match.groups()) == 0: continue
        month = match.groups()[0]
        month_prefixes.append((yr,month,href))

# get all webpages' responses from years concurrently
store = parallelize_function_calls_to_map(
    [BASE_URL + prefix for _,_,prefix in month_prefixes]
    ,get_response_from_url
)

date_prefixes = []
month_to_number = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'];
for yr, month, prefix in month_prefixes:
    url = BASE_URL + prefix 
    res = store[url]
    if res == None: continue
    soup = bs(res,features='html.parser')
    for link in soup.findAll('a', href=True):
        href = link['href']
        match = re.search(prefix + '/([0-9]+)' ,href)
        if match is None or len(match.groups()) == 0: continue
        day = match.groups()[0]
        date_prefixes.append((yr,day,month_to_number.index(month)+1,href))

writer = csv.writer(urls_file)
ctr = 0
write_rows = []

store = parallelize_function_calls_to_map(
    [BASE_URL + prefix for _,_,_,prefix in date_prefixes]
    ,get_response_from_url
)
for yr, day, month, prefix in date_prefixes:
    url = BASE_URL + prefix
    res = store[url]
    if res == None: continue
    soup = bs(res,features='html.parser')
    div_content = soup.find("div", {"id": "content"})
    links = div_content.findAll('a',href=True)

    for link in links:
        href = link['href']
        match = re.match(DIRECTORY_BASE + '.+' ,href) 
        if match is None: continue
        url_for_article = BASE_URL + href
        title_for_article = link.string
        ctr += 1
        write_rows.append([yr,month,day,title_for_article,url_for_article])
        print('Found article %s with url %s' % (title_for_article,url_for_article))
    
    

writer.writerows(write_rows)
urls_file.close()
exit(0)

