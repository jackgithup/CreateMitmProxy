import mitmproxy.http
import json


class Counter:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        url1 = flow.request.url
        text1 = flow.response.get_text()
        false = False
        true = True
        if '广告' in text1 and 'hl.snssdk.com/api/news/feed/' in url1:
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

                    with open('item.txt','a') as wf:
                        wf.write(str(item)+'\n')
                        wf.close()
                    print(item)
                    print('一条视频广告')

        if '广告' in text1 and 'hl.snssdk.com/2/article/information/' in url1:
            dict1 = eval(text1)
            try:
                #视频
                data = dict1['data']
                related_video_toutiao = data['related_video_toutiao']
                object1 = related_video_toutiao[0]
                item = {}
                item['abstract'] = object1['abstract']
                item['display_url'] = object1['article_url']
                item['share_url'] = object1['download_url']
                item['source'] = object1['source']
                item['title'] = object1['title']
                item['source_avatar'] = object1['web_url']
                with open('item.txt', 'a') as wf:
                    wf.write(str(item) + '\n')
                    wf.close()
                print('推荐视频中第一个广告')
            except:
                try:
                    # 图文
                    data = dict1['data']
                    related_video_toutiao = data['related_video_toutiao']
                    object1 = related_video_toutiao[0]
                    item = {}
                    try:
                        item['share_url'] = object1['download_url']
                    except:
                        pass
                    middle_image = object1['middle_image']
                    item['source_avatar'] = middle_image['url']
                    item['source'] = object1['source']
                    item['title'] = object1['title']
                    item['source_avatar'] = object1['web_url']
                    with open('item.txt', 'a') as wf:
                        wf.write(str(item) + '\n')
                        wf.close()
                    print('推荐视频中第一个广告')
                except Exception as e:
                    pass

            # 获取推荐视频中的最后一个广告
            try:
                item = {}
                data = dict1['data']
                ad = data['ad']
                app = ad['app']
                item['title'] = app['title']
                item['description'] = app['description']
                try:
                    item['cover_url'] = app['image']['url_list']['url']
                except:
                    pass
                item['display_url'] = app['web_url']
                item['download_url'] = app['download_url']
                with open('item.txt', 'a') as wf:
                    wf.write(str(item) + '\n')
                    wf.close()
                print('获取推荐视频中最后一个广告')
            except Exception as e:
                pass


addons = [
    Counter()
]


# title,description,cover_url,display_url,download_url