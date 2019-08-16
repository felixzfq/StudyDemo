from db.mysql_db import pool

class QuaryDao:

    #查询分类列表
    def quary_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id,type,description FROM t_type"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询详情
    def quary_desc(self,id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT p.guidance FROM t_type t JOIN t_put p ON " \
                "t.id = p.type_id AND t.id=%s"
            cursor.execute(sql,[id])
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询分类
    def quary_sort(self,name):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT g.name,t.type FROM t_type t JOIN t_gc g ON " \
                "t.id = g.type_id AND g.name LIKE %s"
            cursor.execute(sql,['%'+name+'%'])
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询垃圾列表
    def search_list(self,name,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT g.id,g.name,t.type FROM t_gc g JOIN t_type t " \
                  "ON g.type_id=t.id AND t.type=%s " \
                  "ORDER BY g.update_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql,(name,(page-1)*5,5))
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询页数
    def search_count(self,type_id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM t_gc " \
                  "WHERE type_id=%s"
            cursor.execute(sql,[type_id])
            return cursor.fetchone()[0]
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()