__author__ = 'yanjiajia'
#coding = utf-8
#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from gaga.models import Fileserver

def ssh(request):
#    DISK_STATUS = sshapi(ser_config.DISK_STATUS)
#    RAID_STATUS = sshapi(ser_config.RAID_STATUS)
#    SMB_STATUS = sshapi(ser_config.SMB_STATUS)
#    DICT = {'username': username, 'list1': DISK_STATUS, 'list2': RAID_STATUS, 'list3': SMB_STATUS}
    username = request.COOKIES.get('username', '')
    obj = Fileserver.objects.all().order_by('-id')[0]
    return render_to_response('newtem/samba.html', {'username': username, 'obj': obj})
