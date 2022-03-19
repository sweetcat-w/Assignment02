#-*- codeing = utf-8 *-
#@Time : 2022/3/15 20:30
#@Author : 212106732 田薇
#@File : demo01.py
#@Software : PyCharm

import requests,json
import urllib3
import datetime,time,os

# 存放访问网址
def main():
    url = "https://j1.pupuapi.com/client/marketing/storeproduct/v2/search?business=scenes&business_id=f14c37f7-3ff3-44da-a925-c2a158bf522d&category_id=f14c37f7-3ff3-44da-a925-c2a158bf522d&in_stock=-1&page=1&size=20&sort=0&store_id=7c1208da-907a-4391-9901-35a60096a3f9&tag=-1"
    get(url)

# 数据清洗
def get(url):
    # 获得爬取后的数据字典
    jsonData = askUrl(url)
    list = []   # 用于存放数据清洗后的数据
    productList = []    # 指定数据清洗位置
    productList = jsonData['data']['products'];
    # 遍历数据字典将指定数据存入data集合中
    for item in productList:
        data = {
            'p_name' : item['name'],  # 商品名
            'p_spec' : item['spec'],  # 规格
            'p_price' : item['price']/100, # 折扣价
            'p_marketPrice' : item['market_price']/100,  # 原价、市场价
            'p_subTitle' : item['sub_title'] , # 商品信息
        }
        # 将每一行清洗后的数据添加到list中
        list.append(data)
    showData(list)  # 调用显示方法

# 数据爬取（模拟浏览器爬取网站上的数据返回数据字典）
def askUrl(url):
    try:
        headers = {     # 模拟浏览器头部信息，向服务器发送信息
            "pp-version": "2021063201",
            "pp-os": "20",
            "Accept": "*/*",
            "Accept-Language": "zh-Hans-CN;q=1.0",
            "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
            "pp_storeid": "7c1208da-907a-4391-9901-35a60096a3f9",
            "User-Agent": "Pupumall/2.9.0;iPadOS 15.3.1;3FD69868-7E1C-4BC3-88F8-7541719968B1",
            "Host": "j1.pupuapi.com",
            "Connection": "keep-alive",
        }
        response = requests.get(url=url,headers=headers)
        # 将json格式数据转换为字典
        jsonOld = json.loads(response.text)
    except error.URLError as e:
        print("请输入正确的要爬取网站")
    return jsonOld

# 数据展示
def showData(list):
    # 单个数据展示
    print("\n--------------商品：" + list[0]['p_name'] + "--------------")
    print("规格：" + list[0]['p_spec'])
    print("价格：" + str(list[0]['p_price']))
    print("原价/折扣价：" + str(list[0]['p_price']) + "/" +str(list[0]['p_marketPrice']))
    print("详细信息：" + list[0]['p_subTitle'])
    print("\n---------------监控朴朴超市休闲零食新品专区商品的价格波动----------------")
    # 获取当前时间
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("当前时间为：" + date)
    # 遍历展示所有商品的信息
    i = 1
    for item in list:
        print(str(i) + "、 " + item['p_name'] + ",【价格为：" + str(item['p_price']) + "】")
        i = i+1


# 调用函数
if __name__ == '__main__':
    main()
