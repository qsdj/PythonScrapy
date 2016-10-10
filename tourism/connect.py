# -*- coding: utf-8 -*-
import MySQLdb


def InsertScenic(list):
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        cur.execute(
            " insert into YouPu_Scenic(CityId,ScenicName,Describes,CityCnName,EnName,TagName,Lng,Lat,PicPath,JsonData) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
            (list['CityId'], list['ScenicName'], list['Describes'], list['CityCnName'], list['EnName'],
             list['TagName'], list['Lng'], list['Lat'], list['PicPath'], list['JsonData']))

    except MySQLdb.Error, e:
        print e
    cur.close()
    conn.commit()
    conn.close()


def InsertCountry(lists):
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        cur.execute(
            " insert into YouPu_Country(CountryId,CountryName,Pic,JsonData) VALUES (%s, %s, %s, %s) ",
            (lists["id"], lists["cnName"], lists["pic"], lists["jsonData"]))

    except MySQLdb.Error, e:
        print e
    cur.close()
    conn.commit()
    conn.close()


def QueryCountryId():
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        lists = cur.execute(" select CountryId from YouPu_Country ")
        infos = cur.fetchmany(lists)

    except MySQLdb.Error, e:
        print e
    cur.close()
    conn.commit()
    conn.close()
    return infos


def InsertCity(lists):
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        cur.execute(
            " insert into YouPu_City(CityId,CountryId,CityName,EnName,Lat,Lng,Pic,Describes,JsonData) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s) ",
            (lists["CityId"], lists["CountryId"], lists["CityName"], lists["EnName"], lists["Lat"], lists["Lng"],
             lists["Pic"], lists["Describes"], lists["JsonData"]))

    except MySQLdb.Error, e:
        print e
    cur.close()
    conn.commit()
    conn.close()


def QueryCityId():
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        lists = cur.execute(" select CityId from YouPu_City ")
        infos = cur.fetchmany(lists)

    except MySQLdb.Error, e:
        print e
    cur.close()
    conn.commit()
    conn.close()
    return infos


def InsertTheme(lists):
    conn = MySQLdb.connect(
        host="172.16.5.15",
        port=3306,
        user="zhang",
        passwd="zhang",
        db="TravelDataCapture",
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        cous = cur.execute(" select Id from YouPu_Theme WHERE TagId =" + lists["ThemeId"])
        print cous
        if cous < 1:
            cur.execute(
                " insert into YouPu_Theme(TagId,TagName,Pic,Uspic,JsonData) VALUES (%s, %s, %s, %s, %s) ",
                (lists["ThemeId"], lists["TagName"], lists["Pic"], lists["Uspic"], lists["JsonData"]))

    except MySQLdb.Error, e:
        print e

    cur.close()
    conn.commit()
    conn.close()
