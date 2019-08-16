# -*- coding: utf-8 -*-
from db.add_dao import AddDao

class AddService:
    __add_dao = AddDao()

    #添加垃圾
    def add_gc(self,name,type_id):
        self.__add_dao.add_gc(name,type_id)

