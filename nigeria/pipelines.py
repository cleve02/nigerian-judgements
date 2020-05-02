# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import firebase_admin
from firebase_admin import credentials,firestore

class CasePipeline:


    def process_item(self, item, spider):

        cred = credentials.Certificate("helloworld-4c1b2-firebase-adminsdk-at3ey-68bfa2cbae.json")

        default_app = firebase_admin.initialize_app(cred)

        db = firestore.client()

        def get_latest_id():
            docs = db.collection("Cases").get()
            length = 0
            for doc in docs: 
                length+=1
            return length + 1           
            
        

        doc_ref = db.collection("Cases").document(f"{str(get_latest_id())}")

        doc_ref.set({
            "title":item.get('title'),
            "details":item.get('details'),
            "url":item.get('url')

        })
            

