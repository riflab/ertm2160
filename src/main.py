from bs4 import BeautifulSoup as soup
import requests
import re

def parse_url(url):
    response = requests.get(url)
    page_soup = soup(response.text, "html.parser")
    page = page_soup.find_all('a', href=True)

    list = [item['href'] for item in page]

    return list

def download_file(url, path):
    response = requests.get(url)
    open(path, "wb").write(response.content)

def main(url, path_f=None, pathsave=None):
    pages_1 = parse_url(url) 
    print(pages_1[5:])
    
    for i in pages_1[5:]:
        url_1 = url + i
        print(' > ' + url_1)
        path_save = pathsave + str(i)
        path_f.write(path_save + '\n')
        download_file(url_1, path_save)

if __name__ == '__main__':
    
    url = 'https://ddfe.curtin.edu.au/gravitymodels/ERTM2160/data/eta/'
    path = open('loge_ta.txt', 'w')
    path_save = '../data/eta/'
    main(url, path, path_save)

    url = 'https://ddfe.curtin.edu.au/gravitymodels/ERTM2160/data/xi/'
    path = open('log_xi.txt', 'w')
    path_save = '../data/xi/'
    main(url, path, path_save)

    url = 'https://ddfe.curtin.edu.au/gravitymodels/ERTM2160/data/dg/'
    path = open('log_dg.txt', 'w')
    path_save = '../data/dg/'
    main(url, path, path_save)

    url = 'https://ddfe.curtin.edu.au/gravitymodels/ERTM2160/data/geoid/'
    path = open('log_geoid.txt', 'w')
    path_save = '../data/geoid/'
    main(url, path, path_save)

    url = 'https://ddfe.curtin.edu.au/gravitymodels/ERTM2160/data/dem/'
    path = open('log_dem.txt', 'w')
    path_save = '../data/dem/'
    main(url, path, path_save)