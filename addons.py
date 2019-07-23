import mitmproxy.http
from mitmproxy import ctx
import pymysql
import time
import json

class Counter:
    def __init__(self):
        self.num = 0

    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     self.num = self.num + 1
    #     ctx.log.info("We've seen %d flows" % self.num)

    # def insert_mysql(self,url1):
    #     #`id` INT UNSIGNED AUTO_INCREMENT,
    #     # `req_url` VARCHAR(255) DEFAULT NULL,
    #     # `create_time` VARCHAR(255) DEFAULT NULL,
    #     #  `req_status` VARCHAR(255) DEFAULT NULL,
    #     # try:
    #     db = pymysql.connect(host='192.168.102.168', port=3306, user='root', passwd='65#@fecos3sTnc@%1',
    #                          db='schema_spider',
    #                          charset='utf8mb4')
    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #     # SQL 插入语句
    #
    #     # 格式化成2016-03-20 11:45:39形式
    #     now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     sql = "insert into jrtt_urls_table(req_url,create_time,req_status) values('{}','{}','0')".format(url1,now_time) #0表示未爬取
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     # 执行sql语句
    #     db.commit()
    #     cursor.close()
    #     # 关闭数据库连接
    #     db.close()
    #     pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        url1 = flow.request.url
        if 'hl.snssdk.com/api/news/feed/' in url1:
            # print(url1)
            # text1 = flow.response.get_text()

            # print(text1)
            # self.insert_mysql(url1)
            # db = pymysql.connect(host='192.168.102.168', port=3306, user='root', passwd='65#@fecos3sTnc@%1',
            #                      db='schema_spider',
            #                      charset='utf8mb4')
            # # 使用cursor()方法获取操作游标
            # cursor = db.cursor()
            # # SQL 插入语句
            #
            # # 格式化成2016-03-20 11:45:39形式
            # now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # sql = "insert into jrtt_urls_table(req_url,create_time,req_status) values('{}','{}','0')".format(url1,now_time) #0表示未爬取
            # # 执行sql语句
            # cursor.execute(sql)
            # # 执行sql语句
            # db.commit()
            # cursor.close()
            # # 关闭数据库连接
            # db.close()
            with open('request_urls.txt','a') as f:
                f.write(flow.request.url + '\n')
                # f.write(text1 + '\n')
                f.close()
                print('成功存入一条url!')

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 忽略非 360 搜索地址
        # if flow.request.host != "www.so.com":
        #     return
        url1 = flow.request.url
        if 'hl.snssdk.com/api/news/feed/' in url1:
        # 将响应中所有“搜索”替换为“请使用谷歌”
            text1 = flow.response.get_text()
            # print(text1)
            # with open('resp.txt', 'a') as f:
            #     f.write(text1 + '\n')
                # f.write(text1 + '\n')
                # f.close()
            resp = text1#response.text
            json_data = json.loads(resp)
            data_list = json_data['data']
            for data in data_list:
                # print('data:{}'.format(data))
                item = {}
                if '广告' in str(data):
                    print('有广告关键字！')
                    try:

                        content = data['content']
                        json_content = json.loads(content)
                        item['abstract'] = json_content['abstract']
                        item['display_url'] = json_content['display_url']
                        item['label'] = json_content['label']
                        item['label_style'] = json_content['label_style']
                        item['share_url'] = json_content['share_url']  # APP下载链接
                        item['source'] = json_content['source']
                        item['source_avatar'] = json_content['source_avatar']  # APP图标
                        item['title'] = json_content['title']
                        item['content'] = content
                        # resp_url = response.url
                        # all_list.append(resp_url)
                        with open('data.json','a') as file:
                            file.write(str(item)+'\n')
                            file.close()
                        # self.insert_mysql(item)
                        print('数据存储成功！')
                        # print('all_list:{}'.format(all_list))
                        # time.sleep(5)
                        # yield item
                    except:
                        print('数据提取失败！')
                        with open('广告提取失败.txt', 'a') as f:
                            f.write(str(data) + '\n')
                            f.close()
                            time.sleep(5)
                else:
                    print('没有广告关键字！')
                # print('data:{}'.format(data))
            # text = text.replace("搜索", "请使用谷歌")
            # flow.response.set_text(text)
        # if 'ic-hl.snssdk.com/api/news/feed/' in url1:
        #     print(url1)
        #     with open('request_urls.txt','a') as f:
        #         f.write(flow.request.url + '\n')
        #         f.close()
        # 忽略非百度搜索地址
        # if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
        #     return

        # 确认请求参数中有搜索词
        # if "wd" not in flow.request.query.keys():
        #     ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
        #     return

        # 输出原始的搜索词
        # ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        # 替换搜索词为“360搜索”
        # flow.request.query.set_all("wd", ["360搜索"])
    def insert_mysql(self,item):
        # try:
        db = pymysql.connect(host='192.168.102.168', port=3306, user='root', passwd='65#@fecos3sTnc@%1',
                             db='schema_spider',
                             charset='utf8mb4')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = "insert into jrtt_table(abstract,display_url,share_url,label,label_style,source,source_avatar,title,content) " \
              "values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(item['abstract'], item['display_url'],
                                                                            item['share_url'],item['label'],
                                                                            item['label_style'], item['source'],
                                                                            item['source_avatar'], item['title'],
                                                                            item['content'])
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        cursor.close()
        # 关闭数据库连接
        db.close()

# if __name__ == '__main__':
addons = [
    Counter()
]
    #mitmproxy -p 8080 -s addons.py

