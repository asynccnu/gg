import os
from . import app
from ..spiders import _start_spiders
from ..spiders import _check_ips
from ..db_master import db

ip_all = []  # 爬取的全部IP
ip_use = []  # 检测可用的IP

def check_ip(ip=None):
    ping_result = os.popen(ping_cmd).read()
    return ping_result

@app.task(name='start_spiders')
def start_spiders():
    global ip_all
    _start_spiders(ip_all)
    _check_ips(ip_all, ip_use)
