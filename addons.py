import mitmproxy.http
import json

class Counter:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        url1 = flow.request.url
        text1 = flow.response.get_text()#.decode('utf8',errors='ignore') #content.decode('utf8',errors='ignore')
        if '广告' in text1 and 'hl.snssdk.com/api/news/feed/' in url1:
            # 获取视频广告
            resp = text1#response.text
            json_data = json.loads(resp)
            data_list = json_data['data']
            for data in data_list:
                item = {}
                if '广告' in str(data):
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
                    self.write_file(item,'ad1_data.txt')
                    print(item)
                    print('成功存入一条视频广告')

        if '广告' in text1 and 'hl.snssdk.com/2/article/information/' in url1:
            false = False
            true = True
            dict1 = eval(text1)
            try:
                #视频
                data = dict1['data']
                related_video_toutiao = data['related_video_toutiao']
                object1 = related_video_toutiao[0]
                item = {}
                item['abstract'] = object1['abstract']
                item['display_url'] = object1['article_url']
                item['download_url'] = object1['download_url']
                item['source'] = object1['source']
                item['title'] = object1['title']
                item['web_url'] = object1['web_url']
                self.write_file(item,'ad2_data.txt')
                print(item)
                print('推荐视频中第一个广告存入成功')
            except:
                try:
                    # 图文
                    data = dict1['data']
                    related_video_toutiao = data['related_video_toutiao']
                    object1 = related_video_toutiao[0]
                    item = {}
                    item['download_url'] = object1['download_url']
                    middle_image = object1['middle_image']
                    item['url'] = middle_image['url']
                    item['source'] = object1['source']
                    item['title'] = object1['title']
                    item['web_url'] = object1['web_url']
                    self.write_file(item, 'ad2_data.txt')
                    print(item)
                    print('推荐视频中第一个广告存入成功')
                except:
                    with open('error2.txt','w') as f:
                        f.write(text1)
                        f.close()
            try:
                item = {}
                ad = dict1['data']['ad']
                app = ad['app']
                item['app_name'] = app['app_name']
                item['description'] = app['description']
                item['download_url'] = app['download_url']
                image = app['image']
                url_list = image['url_list']
                item['url'] = url_list[0]['url']
                item['title'] = app['title']
                item['web_url'] = app['web_url']
                self.write_file(item,'ad3_data.txt')
                print(item)
                print('推荐视频中最后一个广告存入成功')
            except:
                with open('error3.txt','w') as f:
                    f.write(text1)
                    f.close()


    def write_file(self,item,file_name):
        with open(file_name, 'a') as file:
            file.write(str(item) + '\n')
            file.close()

addons = [
    Counter()
]
