# encoding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler
from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import time
import cgi
import uuid
import json

Base = declarative_base()


class MacBase(Base):
    __tablename__ = 'macBase'

    id = Column(Integer, primary_key=True)
    sid = Column(String(40))
    mmac = Column(String(200))
    rate = Column(String(200))
    wssid = Column(String(200))
    wmac = Column(String(200))
    time = Column(String(200))
    lat = Column(String(200))
    lon = Column(String(200))
    addr = Column(String(200))
    createtime = Column(String(200))

    macdata = relationship('MacData')


class MacData(Base):
    __tablename__ = 'macData'

    id = Column(Integer, primary_key=True)
    mac = Column(String(200))
    rssi = Column(String(200))
    ts = Column(String(200))
    tmc = Column(String(200))
    tc = Column(String(200))
    dsi = Column(String(200))
    createtime = Column(String(200))

    macbase_id = Column(String(20), ForeignKey('MacBase.id'))


engine = create_engine('mysql://zhang:zhang@172.16.5.15:3306/probeDb')
DBSession = sessionmaker(bind=engine)


class TodoHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['content-length'])
        post_values = self.rfile.read(length)

        print post_values

        jsondata = json.loads(post_values[5:])  # [5:]

        session = DBSession()

        list = []
        for singeldata in jsondata["data"]:
            new_macData = MacData(
                mac=singeldata["mac"],
                rssi=singeldata["rssi"],
                ts=self.json_has(singeldata, "ts"),
                tmc=self.json_has(singeldata, "tmc"),
                tc=self.json_has(singeldata, "tc"),
                dsi=self.json_has(singeldata, "ds"),
                createtime=time.time()
            )
            list.append(new_macData)

        new_macbase = MacBase(
            sid=jsondata["id"],
            mmac=jsondata["mmac"],
            rate=jsondata["rate"],
            wssid=jsondata["wssid"],
            wmac=jsondata["wmac"],
            time=jsondata["time"],
            lat=jsondata["lat"],
            lon=jsondata["lon"],
            addr=jsondata["addr"],
            createtime=time.time(),
            macdata=list
        )

        session.add(new_macbase)

        session.commit()

        session.close()

        print "记录完成:", time.time()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(post_values)

    def json_has(self, json, key):
        if (json.has_key(key)):
            return json[key]
        return ""


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('192.168.0.101', 8080), TodoHandler)
    print("服务器已启动...")
    server.serve_forever()
