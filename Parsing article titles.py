import requests
from bs4 import BeautifulSoup

def get_page_titles_text(url):

    all_page_titles = ''
    r = requests.get(url)
    all_page_text = str(r.content)
    bs = BeautifulSoup(all_page_text, 'html.parser')
    title_tags_all = bs.find_all(itemprop='name headline')
    for title_tag in title_tags_all:
        title_text = title_tag.select_one('a').get_text(strip=True)
        all_page_titles += str(title_text)
        all_page_titles += '\n'
    return all_page_titles

def parse_all_pages(my_url, pages_number):

    all_pages_text = ''
    for page in range(1, pages_number+1):
        all_pages_text += get_page_titles_text(my_url+str(page))        
    return all_pages_text


with open('words_Nature.txt', 'w') as output:

    LINK = 'https://www.nature.com/search?order=date_desc&date_range=\
            last_year&subject=computational-biology-and-bioinformatics\
            &article_type=research&page='
    PAGES = 20  # due to restrictions

    info = parse_all_pages(LINK, PAGES)
    output.write(info)

