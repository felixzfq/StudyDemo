# -*- coding: utf-8 -*-
from db.quary_dao import QuaryDao

class QuaryService:
    __quary_dao = QuaryDao()

    #查询分类列表
    def quary_list(self):
        return self.__quary_dao.quary_list()

    #查询详情
    def quary_desc(self,id):
        return self.__quary_dao.quary_desc(id)

    #查询分类
    def quary_sort(self,name):
        return self.__quary_dao.quary_sort(name)

    #查询垃圾列表
    def search_list(self,name,page):
        return self.__quary_dao.search_list(name,page)

    #查询页数
    def search_count(self,type_id):
        return self.__quary_dao.search_count(type_id)
