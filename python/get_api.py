import requests
import json

serviceKey = '5u0JKsFM1zDaRTdc4hXeNYfNS66XbSh0Itj0Kf%2FdpjgFuZSNO2ERCr5jFdluwjPSA7VhiNFVcMzbEBL0UZUjnw%3D%3D'
pageNo = 1
numOfRows = 100
types = 'json'
url = 'http://api.data.go.kr/openapi/tn_pubr_public_pblprfr_event_info_api'
url_2 = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
path = ''

def make_file():
    #url_result = url + '?serviceKey=' + serviceKey + '&pageNo=' + str(pageNo) + '&numOfRows=' + str(numOfRows) + '&type=' + types
    url_result = url_2 + '?serviceKey=' + serviceKey + '&pageNo=' + str(pageNo) + '&numOfRows=' + str(numOfRows) + '&type=' + types

    response = requests.get(url_result)
    response.encoding = 'UTF-8'
    
    text = response.content
    
    file = open('../json/data.json', 'wb')
    file.write(text)
    file.close()
    
    with open('../json/data.json', 'r') as file:
        text = json.load(file, strict=False)
    
    with open(path, 'w') as file:
        json.dump(text, file, indent = 4, ensure_ascii = False)

for i in range(1, 12):
    pageNo = i
    path = '../json/Second_Data/data_' + str(pageNo) + '.json'
    make_file()
    print(str(pageNo) + '페이지를 저장하였습니다.')