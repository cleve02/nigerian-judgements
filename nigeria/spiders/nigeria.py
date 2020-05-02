# -*- coding: utf-8 -*-
import json
import os
from termcolor import colored, cprint
from bs4 import BeautifulSoup

from scrapy import Request, Spider 

from nigeria.items import CaseItem

class NigeriaSpider(Spider):
    name = 'judgements'
    
    
    JUDGEMENTS_URL = "https://lawnigeria.com/2018/06/judgments-and-cases-of-nigerian-courts/"
    CATEGORY_TO_PARSE = "Banking & Finance"          #This should be the exact text as on the browser. You can copy-paste the category title

    CASE_NUMBER_TO_EXTRACT = 1                    #Extracts the first case in the above category
   


    def start_requests(self):
        url = self.JUDGEMENTS_URL
        yield Request(url=url, callback=self.parse_categories_page)



    def parse_categories_page(self, response):
        response = response.body

        page = BeautifulSoup(response,"html.parser")
        page_title = page.title.string

        cprint(f"Scraped the page {page_title}","red")

        category_links = page.find_all("a","mfn-link mfn-link-6")

        links_dictionary ={}

        for link in category_links:
            name = link.string
            url = link["href"]
            if name and url :
                links_dictionary.update({ name : url })
                
        link_to_follow = links_dictionary[self.CATEGORY_TO_PARSE]

        yield Request(url=link_to_follow, callback=self.parse_single_category_page)



    def parse_single_category_page(self, response):
        response = response.body

        page = BeautifulSoup(response,"html.parser")
        page_title = page.title.string

        cprint(f"Scraped the page {page_title}","red")

        case_rows = page.find_all("tr")

        links_dictionary = {}
        for row in case_rows:
            links = row.find_all("a")

            for link in links:
                name = link.string 
                url = link["href"]

                links_dictionary.update({ name : url })

        case_link_to_follow = links_dictionary[list(links_dictionary.keys())[self.CASE_NUMBER_TO_EXTRACT - 1]]    

        yield Request(url=case_link_to_follow, callback=self.parse_case_page)



    def parse_case_page(self, response):
        response_body = response.body

        page = BeautifulSoup(response_body,"html.parser")
        page_title = page.title.string

        cprint(f"Scraped the page {page_title}","red")

        case_details = page.find("div",class_="the_content_wrapper").text    
        

        with open("details.txt",'w+',encoding="utf8") as f:
            f.write(case_details)

        with open("details.txt",'r+',encoding="utf8") as f:
            details = f.read()
            case = CaseItem(title=page_title,details=details,url = response.request.url)
            
        if case: return case

            

            

        

    
                   
                

        





        

 











































































  





    # def parse_user(self, response):
    # """
    # 解析用户信息
    # :param response: Response对象
    # """
    # self.logger.debug(response)
    # result = json.loads(response.text)
    # if result.get('data').get('userInfo'):
    #     user_info = result.get('data').get('userInfo')
    #     user_item = UserItem()
    #     field_map = {
    #         'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'cover': 'cover_image_phone',
    #         'gender': 'gender', 'description': 'description', 'fans_count': 'followers_count',
    #         'follows_count': 'follow_count', 'weibos_count': 'statuses_count', 'verified': 'verified',
    #         'verified_reason': 'verified_reason', 'verified_type': 'verified_type'
    #     }
    #     for field, attr in field_map.items():
    #         user_item[field] = user_info.get(attr)
    #     yield user_item
    #     # 关注
    #     uid = user_info.get('id')
    #     yield Request(self.follow_url.format(uid=uid, page=1), callback=self.parse_follows,
    #                     meta={'page': 1, 'uid': uid})
    #     # 粉丝
    #     yield Request(self.fan_url.format(uid=uid, page=1), callback=self.parse_fans,
    #                     meta={'page': 1, 'uid': uid})
    #     # 微博
    #     yield Request(self.weibo_url.format(uid=uid, page=1), callback=self.parse_weibos,
                        #meta={'page': 1, 'uid': uid})