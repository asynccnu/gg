from spiders import _start_spiders
from spiders import _check_ips

ip_all = []
ip_use = []

if __name__ == '__main__':
    _start_spiders(ip_all)
    print(len(ip_all))
    _check_ips(ip_all, ip_use)
    print(len(ip_use))
