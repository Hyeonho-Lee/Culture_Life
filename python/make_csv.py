import json
import numpy as np
import pandas as pd

event_name = '행사명'
opar = '개최장소'
start_date = '시작일자'
end_date = '종료일자'
opar_info = '행사내용'
homepage_url = '홈페이지주소'
phone_number = '전화번호'
mnnst = '주관기관'
auspcInstt = '주최기관'
rdnmadr = '도로명주소'
lnmadr = '지번주소'
latitude = '위도'
longitude = '경도'

data = pd.DataFrame(columns=[event_name, opar, start_date, end_date, opar_info, homepage_url, phone_number, mnnst, auspcInstt, rdnmadr, lnmadr, latitude, longitude])

with open('../json/Second_Data/data_1.json', 'r') as file:
    text = json.load(file, strict=False)


def input_csv_second(value):
    
    global event_name
    global data
    
    json_index = value
    
    event_name_v = text['response']['body']['items'][json_index]['fstvlNm']
    if event_name_v == '' or event_name_v == 'null':
        event_name = ''
    
    opar_v = text['response']['body']['items'][json_index]['opar']
    if opar_v == '' or opar_v == 'null':
        opar_v = '-'
    
    start_date_v = text['response']['body']['items'][json_index]['fstvlStartDate']
    if start_date_v == '' or start_date_v == 'null':
        start_date_v = '-'
    
    end_date_v = text['response']['body']['items'][json_index]['fstvlEndDate']
    if end_date_v == '' or end_date_v == 'null':
        end_date_v = '-'
    
    opar_info_v = text['response']['body']['items'][json_index]['fstvlCo']
    if opar_info_v == '' or opar_info_v == 'null':
        opar_info_v = '-'
    
    homepage_url_v = text['response']['body']['items'][json_index]['homepageUrl']
    if homepage_url_v == '' or homepage_url_v == 'null':
        homepage_url_v = '-'
    
    phone_number_v = text['response']['body']['items'][json_index]['phoneNumber']
    if phone_number_v == '' or phone_number_v == 'null':
        phone_number_v = '-'
    
    mnnst_v = text['response']['body']['items'][json_index]['mnnst']
    if mnnst_v == '' or mnnst_v == 'null':
        mnnst_v = '-'
    
    auspcInstt_v = text['response']['body']['items'][json_index]['auspcInstt']
    if auspcInstt_v == '' or auspcInstt_v == 'null':
        auspcInstt_v = '-'
    
    rdnmadr_v = text['response']['body']['items'][json_index]['rdnmadr']
    if rdnmadr_v == '' or rdnmadr_v == 'null':
        rdnmadr_v = '-'
    
    lnmadr_v = text['response']['body']['items'][json_index]['lnmadr']
    if lnmadr_v == '' or lnmadr_v == 'null':
        lnmadr_v = '-'
    
    latitude_v = text['response']['body']['items'][json_index]['latitude']
    if latitude_v == '' or latitude_v == 'null':
        latitude_v = '-'
    
    longitude_v = text['response']['body']['items'][json_index]['longitude']
    if longitude_v == '' or longitude_v == 'null':
        longitude_v = '-'
    
    input_data =  {
        event_name : event_name_v,
        opar : opar_v,
        start_date : start_date_v,
        end_date : end_date_v,
        opar_info : opar_info_v,
        homepage_url :homepage_url_v,
        phone_number : phone_number_v,
        mnnst : mnnst_v,
        auspcInstt : auspcInstt_v,
        rdnmadr : rdnmadr_v,
        lnmadr : lnmadr_v,
        latitude : latitude_v,
        longitude : longitude_v
    }
    
    data = data.append(input_data, ignore_index=True)

def save_csv(index):
    path = '../json/Second_Data/data_' + str(index) + '.json'
    with open(path, 'r') as file:
        text = json.load(file, strict=False)
    
    for i in range(0, len(text['response']['body']['items'])):
        input_csv_second(i)

for i in range(1, 12):
    save_csv(i)

with open('../json/First_Data/data_1.json', 'r') as file:
    text = json.load(file, strict=False)

def input_csv_first(value):
    
    global event_name
    global data
    
    json_index = value
    
    event_name_v = text['response']['body']['items'][json_index]['eventNm']
    if event_name_v == '' or event_name_v == 'null':
        event_name = ''
    
    opar_v = text['response']['body']['items'][json_index]['opar']
    if opar_v == '' or opar_v == 'null':
        opar_v = '-'
    
    start_date_v = text['response']['body']['items'][json_index]['eventStartDate']
    if start_date_v == '' or start_date_v == 'null':
        start_date_v = '-'
    
    end_date_v = text['response']['body']['items'][json_index]['eventEndDate']
    if end_date_v == '' or end_date_v == 'null':
        end_date_v = '-'
    
    opar_info_v = text['response']['body']['items'][json_index]['eventCo']
    if opar_info_v == '' or opar_info_v == 'null':
        opar_info_v = '-'
    
    homepage_url_v = text['response']['body']['items'][json_index]['homepageUrl']
    if homepage_url_v == '' or homepage_url_v == 'null':
        homepage_url_v = '-'
    
    phone_number_v = text['response']['body']['items'][json_index]['phoneNumber']
    if phone_number_v == '' or phone_number_v == 'null':
        phone_number_v = '-'
    
    mnnst_v = text['response']['body']['items'][json_index]['mnnst']
    if mnnst_v == '' or mnnst_v == 'null':
        mnnst_v = '-'
    
    auspcInstt_v = text['response']['body']['items'][json_index]['auspcInstt']
    if auspcInstt_v == '' or auspcInstt_v == 'null':
        auspcInstt_v = '-'
    
    rdnmadr_v = text['response']['body']['items'][json_index]['rdnmadr']
    if rdnmadr_v == '' or rdnmadr_v == 'null':
        rdnmadr_v = '-'
    
    lnmadr_v = text['response']['body']['items'][json_index]['lnmadr']
    if lnmadr_v == '' or lnmadr_v == 'null':
        lnmadr_v = '-'
    
    latitude_v = text['response']['body']['items'][json_index]['latitude']
    if latitude_v == '' or latitude_v == 'null':
        latitude_v = '-'
    
    longitude_v = text['response']['body']['items'][json_index]['longitude']
    if longitude_v == '' or longitude_v == 'null':
        longitude_v = '-'
    
    input_data_2 =  {
        event_name : event_name_v,
        opar : opar_v,
        start_date : start_date_v,
        end_date : end_date_v,
        opar_info : opar_info_v,
        homepage_url :homepage_url_v,
        phone_number : phone_number_v,
        mnnst : mnnst_v,
        auspcInstt : auspcInstt_v,
        rdnmadr : rdnmadr_v,
        lnmadr : lnmadr_v,
        latitude : latitude_v,
        longitude : longitude_v
    }
    
    data = data.append(input_data_2, ignore_index=True)


def save_csv_2(index):
    path = '../json/First_Data/data_' + str(index) + '.json'
    with open(path, 'r') as file:
        text = json.load(file, strict=False)
    
    for i in range(0, len(text['response']['body']['items'])):
        input_csv_first(i)

for i in range(1, 21):
    save_csv_2(i)


data[start_date] = pd.to_datetime(data[start_date], format='%Y-%m-%d')
data.to_csv("csv_data.csv", mode='w', encoding='utf-8-sig')