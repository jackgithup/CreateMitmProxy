# coding:utf8
import mitmproxy.http
import json
import time

# 格式化成2016-03-20 11:45:39形式
today = '/Users/edz/Desktop/zhengmangProject/JRTT/data/' + time.strftime("%Y%m%d", time.localtime())
# print(today)
# print(type(today))

class Counter:
    def __init__(self):
        self.file_name = today + '_item.txt'

    def write_file(self,item):

        with open(self.file_name, 'a') as self.wf:
            self.wf.write(str(item) + '\n')
            self.wf.flush()
        self.wf.close()
        print(item)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        headers = flow.response.headers
        url1 = flow.request.url
        text1 = flow.response.get_text()
        false = False
        true = True
        #http://is-hl.snssdk.com/api/news/feed/v88/?list_count=121&category=video&refer=1&refresh_reason=2&session_refresh_idx=8&count=20&min_behot_time=1565062319&list_entrance=main_tab&last_refresh_sub_entrance_interval=1565062442&gps_mode=7&loc_mode=0&tt_from=tab&plugin_enable=3&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A0%22%2C%22lynx_version_json%22%3A%22%7B%5C%22ugc_lynx_hotboard%5C%22%3A73501%7D%22%7D&sati_extra_params=%7B%22last_click_item_list%22%3A%5B%5D%7D&iid=81675131996&device_id=56553539644&ac=wifi&channel=xiaomi&aid=13&app_name=news_article&version_code=736&version_name=7.3.6&device_platform=android&ab_version=830855%2C1015033%2C1060010%2C662176%2C1030947%2C674049%2C643894%2C1052633%2C1022879%2C649426%2C801968%2C707372%2C667097%2C1048158%2C661907%2C668775%2C750019%2C1052816%2C1015389%2C1023103%2C739392%2C662099%2C668774%2C1063561%2C631594%2C765196%2C1050251%2C857803%2C757284%2C679100%2C660830%2C1039433%2C1054755%2C1027119%2C661781&ab_feature=94563%2C102749&ssmix=a&device_type=Redmi+6A&device_brand=xiaomi&language=zh&os_api=27&os_version=8.1.0&openudid=721f5a419901e06d&manifest_version_code=736&resolution=720*1344&dpi=320&update_version_code=73608&_rticket=1565062442609&plugin=0&fp=T2TrPzcOczGWFlceP2U1FzKSFrGW&rom_version=miui_v10_v10.0.1.0.ocbcnfh&ts=1565062442&as=ab8d5f1e085d48f52a8d5f&mas=011993233399b35993192379b9852d906b59931923b97393592313&cp=51d14d83f552aq1
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
                        item['description'] = json_content['abstract']
                        item['cover_url'] = json_content['large_image_list'][0]['url']
                        item['display_url'] = json_content['article_url']
                        item['land_page']  =  json_content['raw_ad_data']['web_url']
                        item['download_url'] = json_content['raw_ad_data']['download_url']
                    except Exception as e:
                        print(e)
                        pass
                        # item['title'] = json_content['title']
                        # item['description'] = json_content['source']
                        # item['cover_url'] = json_content['large_image_list'][0]['url']
                        # item['display_url'] = json_content['display_url']
                        # item['land_page']  =  json_content['raw_ad_data']['web_url']
                        # item['download_url'] = json_content['raw_ad_data']['download_url']
                    # file_name = today + '_item.txt'
                    # with open(file_name, 'a') as wf:
                    #     wf.write(str(item) + '\n')
                    #     wf.flush()
                    #     wf.close()
                    # print(item)
                    self.write_file(item)
                    print('视频广告')


        if '广告' in text1 and 'snssdk.com/2/article/information/' in url1:
            dict1 = eval(text1)
            try:
                data = dict1['data']
                related_video_toutiao = data['related_video_toutiao']
                object1 = related_video_toutiao[0]
                item = {}
                # title, description, cover_url, display_url, download_url
                item['title'] = object1['title']
                item['description'] = object1['abstract']
                item['source'] = object1['source']
                item['cover_url'] = object1['middle_image']['url']
                item['display_url'] = object1['article_url']
                item['land_page'] = object1['web_url']
                item['download_url'] = object1['download_url']
                # file_name = today + '_item.txt'
                # with open(file_name, 'a') as wf:
                #     wf.write(str(item) + '\n')
                #     wf.flush()
                #     wf.close()
                # print(item)
                self.write_file(item)
            except Exception as e:
                print(e)
                # print('获取推荐视频出错！')
            #     try:
            #         # 图文
            #         data = dict1['data']
            #         related_video_toutiao = data['related_video_toutiao']
            #         object1 = related_video_toutiao[0]
            #         item = {}
            #         # title, description, cover_url, display_url, download_url
            #         item['title'] = object1['title']
            #         item['description'] = object1['source']
            #         middle_image = object1['middle_image']
            #         item['cover_url'] = middle_image['url']
            #         item['land_page'] = object1['article_url']
            #         item['download_url'] = object1['download_url']
            #         # file_name = today + '_item.txt'
            #         # with open(file_name, 'a') as wf:
            #         #     wf.write(str(item) + '\n')
            #         #     wf.flush()
            #         #     wf.close()
            #         # print(item)
            #         self.write_file(item)
            #     except Exception as e:
            #         print(e)
            # finally:
            # print('获取推荐视频中第一个广告')

            # 获取推荐视频中的最后一个广告
            try:
                item = {}
                # title, description, cover_url, display_url, download_url
                data = dict1['data']
                ad = data['ad']
                app = ad['app']
                item['title'] = app['title']
                item['app_name'] = app['app_name']
                item['description'] = app['description']
                item['cover_url'] = app['image']['url_list'][0]['url']
                # item['display_url'] = app['web_url']
                item['land_page'] = app['web_url']
                item['download_url'] = app['download_url']
                # file_name = today + '_item.txt'
                # with open(file_name, 'a') as wf:
                #     wf.write(str(item) + '\n')
                #     wf.flush()
                #     wf.close()
                # print(item)
                self.write_file(item)
            except Exception as e:
                print(e)
                # try:
                #     item = {}
                #     # title, description, cover_url, display_url, download_url
                #     data = dict1['data']
                #     ad = data['ad']
                #     app = ad['mixed']
                #     item['title'] = app['title']
                #     item['description'] = app['source_name']
                #     item['cover_url'] = app['image']
                #     # item['display_url'] = app['web_url']
                #     item['land_page'] = app['web_url']
                #     # item['download_url'] = app['download_url']
                #     # file_name = today + '_item.txt'
                #     # with open(file_name, 'a') as wf:
                #     #     wf.write(str(item) + '\n')
                #     #     wf.flush()
                #     #     wf.close()
                #     # print(item)
                #     self.write_file(item)
                # except Exception as e:
                #     print(e)
            print('推荐广告')



addons = [
    Counter()
]


# title,description,cover_url,display_url,download_url