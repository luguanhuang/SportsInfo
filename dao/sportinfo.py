from utils.sql_helper import sql_helper
# from utils.sql_helper import db2_sql_helper
from utils.log import sportlogger
from utils.log import sportguilogger
import time

def insert_news_info(listinfo, sysTime):
    for data in listinfo:
        sportlogger.info(f"insert_news_info: datatag={data['tags']} imageUri={data['imageUri']}  title={data['title']} reportTime={data['reportTime']} images={data['images']}")
        titleinfo = data['images'][0]['title']
        sql = """
        SELECT * FROM newsinfo where title=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['title']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sametitletime = data['reportTime']
            if resdata['sametitletime'] != None:
                if sametitletime in resdata['sametitletime']:
                    sametitletime = resdata['sametitletime']
                else:
                    sametitletime = resdata['sametitletime']  + ","+data['reportTime']
            sql = """
                update newsinfo set reportTime=%s, imageUri=%s, newsTypeName=%s, content=%s, sysTime=%s, subtitle=%s, sametitletime=%s  where title=%s
                """
            print(f"sql={sql}")
            ret = sql_helper.update(sql, (data['reportTime'], data['imageUri'], data['newsTypeSimpleName'], data['content'],
                                                sysTime, titleinfo, sametitletime, data['title']))
        else:
            sql = """
                insert into newsinfo(title, reportTime, imageUri, newsTypeName, content, sysTime, subtitle, sametitletime) values(%s,%s,%s,%s,%s, %s, %s, %s)
                """
            print(f"sql111={sql}")   
            # ret = sql_helper.update(sql, (data['title'], data['reportTime'], data['imageUri'], 
            #                                     data['images'], data['newsTypeName'], data['content']))
            ret = sql_helper.update(sql, (data['title'], data['reportTime'], data['imageUri'], data['newsTypeSimpleName'], data['content'], sysTime,
                                          titleinfo, data['reportTime']))

def insert_basketball_news_info(listinfo, sysTime):
    for data in listinfo:
        sportlogger.info(f"insert_basketball_news_info: datatag={data['tags']} imageUri={data['imageUri']}  title={data['title']} reportTime={data['reportTime']} images={data['images']}")
        titleinfo = data['images'][0]['title']
        sql = """
        SELECT * FROM basketballnewsinfo where title=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['title']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sametitletime = data['reportTime']
            if resdata['sametitletime'] != None:
                if sametitletime in resdata['sametitletime']:
                    sametitletime = resdata['sametitletime']
                else:
                    sametitletime = resdata['sametitletime']  + ","+data['reportTime']
            sql = """
                update basketballnewsinfo set reportTime=%s, imageUri=%s, newsTypeName=%s, content=%s, sysTime=%s, subtitle=%s, sametitletime=%s  where title=%s
                """
            print(f"sql={sql}")
            ret = sql_helper.update(sql, (data['reportTime'], data['imageUri'], data['newsTypeSimpleName'], data['content'],
                                                sysTime, titleinfo, sametitletime, data['title']))
        else:
            sql = """
                insert into basketballnewsinfo(title, reportTime, imageUri, newsTypeName, content, sysTime, subtitle, sametitletime) values(%s,%s,%s,%s,%s, %s, %s, %s)
                """
            print(f"sql111={sql}")   
            # ret = sql_helper.update(sql, (data['title'], data['reportTime'], data['imageUri'], 
            #                                     data['images'], data['newsTypeName'], data['content']))
            ret = sql_helper.update(sql, (data['title'], data['reportTime'], data['imageUri'], data['newsTypeSimpleName'], data['content'], sysTime,
                                          titleinfo, data['reportTime']))


def insert_score_maindata(listinfo, sysTime):
    for data in listinfo:
        sportlogger.info(f"currentPeriodStart={data['currentPeriodStart']} currentscore={data['score']['current']} hometeamName={data['hometeamName']} awayteamName={data['awayteamName']} sysTime={sysTime}")
        sql = """
        SELECT * FROM scoremaindata where currentPeriodStart=%s and hometeamName=%s and awayteamName=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['currentPeriodStart'], data['hometeamName'], 
                                    data['awayteamName']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sql = """
                update scoremaindata set cornerscore=%s, currentscore=%s, matchId=%s, startDate=%s, lastUpdateTime=%s where currentPeriodStart=%s and hometeamName=%s and awayteamName=%s
                """
            sportlogger.info(f"sql={sql}")
            ret = sql_helper.update(sql, (data['corner']['current'], data['score']['current'], data['matchId'], data['startDate'], data['lastUpdateTime'],
                                          data['currentPeriodStart'], data['hometeamName'], data['awayteamName']))
        else:
            sql = """
                insert into scoremaindata(currentPeriodStart, currentscore, hometeamName, awayteamName, sysTime, cornerscore, matchId, startDate, lastUpdateTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            sportlogger.info(f"sql111={sql}")   
            ret = sql_helper.update(sql, (data['currentPeriodStart'], data['score']['current'], data['hometeamName'], data['awayteamName'], sysTime,
                                            data['corner']['current'], data['matchId'], data['startDate'], data['lastUpdateTime']))
            
def insert_basketball_score_data(listinfo, sysTime):
    for data in listinfo:
        # print("data['hcap']['ftHandicap']=", data['hcap']['ftHandicap'])
        # sportlogger.info(f"currentPeriodStart={data['currentPeriodStart']} currentscore={data['score']['current']} hometeamName={data['hometeamName']} awayteamName={data['awayteamName']} sysTime={sysTime}")

        ftHandicap = ""
        htHandicap = ""
        htOverUnder = ""
        ftOverUnder = ""

        scoreq1 = ""
        scoreq2 = ""
        scoreq3 = ""
        scoreq4 = ""
        scorecurrent = ""
        scorefh = ""
        scoresh = ""

        if "hcap" in data:
            print("11")
            if "ftHandicap" in data['hcap']:
                ftHandicap = data['hcap']['ftHandicap']
            if "htHandicap" in data['hcap']:
                htHandicap = data['hcap']['htHandicap']
            if "htOverUnder" in data['hcap']:
                htOverUnder = data['hcap']['htOverUnder']
            if "ftOverUnder" in data['hcap']:
                ftOverUnder = data['hcap']['ftOverUnder']
                    
        if "score" in data:
            print("22")
            if "q1" in data['score']:
                scoreq1 = data['score']['q1']
            if "q2" in data['score']:
                scoreq2 = data['score']['q2']
            if "q3" in data['score']:
                scoreq3 = data['score']['q3']
            if "q4" in data['score']:
                scoreq4 = data['score']['q4']
            if "current" in data['score']:
                scorecurrent = data['score']['current']
            if "fh" in data['score']:
                scorefh = data['score']['fh']
            if "sh" in data['score']:
                scoresh = data['score']['sh']

        sql = """
        SELECT * FROM basketballscoredata where startDate=%s and hometeamName=%s and awayteamName=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['startDate'], data['hometeamName'], 
                                    data['awayteamName']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sql = """
                update basketballscoredata set sysTime=%s, lastUpdateTime=%s, leaguename=%s, ftHandicap=%s, htHandicap=%s, htOverUnder=%s, ftOverUnder=%s, currentState=%s, scoreq1=%s, scoreq2=%s, scoreq3=%s, scoreq4=%s, scorecurrent=%s, scorefh=%s, scoresh=%s where startDate=%s and hometeamName=%s and awayteamName=%s
                """
            sportlogger.info(f"sql={sql}")
            ret = sql_helper.update(sql, (sysTime, data['lastUpdateTime'], data['uqTournament']['name'], ftHandicap, htHandicap, htOverUnder, ftOverUnder, 
                                          data['currentState'], scoreq1, scoreq2, scoreq3, scoreq4
                                            , scorecurrent, scorefh, scoresh,data['startDate'], data['hometeamName'], data['awayteamName']))
        else:
            sql = """
                insert into basketballscoredata(hometeamName, awayteamName, sysTime, startDate, lastUpdateTime, leaguename, ftHandicap, htHandicap, htOverUnder, ftOverUnder, currentState, scoreq1, scoreq2, scoreq3, scoreq4, scorecurrent, scorefh, scoresh) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

            sportlogger.info(f"sql111={sql}")   

            ret = sql_helper.update(sql, (data['hometeamName'], data['awayteamName'], sysTime,
                                            data['startDate'], data['lastUpdateTime'], data['uqTournament']['name'], ftHandicap, htHandicap, htOverUnder
                                            , ftOverUnder, data['currentState'], scoreq1, scoreq2, scoreq3, scoreq4
                                            , scorecurrent, scorefh, scoresh))

def insert_score_info(listinfo, sysTime):
    for data in listinfo:
        sportlogger.info(f"matchId={data['matchId']} teamId={data['teamId']} clock={data['clock']} typeCode={data['typeCode']}")
        sql = """
        SELECT * FROM scoreinfo where matchId=%s and teamId=%s and clock=%s and typeCode=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['matchId'], data['teamId'], 
                                    data['clock'], data['typeCode']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            i=1
            sql = """
                update scoreinfo set teamId=%s, clock=%s, typeCode=%s, sysTime=%s where matchId=%s
                """
            sportlogger.info(f"sql={sql}")
            ret = sql_helper.update(sql, (data['teamId'], data['clock'], data['typeCode'], sysTime,data['matchId']))
        else:
            sql = """
                insert into scoreinfo(matchId, teamId, clock, typeCode, sysTime) values(%s,%s,%s,%s,%s)
                """
            sportlogger.info(f"sql111={sql}")   
            ret = sql_helper.update(sql, (data['matchId'], data['teamId'], data['clock'], data['typeCode'], sysTime))



def insert_basketball_odds_data(allodddata):
    for data in allodddata:
        # print("matchId=", data['matchId'], " teamId=", data['teamId'], ' clock=', data['clock'], ' typeCode=', data['typeCode'])
        sql = """
        SELECT * FROM oddsdataoddsdata where ev_id=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['ev_id']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sql = """
                update oddsdataoddsdata set HomeName=%s, AwayName=%s, StandardHomeRate=%s, StandardawayRate=%s, StandarddrawRate=%s, HandicapHomeRate=%s, HandicapawayRate=%s, Handicapawayhcapdisp=%s, UpperlowerplateHomeRate=%s, UpperlowerplateawayRate=%s, Upperlowerawayhcapdisp=%s, eventname=%s, start_time=%s, systime=%s where ev_id=%s
                """
            sportlogger.info(f"sql={sql}")
            ret = sql_helper.update(sql, (data['HomeName'], data['AwayName'], data['StandardHomeRate'], data['StandardawayRate'], data['StandarddrawRate'], data['HandicapHomeRate'], 
                                          data['HandicapawayRate'], data['Handicapawayhcapdisp'], data['UpperlowerplateHomeRate'], data['UpperlowerplateawayRate'], data['Upperlowerawayhcapdisp'], 
                                          data['eventname'], data['start_time'], data['systime'], data['ev_id']))
        else:
            sql = """
                insert into oddsdataoddsdata(ev_id, HomeName, AwayName, StandardHomeRate, StandardawayRate, StandarddrawRate, HandicapHomeRate, HandicapawayRate, Handicapawayhcapdisp, UpperlowerplateHomeRate, UpperlowerplateawayRate, Upperlowerawayhcapdisp, eventname, start_time, systime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            sportlogger.info(f"sql111={sql}")   
            ret = sql_helper.update(sql, (data['ev_id'], data['HomeName'], data['AwayName'], data['StandardHomeRate'], data['StandardawayRate'], data['StandarddrawRate'], data['HandicapHomeRate'], 
                                          data['HandicapawayRate'], data['Handicapawayhcapdisp'], data['UpperlowerplateHomeRate'], data['UpperlowerplateawayRate'], data['Upperlowerawayhcapdisp'], 
                                          data['eventname'], data['start_time'], data['systime']))
            
def insert_odds_data(allodddata):
    for data in allodddata:
        # print("matchId=", data['matchId'], " teamId=", data['teamId'], ' clock=', data['clock'], ' typeCode=', data['typeCode'])
        sql = """
        SELECT * FROM oddsdata where ev_id=%s
        """
        resdata = sql_helper.fetch_one(sql, (data['ev_id']))
        cnt = 0
        if resdata is not None and resdata != False:
            cnt = len(resdata)

        if (cnt > 0):
            sql = """
                update oddsdata set HomeName=%s, AwayName=%s, StandardHomeRate=%s, StandardawayRate=%s, StandarddrawRate=%s, HandicapHomeRate=%s, HandicapawayRate=%s, Handicapawayhcapdisp=%s, UpperlowerplateHomeRate=%s, UpperlowerplateawayRate=%s, Upperlowerawayhcapdisp=%s, eventname=%s, start_time=%s, systime=%s where ev_id=%s
                """
            sportlogger.info(f"sql={sql}")
            ret = sql_helper.update(sql, (data['HomeName'], data['AwayName'], data['StandardHomeRate'], data['StandardawayRate'], data['StandarddrawRate'], data['HandicapHomeRate'], 
                                          data['HandicapawayRate'], data['Handicapawayhcapdisp'], data['UpperlowerplateHomeRate'], data['UpperlowerplateawayRate'], data['Upperlowerawayhcapdisp'], 
                                          data['eventname'], data['start_time'], data['systime'], data['ev_id']))
        else:
            sql = """
                insert into oddsdata(ev_id, HomeName, AwayName, StandardHomeRate, StandardawayRate, StandarddrawRate, HandicapHomeRate, HandicapawayRate, Handicapawayhcapdisp, UpperlowerplateHomeRate, UpperlowerplateawayRate, Upperlowerawayhcapdisp, eventname, start_time, systime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            sportlogger.info(f"sql111={sql}")   
            ret = sql_helper.update(sql, (data['ev_id'], data['HomeName'], data['AwayName'], data['StandardHomeRate'], data['StandardawayRate'], data['StandarddrawRate'], data['HandicapHomeRate'], 
                                          data['HandicapawayRate'], data['Handicapawayhcapdisp'], data['UpperlowerplateHomeRate'], data['UpperlowerplateawayRate'], data['Upperlowerawayhcapdisp'], 
                                          data['eventname'], data['start_time'], data['systime']))


def query_odds_data(from_time_str, to_time_str, arrleaguename, newtitle):
    sportguilogger.info("query_odds_data: func begin")
    today = time.localtime()
    threedays_timestamp = time.mktime(today) - 3*86400
    threedays = time.localtime(threedays_timestamp)
    timebegin = time.strftime('%Y-%m-%d 00:00:00', threedays)
    timeend = time.strftime('%Y-%m-%d 23:59:59', today)
    resdata = ""
    strtmp = ""
    sql = ""
    # leaguename

    sql = """
        select oa.start_time,oa.eventname,oa.HomeName, oa.AwayName, oa.Handicapawayhcapdisp, oa.HandicapHomeRate,oa.HandicapawayRate, sd.currentscore from oddsdata oa left join scoremaindata sd on oa.HomeName = sd.hometeamName and oa.AwayName=sd.awayteamName and oa.start_time= sd.startDate  where oa.start_time>= '{0}' and oa.start_time <= '{1}'
    """
    sql = sql.format(from_time_str, to_time_str)
    if len(arrleaguename) > 0:
    # if leaguename!="":
        sql = sql + " and  eventname in("
        for name in arrleaguename:
            sql = sql + "'"+name+"',"
        sql = sql[:-1]
        sql = sql + ")"
    print("sql=", sql)

    # if leaguename!="":
    #     strparam="  and  eventname=%s"
    #     # if newtitle != "":
    #     sql = "select oa.start_time,oa.eventname,oa.HomeName, oa.AwayName, oa.Handicapawayhcapdisp, oa.HandicapHomeRate,oa.HandicapawayRate, sd.currentscore from oddsdata oa left join scoremaindata sd on oa.HomeName = sd.hometeamName and oa.AwayName=sd.awayteamName and oa.start_time= sd.startDate  where oa.start_time>= %s and oa.start_time <= %s" + strparam
    #     # strparam = "(from_time_str, to_time_str, leaguename)"
    #     strtmp = (from_time_str, to_time_str, leaguename)
        
    # else:
    #     strtmp = (from_time_str, to_time_str)
    #     sql = """
    #     select oa.start_time,oa.eventname,oa.HomeName, oa.AwayName, oa.Handicapawayhcapdisp, oa.HandicapHomeRate,oa.HandicapawayRate, sd.currentscore from oddsdata oa left join scoremaindata sd on oa.HomeName = sd.hometeamName and oa.AwayName=sd.awayteamName and oa.start_time= sd.startDate  where oa.start_time>= %s and oa.start_time <= %s
    # """
    
    
    resdata = sql_helper.fetch_all_noparam(sql)

    cnt = 0
    if resdata is not None and resdata != False:
        cnt = len(resdata)

    
    arroddsdata = []
    if 0 == cnt:
        return arroddsdata
    for row in resdata:
        currentscore = ""
        if row['currentscore'] is not None:
            currentscore = row['currentscore']
        tmpdata = {
            'start_time':row['start_time'],
            'eventname':row['eventname'],
            'HomeName':row['HomeName'],
            'AwayName':row['AwayName'],
            # 'HandicapHomehcapdisp':row['HandicapHomehcapdisp'],
            'HandicapHomehcapdisp':row['Handicapawayhcapdisp'],
            'HandicapHomeRate':row['HandicapHomeRate'],
            'Handicapawayhcapdisp':row['Handicapawayhcapdisp'],
            'HandicapawayRate':row['HandicapawayRate'],
            "currentscore":currentscore
            # 'eventname':row['eventname'],
            # 'eventname':row['eventname'],
            # 'eventname':row['eventname']
            
        }

        arroddsdata.append(tmpdata);
    
    arroddsdata = []
    if 0 == cnt:
        return arroddsdata
    for row in resdata:
        currentscore = ""
        if row['currentscore'] is not None:
            currentscore = row['currentscore']
        tmpdata = {
            'start_time':row['start_time'],
            'eventname':row['eventname'],
            'HomeName':row['HomeName'],
            'AwayName':row['AwayName'],
            # 'HandicapHomehcapdisp':row['HandicapHomehcapdisp'],
            'HandicapHomehcapdisp':row['Handicapawayhcapdisp'],
            'HandicapHomeRate':row['HandicapHomeRate'],
            'Handicapawayhcapdisp':row['Handicapawayhcapdisp'],
            'HandicapawayRate':row['HandicapawayRate'],
            "currentscore":currentscore,
            'newstitle':"",
            "newscontent":"",
             "reportTime":""
        }

        arroddsdata.append(tmpdata);

   
    sql = """
        select * from newsinfo where newsTypeName='賽前' and reportTime>=%s and reportTime<= %s
    """
    resdata = sql_helper.fetch_all(sql, (timebegin, timeend))
    
    cnt = 0
    if resdata is not None and resdata != False:
        cnt = len(resdata)

    arrNews = []
    if (cnt > 0):
        for row in resdata:
            Newsinfo = {
                'title': row['title'],
                'content': row['content'],
                'reportTime': row['reportTime']
            }


            # if newtitle in row['title']:
            arrNews.append(Newsinfo)

    arrresdata = []
    if newtitle != "":
        for row in arroddsdata:
            for news in arrNews:
                if newtitle in news['title'] and row['HomeName'] in news['content'] and row['AwayName'] in news['content']:
                    tmpdata = {
                    'start_time':row['start_time'],
                    'eventname':row['eventname'],
                    'HomeName':row['HomeName'],
                    'AwayName':row['AwayName'],
                    'HandicapHomehcapdisp':row['Handicapawayhcapdisp'],
                    'HandicapHomeRate':row['HandicapHomeRate'],
                    'Handicapawayhcapdisp':row['Handicapawayhcapdisp'],
                    'HandicapawayRate':row['HandicapawayRate'],
                    "currentscore":row['currentscore'],
                    'newstitle':news['title'],
                    "newscontent":news['content'],
                    "reportTime":news['reportTime']
                }

                    arrresdata.append(tmpdata);
        return arrresdata
    else:
        for row in arroddsdata:
            for news in arrNews:
                if row['HomeName'] in news['content'] and row['AwayName'] in news['content']:
                    row['newstitle'] = news['title']
                    row['newscontent'] = news['content']
                    row['reportTime'] = news['reportTime']
                    break;

    return arroddsdata