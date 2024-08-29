# -*- coding: utf-8 -*-

from config import setting 
from utils.log import sportlogger
import json
import sys
sys.path.append('..')
import requests

from dao import sportinfo
from bs4 import BeautifulSoup
import time

from requests.exceptions import Timeout

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':'no-cache'
}

def getprematchbriefingdata():
    sportlogger.info("getprematchbriefingdata: func begin")


    data =  {
        "newsTypeId": "721", 
        "pageNumber": "1", 
        "newsId": "", 
        "hotTagId": "", 
        "fRptTime": "", 
        "fNewsId": "", 
        "fChkTime": ""
    }

    
    # {newsTypeId: "601", pageSize: "24", pageNumber: "1", hotTagId: ""}
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try:
        # xml_data = res.content
        # print("Content-Type=", res.headers['Content-Type'])
        sportlogger.info(f"getprematchbriefingdata: func begin11")       
        sportlogger.info(f"data0={data}")
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getprematchbriefingdata: status_code={res.status_code}")
        if res.status_code==200:
            data = res.json()['data']
            # print("data=",data['total'], " page=", data['pages'])
            # print("listinfo=",data['list'])
            # print("listlen=", len(data['list']))
            listinfo = data['list']
            sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']
                data =  {
                "newsTypeId": "721",
                "newsId": "",
                "pageNumber": str(pagenum),
                "hotTagId": "",
                "fChkTime":fChkTime,
                'fNewsId':fNewsId,
                "fRptTime":fRptTime
                }

                sportlogger.info(f"getprematchbriefingdata:data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getprematchbriefingdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getprematchbriefingdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getprematchbriefingdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getprematchbriefingdata: There was a problem: {exc}")

def getbasketballprematchbriefingdata():
    sportlogger.info("getbasketballprematchbriefingdata: func begin")
    data = {
            "newsTypeId": "94", 
            "pageNumber": "1", 
            "newsId": "", 
            "hotTagId": "", 
            "fRptTime": "", 
            "fNewsId": "", 
            "fChkTime": ""
        }
    
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try: 
        
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getbasketballprematchbriefingdata: status_code={res.status_code}")
        if res.status_code==200:
            sportlogger.info(f"res.json()={res.json()}")
            data = res.json()['data']
            sportlogger.info(f"data0={data}")
            # return
            listinfo = data['list']
            sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']
                data =  {
                "newsTypeId": "94",
                "newsId": "",
                "pageNumber": str(pagenum),
                "hotTagId": "",
                "fChkTime":fChkTime,
                'fNewsId':fNewsId,
                "fRptTime":fRptTime
                }

                # sportlogger.info(f"getbasketballprematchbriefingdata:data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getbasketballprematchbriefingdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getbasketballprematchbriefingdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballprematchbriefingdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballprematchbriefingdata: There was a problem: {exc}")

def getbasketballnewshighlightsdata():
    sportlogger.info("getbasketballnewshighlightsdata: func begin")
    data = {
            "newsTypeId": "96", 
            "pageNumber": "1", 
            "newsId": "", 
            "hotTagId": "", 
            "fRptTime": "", 
            "fNewsId": "", 
            "fChkTime": ""
        }
    
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try: 
        
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getbasketballprematchbriefingdata: status_code={res.status_code}")
        if res.status_code==200:
            sportlogger.info(f"res.json()={res.json()}")
            data = res.json()['data']
            sportlogger.info(f"data0={data}")
            # return
            listinfo = data['list']
            sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']
                data =  {
                "newsTypeId": "96",
                "newsId": "",
                "pageNumber": str(pagenum),
                "hotTagId": "",
                "fChkTime":fChkTime,
                'fNewsId':fNewsId,
                "fRptTime":fRptTime
                }

                # sportlogger.info(f"getbasketballprematchbriefingdata:data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getbasketballnewshighlightsdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getbasketballnewshighlightsdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballnewshighlightsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballnewshighlightsdata: There was a problem: {exc}")

def getbasketballpostmatchbriefingdata():
    sportlogger.info("getbasketballpostmatchbriefingdata: func begin")
    data = {
            "newsTypeId": "95", 
            "pageNumber": "1", 
            "newsId": "", 
            "hotTagId": "", 
            "fRptTime": "", 
            "fNewsId": "", 
            "fChkTime": ""
        }
    
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try: 
        
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getbasketballprematchbriefingdata: status_code={res.status_code}")
        if res.status_code==200:
            sportlogger.info(f"res.json()={res.json()}")
            data = res.json()['data']
            sportlogger.info(f"data0={data}")
            # return
            listinfo = data['list']
            sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']
                data =  {
                "newsTypeId": "95",
                "newsId": "",
                "pageNumber": str(pagenum),
                "hotTagId": "",
                "fChkTime":fChkTime,
                'fNewsId':fNewsId,
                "fRptTime":fRptTime
                }

                # sportlogger.info(f"getbasketballprematchbriefingdata:data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_basketball_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getbasketballpostmatchbriefingdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getbasketballpostmatchbriefingdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballpostmatchbriefingdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballpostmatchbriefingdata: There was a problem: {exc}")

def getpostmatchbriefingdata():
    sportlogger.info("getpostmatchbriefingdata: func begin")
    data = {
        "newsTypeId": "761", 
        "pageNumber": "1", 
        "newsId": "", 
        "hotTagId": "", 
        "fRptTime": "", 
        "fNewsId": "", 
        "fChkTime": ""
        }
    
    # {newsTypeId: "601", pageSize: "24", pageNumber: "1", hotTagId: ""}
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try:
        # xml_data = res.content
        # print("Content-Type=", res.headers['Content-Type'])
            
        sportlogger.info(f"getpostmatchbriefingdata: data0={data}")
        
        if setting.isuse_proxy == 1:          
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getpostmatchbriefingdata: status_code={res.status_code}")
        if res.status_code==200:
            data = res.json()['data']
            # print("data=",data['total'], " page=", data['pages'])
            # print("listinfo=",data['list'])
            # print("listlen=", len(data['list']))
            listinfo = data['list']
            sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']

                data = {
                    "newsTypeId": "761", 
                    "pageNumber": str(pagenum), 
                    "newsId": "", 
                    "hotTagId": "", 
                    "fRptTime": fRptTime, 
                    "fNewsId": fNewsId, 
                    "fChkTime": fChkTime
                    }

                # data =  {
                # "newsTypeId": "721",
                # "newsId": "",
                # "pageNumber": str(pagenum),
                # "hotTagId": "",
                # "fChkTime":fChkTime,
                # 'fNewsId':fNewsId,
                # "fRptTime":fRptTime
                # }

                sportlogger.info("getpostmatchbriefingdata: data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getpostmatchbriefingdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getpostmatchbriefingdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getpostmatchbriefingdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getpostmatchbriefingdata: There was a problem: {exc}")

def getnewshighlightsdata():
    sportlogger.info("getnewshighlightsdata: func begin")
    data = {
        "newsTypeId": "601", 
        "pageNumber": "1", 
        "newsId": "", 
        "hotTagId": "", 
        "fRptTime": "", 
        "fNewsId": "", 
        "fChkTime": ""
        }
    
    # {newsTypeId: "601", pageSize: "24", pageNumber: "1", hotTagId: ""}
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    
    try:
        # xml_data = res.content
        # print("Content-Type=", res.headers['Content-Type'])
            
        sportlogger.info(f"getnewshighlightsdata: data0={data}")
        
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getnewshighlightsdata: status_code={res.status_code}")
        if res.status_code==200:
            data = res.json()['data']
            # print("data=",data['total'], " page=", data['pages'])
            # print("listinfo=",data['list'])
            # print("listlen=", len(data['list']))
            listinfo = data['list']
            sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
            pagenum = 2
            totalcnt = 1
            while True:
                fChkTime = data['fChkTime']
                fNewsId = data['fNewsId']
                fRptTime = data['fRptTime']

                data = {
                    "newsTypeId": "761", 
                    "pageNumber": str(pagenum), 
                    "newsId": "", 
                    "hotTagId": "", 
                    "fRptTime": fRptTime, 
                    "fNewsId": fNewsId, 
                    "fChkTime": fChkTime
                    }

                # data =  {
                # "newsTypeId": "721",
                # "newsId": "",
                # "pageNumber": str(pagenum),
                # "hotTagId": "",
                # "fChkTime":fChkTime,
                # 'fNewsId':fNewsId,
                # "fRptTime":fRptTime
                # }

                sportlogger.info(f"getnewshighlightsdata: data1={data}")
                if fChkTime == "-1" or fRptTime == "-1":
                    break;
                totalcnt = totalcnt + 1
                if totalcnt >= 1000:
                    break
                try:
                    if setting.isuse_proxy == 1:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, proxies=proxies, timeout=10)
                    else:
                        res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/newsdlist", json=data,headers=headers, timeout=10)
                    if res.status_code==200:
                        data = res.json()['data']
                        listinfo = data['list']
                        sportinfo.insert_news_info(listinfo, res.json()['sysTime'])
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getnewshighlightsdata: 请求超时，请重试！")
                    time.sleep(2)
                    # totalcnt = totalcnt + 1
                    continue
                except Exception as exc:
                    sportlogger.info(f"getnewshighlightsdata: There was a problem: {exc}")
                    # totalcnt = totalcnt + 1
                    time.sleep(2)
                    continue
                time.sleep(2)
                # totalcnt = totalcnt + 1
                pagenum = pagenum+1
            # with open("news.txt","w",encoding="utf-8") as file:
            #     # 将每页网页的内容存进listpage文件夹中
            #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getnewshighlightsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getnewshighlightsdata: There was a problem: {exc}")

def getscoreinfo():
    data =  {
        }
        
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }

    # print("proxies=", proxies)
    try:
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/matchs/results", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/matchs/results", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getscoreinfo: json={res.json()}")
        # # print("Content-Type=", res.headers['Content-Type'])
        # # print("data=",data['total'], " page=", data['pages'])
        # # # print("listinfo=",data['list'])
        # # # print("listlen=", len(data['list']))
        if res.status_code==200:
            data = res.json()['data']
            listinfo = data['list']
            tmptimeinfo = res.json()['sysTime']
            sportinfo.insert_score_maindata(listinfo, tmptimeinfo)
            
            for data in listinfo:
                sportlogger.info(f"getscoreinfo: currentPeriodStart={data['currentPeriodStart']} currentscore={data['score']['current']} hometeamName={data['hometeamName']} awayteamName={data['awayteamName']} matchId={data['matchId']}")
                if data['score']['current'] == "0:0":
                    continue;
                try:
                    datainfo =  {
                        "matchId": data['matchId'], 
                        "type": "ft"
                        }
                    
                    sportlogger.info(f"datainfo={datainfo}")
                    if setting.isuse_proxy == 1:
                        resgoalcard = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/matchs/goalcard", json=datainfo,headers=headers, proxies=proxies, timeout=10)
                    else:
                        resgoalcard = requests.post("https://www.macauslot.com/infoApi/cn/D/FB/matchs/goalcard", json=datainfo,headers=headers, timeout=10)
                    if resgoalcard.status_code==200:
                        sportlogger.info(f"getscoreinfo:resgoalcard={resgoalcard.json()}")
                        data = resgoalcard.json()['data']
                        datalist = data['list'];
                        sysTime = resgoalcard.json()['sysTime']
                        sportinfo.insert_score_info(datalist, sysTime)
                    time.sleep(2)
                except Timeout:
                    # 请求超时处理
                    sportlogger.info("getscoreinfo:请求超时，请重试！")
                    time.sleep(2)
                except Exception as exc:
                    sportlogger.info(f"getscoreinfo: There was a problem: {exc}")
                    time.sleep(2)
        
        # with open("news.txt","w",encoding="utf-8") as file:
        #     # 将每页网页的内容存进listpage文件夹中
        #     file.write(res.text)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getscoreinfo: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getscoreinfo: There was a problem: {exc}")

def getbasketballscoreinfo():
    data =  {
        }
        
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }

    # print("proxies=", proxies)
    try:
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/matchs/livescore", json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/infoApi/cn/D/BB/matchs/livescore", json=data,headers=headers, timeout=10)
        sportlogger.info(f"getbasketballscoreinfo: json={res.json()}")
       
        if res.status_code==200:
            print("data=", res.json())
            data = res.json()['data']
            listinfo = data['list']
            tmptimeinfo = res.json()['sysTime']
            sportinfo.insert_basketball_score_data(listinfo, tmptimeinfo)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballscoreinfo: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballscoreinfo: There was a problem: {exc}")

def getOddsdata():
    sportlogger.info("getOddsdata: func begin")
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
    "http": proxyMeta,
    "https": proxyMeta
}
    data =  {
        "nocache":1720833165134
        }


    # sportlogger.info("proxies=", proxies)
    arrhomeawayinfo = []
    try:
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/soccer/json/realtime/threeinone_event_cn_fb.json", 
                            json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/soccer/json/realtime/threeinone_event_cn_fb.json", 
                            json=data,headers=headers, timeout=10)
        if res.status_code==200:
            # print("json=", res.json())
            for data in res.json()['data']:
                event = data['event']
                sportlogger.info(f"home_team={event['home_team']} away_team={event['away_team']} eventname={event['eventType']['name']} ev_id={event['ev_id']}")
                homeawayinfo = {
                    "home_team":event['home_team'],
                    "away_team":event['away_team'],
                    "eventname":event['eventType']['name'],
                    "ev_id":event['ev_id'],
                    "start_time":event['start_time'],
                    "systime":res.json()['systime']
                }

                arrhomeawayinfo.append(homeawayinfo)


            arrleagueabbreviation = []
            for data in res.json()['odds_config']:
                # print("BETTING_ID=", data['BETTING_ID'], " TS=", data['TS'], " SS=", data['SS'])
                leagueabbreviation = {
                    "BETTING_ID":str(data['BETTING_ID']),
                    "TS":data['TS'],
                    "SS":data['SS']
                }

                arrleagueabbreviation.append(leagueabbreviation)
            

            for homeawayinfo in arrhomeawayinfo:
                for leagueabbreviation in arrleagueabbreviation:
                    if leagueabbreviation['BETTING_ID'] == None:
                        continue
                    # print("************ ev_id=", homeawayinfo['ev_id'], " BETTING_ID=", leagueabbreviation['BETTING_ID'])
                    if homeawayinfo['ev_id'] == leagueabbreviation['BETTING_ID']:
                        # print("i have ev_id=", homeawayinfo['ev_id'], " TS=", leagueabbreviation['TS'])
                        homeawayinfo['leagueabbreviation'] = leagueabbreviation['TS']
                        break
    except Timeout:
        # 请求超时处理
        sportlogger.info("getOddsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getOddsdata: There was a problem: {exc}")

    # return

    try:
        if setting.isuse_proxy == 1:
            res = requests.post("https://www.macauslot.com/soccer/json/realtime/threeinone_odds_cn_fb.json", 
                            json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/soccer/json/realtime/threeinone_odds_cn_fb.json", 
                            json=data,headers=headers, timeout=10)
        # print("json=", res.json())
        
        allodddata = []
        for data in res.json()['data']:
            markets = data['markets']
            ev_id = data['ev_id']
            StandardHomeRate = ""
            StandardawayRate = ""
            StandarddrawRate = "" #平局

            HandicapHomeRate = ""
            HandicapawayRate = ""
            Handicapawayhcapdisp = ""

            UpperlowerplateHomeRate = ""
            UpperlowerplateawayRate = ""
            Upperlowerawayhcapdisp = ""
            HomeName = ""
            AwayName = ""
            for marketsinfo in markets:
                # print("marketsinfo11=", marketsinfo, "  name123=", marketsinfo['name'])
                if "標準盤" == marketsinfo['name']:
                    sportlogger.info(f"have 標準盤 marketsinfo={marketsinfo}")
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            StandardHomeRate = outcomesinfo['rate']
                        elif outcomesinfo['type'] == "D":
                            StandarddrawRate =  outcomesinfo['rate']
                        elif outcomesinfo['type'] == "A":
                            StandardawayRate = outcomesinfo['rate']
                    
                elif "讓球盤" == marketsinfo['name']:
                    sportlogger.info(f"have 讓球盤 marketsinfo={marketsinfo}")
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            HandicapHomeRate = outcomesinfo['rate']
                            HomeName = outcomesinfo['desc']
                        elif outcomesinfo['type'] == "A":
                            HandicapawayRate = outcomesinfo['rate']
                            AwayName = outcomesinfo['desc']
                    Handicapawayhcapdisp = marketsinfo['away_hcap_disp']
                elif "上/下盤" == marketsinfo['name']:
                    sportlogger.info(f"have 上/下盤 marketsinfo={marketsinfo}")
                    # sportlogger.info("have 上/下盤 marketsinfo=", marketsinfo)
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            UpperlowerplateHomeRate = outcomesinfo['rate']
                        elif outcomesinfo['type'] == "A":
                            UpperlowerplateawayRate = outcomesinfo['rate']
                    Upperlowerawayhcapdisp = marketsinfo['away_hcap_disp']
            iteminfo = {
                "ev_id":ev_id,
                "StandardHomeRate":StandardHomeRate,
                "StandardawayRate":StandardawayRate,
                "StandarddrawRate":StandarddrawRate,
                "HandicapHomeRate":HandicapHomeRate,
                "HandicapawayRate":HandicapawayRate,
                "Handicapawayhcapdisp":Handicapawayhcapdisp,
                "UpperlowerplateHomeRate":UpperlowerplateHomeRate,
                "UpperlowerplateawayRate":UpperlowerplateawayRate,
                "Upperlowerawayhcapdisp":Upperlowerawayhcapdisp,
                "HomeName":HomeName,
                "AwayName":AwayName,
                "eventname":"", 
                "start_time":"",
                "systime":""
            }

            for tmpdata in arrhomeawayinfo:
                if tmpdata['ev_id'] == ev_id:
                    iteminfo["HomeName"] = tmpdata["home_team"]
                    iteminfo["AwayName"] = tmpdata["away_team"]
                    # iteminfo["eventname"] = tmpdata["eventname"]
                    iteminfo["eventname"] = tmpdata["leagueabbreviation"]
                    iteminfo["start_time"] = tmpdata["start_time"]
                    iteminfo["systime"] = tmpdata["systime"]
                    break
                
            allodddata.append(iteminfo)

        sportinfo.insert_odds_data(allodddata)
            # print("data=", data)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getOddsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getOddsdata: There was a problem: {exc}")

def getbasketballOddsdata():
    sportlogger.info("getbasketballOddsdata: func begin")
    proxyMeta = 'socks5://customer-c7590e:13c780cc@proxy.ipipgo.com:31212'
    proxies = {
    "http": proxyMeta,
    "https": proxyMeta
    }

    
    data =  {
        "nocache":1721992020002
        }


    # sportlogger.info("proxies=", proxies)
    arrhomeawayinfo = []
    
    try:
        if setting.isuse_proxy == 1:
            
            res = requests.post("https://www.macauslot.com/nba/json/realtime/threeinone_event_cn_bb.json", 
                            json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/nba/json/realtime/threeinone_event_cn_bb.json", 
                            json=data,headers=headers, timeout=10)
        if res.status_code==200:
            print("json=", res.json())
            for data in res.json()['data']:
                event = data['event']
                sportlogger.info(f"getbasketballOddsdata home_team={event['home_team']} away_team={event['away_team']} eventname={event['eventType']['name']} ev_id={event['ev_id']}")
                homeawayinfo = {
                    "home_team":event['home_team'],
                    "away_team":event['away_team'],
                    "eventname":event['eventType']['name'],
                    "ev_id":event['ev_id'],
                    "start_time":event['start_time'],
                    "systime":res.json()['systime']
                }

                arrhomeawayinfo.append(homeawayinfo)


            arrleagueabbreviation = []
            for data in res.json()['odds_config']:
                # print("BETTING_ID=", data['BETTING_ID'], " TS=", data['TS'], " SS=", data['SS'])
                leagueabbreviation = {
                    "BETTING_ID":str(data['BETTING_ID']),
                    "TS":data['TS'],
                    "SS":data['SS']
                }

                arrleagueabbreviation.append(leagueabbreviation)
            

            for homeawayinfo in arrhomeawayinfo:
                for leagueabbreviation in arrleagueabbreviation:
                    if leagueabbreviation['BETTING_ID'] == None:
                        continue
                    # print("************ ev_id=", homeawayinfo['ev_id'], " BETTING_ID=", leagueabbreviation['BETTING_ID'])
                    if homeawayinfo['ev_id'] == leagueabbreviation['BETTING_ID']:
                        # print("i have ev_id=", homeawayinfo['ev_id'], " TS=", leagueabbreviation['TS'])
                        homeawayinfo['leagueabbreviation'] = leagueabbreviation['TS']
                        break
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballOddsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballOddsdata: There was a problem: {exc}")

    # return

    # https://www.macauslot.com/nba/json/realtime/threeinone_odds_cn_bb.json?nocache=1721992020002
    try:
        if setting.isuse_proxy == 1:
            
            res = requests.post("https://www.macauslot.com/nba/json/realtime/threeinone_odds_cn_bb.json", 
                            json=data,headers=headers, proxies=proxies, timeout=10)
        else:
            res = requests.post("https://www.macauslot.com/nba/json/realtime/threeinone_odds_cn_bb.json", 
                            json=data,headers=headers, timeout=10)
        # print("json=", res.json())
        
        allodddata = []
        for data in res.json()['data']:
            markets = data['markets']
            ev_id = data['ev_id']
            StandardHomeRate = ""
            StandardawayRate = ""
            StandarddrawRate = "" #平局

            HandicapHomeRate = ""
            HandicapawayRate = ""
            Handicapawayhcapdisp = ""

            UpperlowerplateHomeRate = ""
            UpperlowerplateawayRate = ""
            Upperlowerawayhcapdisp = ""
            HomeName = ""
            AwayName = ""
            for marketsinfo in markets:
                # print("marketsinfo11=", marketsinfo, "  name123=", marketsinfo['name'])
                # if "標準盤" == marketsinfo['name']:
                if "ML" == marketsinfo['sort']:
                    sportlogger.info(f"have 標準盤 marketsinfo={marketsinfo}")
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            StandardHomeRate = outcomesinfo['rate']
                        elif outcomesinfo['type'] == "D":
                            StandarddrawRate =  outcomesinfo['rate']
                        elif outcomesinfo['type'] == "A":
                            StandardawayRate = outcomesinfo['rate']
                    
                # elif "讓球盤" == marketsinfo['name']:
                elif "WH" == marketsinfo['sort']:
                    sportlogger.info(f"have 讓分盤 marketsinfo={marketsinfo}")
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            HandicapHomeRate = outcomesinfo['rate']
                            HomeName = outcomesinfo['desc']
                        elif outcomesinfo['type'] == "A":
                            HandicapawayRate = outcomesinfo['rate']
                            AwayName = outcomesinfo['desc']
                    Handicapawayhcapdisp = marketsinfo['away_hcap_disp']
                elif "HL" == marketsinfo['sort']:
                    sportlogger.info(f"have 上/下盤 (全場總得分) marketsinfo={marketsinfo}")
                    outcomes = marketsinfo['outcomes']
                    for outcomesinfo in outcomes:
                        if outcomesinfo['type'] == "H":
                            UpperlowerplateHomeRate = outcomesinfo['rate']
                        elif outcomesinfo['type'] == "A":
                            UpperlowerplateawayRate = outcomesinfo['rate']
                    Upperlowerawayhcapdisp = marketsinfo['away_hcap_disp']
            iteminfo = {
                "ev_id":ev_id,
                "StandardHomeRate":StandardHomeRate,
                "StandardawayRate":StandardawayRate,
                "StandarddrawRate":StandarddrawRate,
                "HandicapHomeRate":HandicapHomeRate,
                "HandicapawayRate":HandicapawayRate,
                "Handicapawayhcapdisp":Handicapawayhcapdisp,
                "UpperlowerplateHomeRate":UpperlowerplateHomeRate,
                "UpperlowerplateawayRate":UpperlowerplateawayRate,
                "Upperlowerawayhcapdisp":Upperlowerawayhcapdisp,
                "HomeName":HomeName,
                "AwayName":AwayName,
                "eventname":"", 
                "start_time":"",
                "systime":""
            }

            for tmpdata in arrhomeawayinfo:
                if tmpdata['ev_id'] == ev_id:
                    iteminfo["HomeName"] = tmpdata["home_team"]
                    iteminfo["AwayName"] = tmpdata["away_team"]
                    # iteminfo["eventname"] = tmpdata["eventname"]
                    iteminfo["eventname"] = tmpdata["leagueabbreviation"]
                    iteminfo["start_time"] = tmpdata["start_time"]
                    iteminfo["systime"] = tmpdata["systime"]
                    break
                
            allodddata.append(iteminfo)

        sportinfo.insert_odds_data(allodddata)
            # print("data=", data)
    except Timeout:
        # 请求超时处理
        sportlogger.info("getbasketballOddsdata: 请求超时，请重试！")
    except Exception as exc:
        sportlogger.info(f"getbasketballOddsdata: There was a problem: {exc}")


def basketball_odds_start():
    sportlogger.info(f"query_odds_interval={setting.query_odds_interval} query_new_interval={setting.query_new_interval} query_main_score_interval={setting.query_main_score_interval}")
    getbasketballprematchbriefingdata()
    getbasketballpostmatchbriefingdata()
    getbasketballnewshighlightsdata()
    getbasketballscoreinfo()
    getbasketballOddsdata()
    return

def odds_start():
    sportlogger.info(f"query_odds_interval={setting.query_odds_interval} query_new_interval={setting.query_new_interval} query_main_score_interval={setting.query_main_score_interval}")
    # getbasketballprematchbriefingdata()
    # getbasketballpostmatchbriefingdata()
    # getbasketballnewshighlightsdata()
    # getbasketballscoreinfo()
    # getbasketballOddsdata()
    # return
    # return
    # getOddsdata()
    # getscoreinfo()
    getprematchbriefingdata()
    return
    # getpostmatchbriefingdata()
    # getnewshighlightsdata()

    odds_timestamp = int(time.time())
    score_timestamp = int(time.time())
    new_timestamp = int(time.time())
    
    while True:
        current_timestamp = time.time()
        seconds_since_1970 = int(current_timestamp)
        timediff = seconds_since_1970 - odds_timestamp
        if timediff >= setting.query_odds_interval:
            getOddsdata()
            odds_timestamp = int(time.time())

        timediff = seconds_since_1970 - score_timestamp
        if timediff >= setting.query_main_score_interval:
            getscoreinfo()
            score_timestamp = int(time.time())


        timediff = seconds_since_1970 - new_timestamp
        if timediff >= setting.query_new_interval:
            getprematchbriefingdata()
            getpostmatchbriefingdata()
            getnewshighlightsdata()
            new_timestamp = int(time.time())
    # getOddsdata()
    # getscoreinfo()
    
        time.sleep(1)
