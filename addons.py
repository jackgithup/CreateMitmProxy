import mitmproxy.http
import json

class Counter:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        url1 = flow.request.url
        text1 = flow.response.get_text()
        if '广告' in text1:
            print('发现广告关键字')
            # 获取视频广告
            if 'hl.snssdk.com/api/news/feed/' in url1:
            # # 将响应中所有“搜索”替换为“请使用谷歌”
                resp = text1#response.text
                json_data = json.loads(resp)
                data_list = json_data['data']
                for data in data_list:
                    item = {}
                    if '广告' in str(data):
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
                            with open('ad_data.json','a') as file:
                                file.write(str(item)+'\n')
                                file.close()
                            print('成功存入一条视频广告')
                        except:
                            print('视频广告存入失败')
                            with open('ad_data_false.txt', 'a') as f:
                                f.write(str(data) + '\n')
                                f.close()

            # 获取图文广告
            if '广告' in text1 and 'hl.snssdk.com/2/article/information/' in url1:
                try:
                    # 推荐视频中的第一个广告
                    false = False
                    true = True
                    dict1 = json.loads(text1)
                    data = dict1['data']
                    ad = data['ad']
                    related_video_toutiao = ad['related_video_toutiao']
                    content1 = related_video_toutiao[0]
                    with open('ad_data.json', 'a') as f:
                        json.dump(content1, f)
                        f.write('\n')
                    print('成功获取推荐视频中的第一个广告')
                except:
                    pass
                try:
                    # 推荐视频中的最后一个广告
                    false = False
                    true = True
                    dict1 = json.loads(text1)
                    data = dict1['data']
                    ad = data['ad']
                    app = ad['app']
                    with open('ad_data.json', 'a') as f:
                        json.dump(app,f)
                        f.write('\n')
                    print('成功获取推荐视频中的最后一个广告')
                except:
                    pass

addons = [
    Counter()
]
