from ipware.ip import get_ip
import inspect
from ..models import Analytics
import datetime


def get_info(request):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    ip = get_ip(request)
    newrow = Analytics(request_ip=ip, func=calframe[1][3], date=datetime.datetime.now())
    newrow.save()
    if ip is not None:
        print("%s called %s"%(ip,calframe[1][3]))

    else:
        print("we don't have an IP address for user")