#coding:utf8
import pymysql
import json
import os
m = 0
n = 0
class InsertMysql():
    def read_file(self):
        with open('item.txt','r') as rf:
            load_dict = rf.readlines()
            # print(load_dict)
        for item in load_dict:
            # print(item)
            # print(type(item))
            self.insert_mysql(eval(item))


    def insert_mysql(self,dict1):
        print(dict1)
        print(type(dict1))
        try:

            db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zheng123',db='schema_spider',charset='utf8mb4')
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            # title,description,cover_url,display_url,download_url
            sql = """insert into jrtt_table(title,description,cover_url,display_url,download_url) values('{}','{}','{}','{}','{}')""".format(
                dict1['title'],dict1['description'],dict1['cover_url'],dict1['display_url'],dict1['download_url'])
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            cursor.close()
            # 关闭数据库连接
            db.close()
            # print('insert data success!')
            global m
            print('插入成功',m)
            m += 1
        except Exception as e:
            global n
            print('插入失败',n)
            print(e)
            with open('item_error.txt','a') as f:
                f.write(str(dict1) + '\n')
                f.flush()
            f.close()
            n += 1

    def start_run(self):
        self.read_file()

if __name__ == '__main__':
    insert_mysql = InsertMysql()
    insert_mysql.start_run()