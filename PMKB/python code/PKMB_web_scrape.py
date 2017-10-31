import urllib
from lxml import html
import requests
import csv
import urllib.request as ur

base_link = 'https://pmkb.weill.cornell.edu/therapies/'
n_pages=416
filename = "PMKBcitations.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()
#numbers 142,190,191,192,213,248 dont exist
skips=[]
for i in range(1,n_pages+1):

    print (i)
    link = base_link+str(i)


    try:
        page = ur.urlopen(link)
    except (RuntimeError, TypeError, NameError, AttributeError, urllib.error.HTTPError):
        pass
        skips.append(str(i))

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(page, "html.parser")

        # print (soup.a)
        # print(soup.prettify())

    all_links = soup.find_all("a")
        # for link in all_links:
        #  print (link.get("href"))

    all_tables = soup.find_all("table")

        # hanging-indent pad-lft
        # test = soup.find_all('table', class_='table')
        # name_box = soup.find(‘div’, attrs={‘class’: ‘hanging-indent pad-lft’})
        # name = name_box.text.strip()
        # print(all_links)
    #f=open(csvfile)
    list_citations=[]
    list_of_lists={'id','citations'}
    citations = (soup.find_all(class_="hanging-indent pad-lft"))
        # print(citations)
    for link in citations:
        alink = (link.find('a'))

        try:
            list_citations.append(alink.get('href'))
        except (RuntimeError, TypeError, NameError, AttributeError):
            pass



    with open(r'PMKBcitations.csv', 'a')as f:
        writer = csv.writer(f)
        writer.writerow([str(i),list_citations])
    ## Python will convert \n to os.linesep
print(skips)
    #print(list_citations)
