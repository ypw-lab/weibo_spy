# weibo_spy
微博热点话题实时爬取话题title和url并采用jieba进行分词，词库进行匹配筛选出符合要求的不同类型的热点话题

就是对微博热搜榜进行请求，得到title和url，然后针对title不同内容进行过滤，使用jieba进行对title进行分词，只需要在词库里面有对应的关键词，即可检查到该话题并将其打印出来或者存储起来
