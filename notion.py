import os
from notion.client import NotionClient
from notion.client import *
from notion.block import *
import notion

class Notion(object):

    def __init__(self):
        NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
        PAGE_BLOCK = os.environ.get("PAGE_BLOCK")
        self.client = NotionClient(token_v2=NOTION_TOKEN)
        self.page = self.client.get_block(PAGE_BLOCK)

    def table_scheme(self):
        return {
            'title': {"name": "제목", "type": "title"},
            'url': {"name": "링크", "type": "url"},
            'type': {"name": "타입", "type": "text"},
            'date': {"name": "날짜", "type": "date"}
        }

    def create_table(self):
        ''' Use one-time only '''
        self.child_page = self.page.children.add_new(CollectionViewBlock)
        self.child_page.collection = self.client.get_collection(self.client.create_record('collection', parent=self.child_page, schema=self.table_scheme()))
        self.child_page.title = 'Nature'


    def set_table_value(self, metadata):
        self.child_page = self.page.children.add_new(CollectionViewBlock)
        self.child_page.collection = self.client.get_collection(self.client.create_record('collection', parent=self.child_page, schema=self.table_scheme()))
        # for data in metadata:
        #     row = self.child_page.collection.add_row()
        #     row.set_property('title', data['meta_title'])
        #     row.set_property('url', data['meta_url'])
        #     row.set_property('type', data['meta_type'])
        #     row.set_property('date', data['meta_date'])

    def get_page_identity(self):
        #print (self.page.id)
        #print (self.page.parent.id)
        #self.page.remove()
        pass
    
