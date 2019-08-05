# encoding:utf8
import mitmproxy.http
import json
import time

# 格式化成2016-03-20 11:45:39形式
today = '/Users/edz/Desktop/zhengmangProject/JRTT/data/' + time.strftime("%Y%m%d", time.localtime())
# print(today)
# print(type(today))

class Counter:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        headers = flow.response.headers
        url1 = flow.request.url
        text1 = flow.response.get_text()


        false = False
        true = True
        if '广告' in text1 and 'snssdk.com/api/news/feed/' in url1:
            # 获取视频广告
            resp = text1
            json_data = json.loads(resp)
            data_list = json_data['data']
            for data in data_list:
                item = {}
                # title,description,cover_url,display_url,download_url
                if '广告' in str(data):
                    content = data['content']
                    json_content = json.loads(content)
                    try:
                        item['title'] = json_content['title']
                        item['description'] = json_content['source']
                        item['cover_url'] = json_content['large_image_list'][0]['url']
                        item['display_url'] = json_content['display_url']
                        item['download_url'] = json_content['share_url']
                    except:
                        item['title'] = json_content['title']
                        item['description'] = json_content['abstract']
                        item['cover_url'] = json_content['large_image_list'][0]['url']
                        item['display_url'] = json_content['display_url']
                        item['download_url'] = json_content['share_url']
                    file_name = today + '_item.txt'
                    with open(file_name,'a') as wf:
                        wf.write(str(item)+'\n')
                        wf.flush()
                        wf.close()
                    print(item)
                    print('获取一条视频广告')

        if '广告' in text1 and 'snssdk.com/2/article/information/' in url1:
            dict1 = eval(text1)
            try:
                #视频
                data = dict1['data']
                related_video_toutiao = data['related_video_toutiao']
                object1 = related_video_toutiao[0]
                item = {}
                # title, description, cover_url, display_url, download_url
                item['title'] = object1['title']
                item['description'] = object1['abstract']
                item['cover_url'] = object1['web_url']
                item['display_url'] = object1['article_url']
                item['download_url'] = object1['download_url']
                file_name = today + '_item.txt'
                with open(file_name, 'a') as wf:
                    wf.write(str(item) + '\n')
                    wf.flush()
                    wf.close()
                print(item)
                print('获取推荐视频中第一个广告')
            except:
                try:
                    # 图文
                    data = dict1['data']
                    related_video_toutiao = data['related_video_toutiao']
                    object1 = related_video_toutiao[0]
                    item = {}
                    # title, description, cover_url, display_url, download_url
                    item['title'] = object1['title']
                    item['description'] = object1['source']
                    middle_image = object1['middle_image']
                    item['cover_url'] = middle_image['url']
                    item['display_url'] = object1['web_url']
                    item['download_url'] = object1['download_url']
                    file_name = today + '_item.txt'
                    with open(file_name, 'a') as wf:
                        wf.write(str(item) + '\n')
                        wf.flush()
                        wf.close()
                    print(item)
                    print('获取推荐视频中第一个广告')
                except Exception as e:
                    pass

            # 获取推荐视频中的最后一个广告
            try:
                item = {}
                # title, description, cover_url, display_url, download_url
                data = dict1['data']
                ad = data['ad']
                app = ad['app']
                item['title'] = app['title']
                item['description'] = app['description']
                item['cover_url'] = app['image']['url_list'][0]['url']
                item['display_url'] = app['web_url']
                item['download_url'] = app['download_url']
                file_name = today + '_item.txt'
                with open(file_name, 'a') as wf:
                    wf.write(str(item) + '\n')
                    wf.flush()
                    wf.close()
                print(item)
                print('获取推荐视频中最后一个广告')
            except Exception as e:
                try:
                    item = {}
                    # title, description, cover_url, display_url, download_url
                    data = dict1['data']
                    ad = data['ad']
                    app = ad['mixed']
                    item['title'] = app['title']
                    item['description'] = app['source_name']
                    item['cover_url'] = app['image']
                    item['display_url'] = app['web_url']
                    # item['download_url'] = app['download_url']
                    file_name = today + '_item.txt'
                    with open(file_name, 'a') as wf:
                        wf.write(str(item) + '\n')
                        wf.flush()
                        wf.close()
                    print(item)
                    print('获取推荐视频中最后一个广告')
                except Exception as e:
                    print(e)


addons = [
    Counter()
]


# title,description,cover_url,display_url,download_url