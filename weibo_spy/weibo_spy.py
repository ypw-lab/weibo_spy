import requests
from lxml import etree
#import time
import csv
import jieba #进行分词

def gettime():
    # 获取当前的时间
    #print("当前的时间是：", time.strftime("%Y-%m-%d %H:%M:%S"))
    pass

def save(name, hot):
    lsname = []
    for i in range(0, len(name)):
        lsname.append([name[i], hot[i]])
    with open("hot.csv", "w", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lsname)
        
def check(text):#该函数用jieba库分词进行词库匹配判断是否为政治话题
    seg_list = jieba.cut(text, cut_all=False)
    #print(" ".join(seg_list))#打印一下看看
    
    # 读取词库
    with open('ciku.txt',encoding='utf-8') as f:
       keywords = set(line.strip() for line in f)
       
    #进行匹配
    matches = [word for word in seg_list if word in keywords]
    #如果存在匹配，就返回true
    if len(matches) > 0:
       #print(matches)
       return True

    

if __name__ == "__main__":

    gettime()

    # 确认目标的 url
    _url = "https://s.weibo.com/top/summary"

    # 手动构造请求的参数
    _headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
        "cookie" : "SINAGLOBAL=5701031797732.083.1638971150198; SUB=_2AkMW7DFkf8NxqwFRmP0QzGvkaIR1zgnEieKgsMC_JRMxHRl-yT9jqhErtRB6PWwfi8IMi4nS63fCLKIwRiYKqexEzF_Q; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFPkNiIHiOqUjBBn8.B.qFu; _s_tentry=cn.bing.com; Apache=9978275422977.867.1639488984604; UOR=,,cn.bing.com; ULV=1639488984639:4:4:1:9978275422977.867.1639488984604:1639061325022",
        # "Referer": "https://www.baidu.com/link?url=j4BATujs6r1tDJgq8AqwTKYFP94_YcXPDXrDW9XKN2wmO0CyWck18MN0ES1bM5gX&wd=&eqid=fdbaa254000e24100000000261b05229"
    }

    # 发送请求
    _response = requests.get(_url, headers = _headers)
    _data = _response.text
    # print(data_)

    # 提取数据
    html_obj = etree.HTML(_data)
    
    # 长度
    name_list = html_obj.xpath('//td/span/preceding-sibling::a/text()')
    l = len(name_list)
    #print(l)
    #打印热点话题
   # print(name_list)
    
    
    # 微博： 1.名称 2.url 链接
    
    for i in range(1,len(name_list)):
      s = '//*[@id="pl_top_realtimehot"]/table/tbody/tr['
      s += f'{i}'
      s += ']/td[2]/a/text()'
      #print(s)
     
      s1 = '//*[@id="pl_top_realtimehot"]/table/tbody/tr['
      s1 += f'{i}'
      s1 += ']/td[2]/a/@href'
      #print(s1)
      name_top = html_obj.xpath(s)[0]
      
      if check(name_top):
         url_top = html_obj.xpath(s1)[0]
         url = "https://s.weibo.com/" + url_top
         print(f'热点事件：{name_top}，链接地址：{url}')
         
      

