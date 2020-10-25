import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser
import pandas as pd


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def main():
    url = 'https://www.giveindia.org/all-ngos/karnataka/'
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    df = pd.DataFrame(p.tables[0][1:],columns =p.tables[0][0])
    del df['']
    cate = pd.DataFrame(df['Cause'].unique(),columns=['Categories'])
    cate.to_csv('./cate.csv')
    causes = [
        'Health & Family Welfare',
        'Labour & Employment',
        "Women's Development & Empowerment",
        'Education',
        'Children',
        'Rural Development & Poverty Alleviation',
        'Drinking Water',
        'Vocational Training',
        'Dalit Upliftment',
        'Micro Finance (SHGs)',
        'Urban Development & Poverty Alleviation',
        'Micro Small & Medium Enterprises',
        'Nutrition'
    ]
   
    final = (df.loc[df['Cause'].isin(causes)])
    final.to_csv('./all_ngo.csv', index = False)
if __name__ == '__main__':
    main()