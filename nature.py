import requests
from bs4 import BeautifulSoup

class Nature(object):

    def __init__(self):
        self.url = "https://www.nature.com/nature/research-articles"
        self.metadata = list()

    def get_metadata(self):
        response = requests.get(self.url)
        source = response.text

        soup = BeautifulSoup(source, 'html.parser')
        new_article_list = soup.find("section", {'id':'new-article-list'})
        for article in new_article_list.findAll("li", {'class':'app-article-list-row__item'}):
            for title in article.findAll('h3', {'class':'c-card__title'}):
                meta_title = title.text.strip('\n')
                meta_url = "https://www.nature.com" + title.find('a')['href']

            for meta in article.findAll('div',{'class':'c-card__section c-meta'}):
                meta_type = meta.find('span', {'class':'c-meta__type'}).getText()
                meta_date = meta.find('time', {'class':'c-meta__item c-meta__item--block-at-xl'})['datetime']

            meta_data_set = {
                'meta_title' : meta_title,
                'meta_url' : meta_url,
                'meta_type' : meta_type,
                'meta_date' : meta_date,
            }
            self.metadata.append(meta_data_set)

        return self.metadata
