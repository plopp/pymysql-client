#!/usr/bin/python2.7
# -*- coding: cp1252 -*-

from __future__ import print_function
from uuid import getnode as get_mac
from random import randint
import pymysql
from time import sleep
import time
import datetime
import json

file = open('credentials.json','r')
cred = json.load(file)
file.close()

ip = '%(ip)s' % cred
port = cred['port']
user = '%(user)s' % cred
passwd = '%(pass)s' % cred
db = '%(db)s' % cred
table = '%(table)s' % cred

conn = pymysql.connect(host=ip, port=port, user=user, passwd=passwd, db=db)
cur = conn.cursor()

unit = {
    'sampletime' : 1,
    'sensors' : [{
        'sys' : get_mac(),
        'id' : '#a82ka',
        'type' : 'pt100',    
    },
    {
        'sys' : get_mac(),
        'id' : '#a93kd',
        'type' : 'di',    
    },
    {
        'sys' : get_mac(),
        'id' : '#19dm1',
        'type' : 'di',    
    },
    {
        'sys' : get_mac(),
        'id' : '#10ak4',
        'type' : 'di',    
    }]
}

while True:
    for sensor in unit['sensors']:
        value = 0
        if sensor['type'] == 'pt100':
            value = str(randint(18,22))
        if sensor['type'] == 'di':
            value = str(randint(0,1))
        key = str(sensor['sys'])+str(sensor['id'])
        date = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        sqlquery = "INSERT INTO "+db+"."+table+" (id,timestamp,value,name) VALUES (1,'"+date+"',"+value+",'"+key+"')"
        cur.execute(sqlquery)
        conn.commit()
    sleep(1)




cur.close()
conn.commit()
conn.close()
