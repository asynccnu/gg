import os
from . import app
from ..spiders import _start_spiders
from ..db_master import db

ip_all = []  # 爬取的全部IP

def ping_ip(ip=None):
    ping_cmd = 'ping -c 2 %s' % ip
    ping_result = os.popen(ping_cmd).read()
    return ping_result

@app.task(name='start_spiders')
def start_spiders():
    global ip_all
    _start_spiders(ip_all)
    for ip in ip_all:
        ping_result = ping_ip(ip.get('ip').split(':')[0])
        if ping_result.find('100% packet loss') < 0:
            db.sadd('ips', ip)
    db.save()
