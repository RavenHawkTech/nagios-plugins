#!/usr/bin/env python3
import os, time, sys, socket, datetime, re, psutil
from datetime import timedelta
#---------------------------------------------#
def convert_bytes(size):
		for x in ['KB', 'MB', 'GB', 'TB']:
			if size < 1024.0:
				return "%3.1f %s" % (size, x)
			size /= 1024.0
		return size
#---------------------------------------------#
now = datetime.datetime.now()
Last_checked = now.strftime("%m/%d/%Y %I:%M %p")
#---------------------------------------------#
# Collect Storage Values
obj_Disk = psutil.disk_usage('/')
sys_storage_total = convert_bytes(obj_Disk.total / (1024) )
sys_storage_used = convert_bytes(obj_Disk.used / (1024) )
sys_storage_free = convert_bytes(obj_Disk.free / (1024) )
#------------------------------------------------------------#             
if obj_Disk.used < obj_Disk.total:
        print("OK - %s disk space used" % sys_storage_used)
        sys.exit(0)
if obj_Disk.used > obj_Disk.free:
        print("WARNING - %s disk space used" % sys_storage_used)
        sys.exit(1)
elif sys_storage_used == sys_storage_total:
        print("CRITICAL - %s disk space used" % sys_storage_used)
        sys.exit(2)
else:
        print("UNKNOWN - unable to check storage" % sys_storage_used)
        sys.exit(3)
