
import csv
from bs4 import BeautifulSoup as bs
from dateparser.search import search_dates
import urllib.request as ur
from threading import Thread
import pandas as pd
import re
import os
import ssl
from helpers import chunks, get_response_from_url, format_text
ssl._create_default_https_context = ssl._create_unverified_context

def get_data_from_url(url):
    """Given a url will extract the content from it"""
    res = get_response_from_url(url)
    if res == None:
        print('No Response, Skipping %s...' % url)
        return None
    soup = bs(res,features='html.parser')
    soup = soup.find("div", {"id": "content"})
    date_section=soup.find('cite',attrs={'class':'section'})
    date = None
    dates = search_dates(date_section.text)
    if len(dates) >= 1: date = dates[0][0]
    contents = soup.findAll(['cite','p'])
    text = []
    for content in contents:
        if re.search(r' %s ' % date,content.text): continue # skip date section
        text.append(content.text)
    article_text = ' '.join(text)
    article_text = format_text(article_text)
    article_text
    return {'date':date, 'text':article_text}

def process_urls_in_range(ids):
    for i in ids:
        yr,month,day,title,url  = input[i]
        data = get_data_from_url(url)
        if data == None:
            print('Didnt Fetch %s from %s' % (title,url))
            continue
        print('Fetched %s from %s' % (title,url))
        date = data['date']
        article_text = data['text']
        row = [i+1,title,url,date,article_text]
        write_rows.append(row)


def process_articles_in_parallel(id_range,nthreads=55):
    """process the id range in a specified number of threads"""
    store = {}
    threads = []
    # create the threads
    for i in range(nthreads):
        ids = id_range[i::nthreads]
        t = Thread(target=process_urls_in_range, args=(ids,))
        threads.append(t)

    # start the threads
    [ t.start() for t in threads ]
    # wait for the threads to finish
    [ t.join() for t in threads ]

START_YEAR=2000
END_YEAR=2006
df = pd.read_csv('urls.csv',header=None,names=['yr','month','day','title','url'],low_memory=True)
for year in range(START_YEAR,END_YEAR+1):
    df_per_year = df[df['yr'] == year]
    file_name = 'parliament_articles_%d.csv' % year
    file_exists = os.path.exists(file_name)
    
    articles_df = None
    if file_exists:
        articles_df = pd.read_csv(file_name,delimiter=';',usecols=['Url'])
    content_file = open(file_name, 'a')
    writer = csv.writer(content_file,delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if not file_exists: writer.writerow(['ID','Title','Url','Date','Text']) 
    uniq_months = set(df_per_year['month'])
    for mon in uniq_months: 
        input_total = []
        for _, row in df_per_year[df_per_year['month'] == mon].iterrows():
            yr = row['yr']
            month = row['month']
            day = row['day']
            title = row['title']
            url = row['url']
            if articles_df is not None:
                res = articles_df[articles_df['Url'] == url]
                if len(res) > 0:
                    print('Skipping... ',url)
                    continue # skip already parsed
            values = [yr,month,day,title,url]
            input_total.append(values)
        for input in chunks(input_total,100):
            print('%d of Urls Read' % len(input))
            write_rows = []
            process_articles_in_parallel(range(len(input)))
            write_rows.sort()
            writer.writerows(write_rows)
    content_file.close()