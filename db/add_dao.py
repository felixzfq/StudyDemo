# -*- coding: utf-8 -*-
from db.mysql_db import pool

class AddDao:

    #添加垃圾
    def add_gc(self,name,type_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_gc(name,type_id) VALUES(%s,%s)"
            cursor.execute(sql,(name,type_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()