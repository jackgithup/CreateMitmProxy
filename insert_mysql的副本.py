#coding:utf8
import pymysql
import json
import os

class InsertMysql():
    def read_file(self):
        rfile = open('data.json','r')
        line = rfile.readline()
        i = 0
        while line:
            dict1 = eval(line)
            print(dict1)
            self.insert_mysql(dict1)
            line = rfile.readline()
            print('第{}条'.format(i))
            i += 1
        os.remove('data.json')

    def insert_mysql(self,dict1):
        try:
            db = pymysql.connect(host='192.168.102.168', port=3306, user='root', passwd='65#@fecos3sTnc@%1',
                                 db='schema_spider',
                                 charset='utf8mb4')
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "insert into jrtt_table(abstract,display_url,share_url,label,label_style,source,source_avatar,title,content) " \
                  "values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(dict1['abstract'],dict1['display_url'],dict1['share_url'],dict1['label'],
                                                                                dict1['label_style'],dict1['source'],dict1['source_avatar'],dict1['title'],dict1['content'])
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            cursor.close()
            # 关闭数据库连接
            db.close()
            print('insert data success!')
        except:
            print('data insert error1 dict1:{}'.format(dict1))
            with open('data_false.json', 'a') as file:
                file.write(str(dict1) + '\n')
                file.close()
        #     content = dict['content']
        #     db = pymysql.connect(host='192.168.102.168', port=3306, user='root', passwd='65#@fecos3sTnc@%1',
        #                          db='schema_spider',
        #                          charset='utf8mb4')
        #     # 使用cursor()方法获取操作游标
        #     cursor = db.cursor()
        #     # SQL 插入语句
        #     sql = "insert into jrtt_table(content) values('{}')".format(dict1['content'])
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # 执行sql语句
        #     db.commit()
        #     cursor.close()
        #     # 关闭数据库连接
        #     db.close()

    def start_run(self):
        self.read_file()

if __name__ == '__main__':
    insert_mysql = InsertMysql()
    insert_mysql.start_run()