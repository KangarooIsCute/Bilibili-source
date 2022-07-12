# 导入请求模块
import requests
import re
# 发送请求
url = 'https://search.51job.com/list/080300,000000,0000,00,9,99,python,2,1.html'
response = requests.get(url=url)
print(response) # <Response [200]>  200表示请求成功
print(response.text)
