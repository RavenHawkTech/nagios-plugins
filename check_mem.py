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
def percentage(percent, whole):
  return (percent * whole) / 100.0
#---------------------------------------------#
now = datetime.datetime.now()
Last_checked = now.strftime("%m/%d/%Y %I:%M %p")
#---------------------------------------------#
lines = os.popen('grep MemTotal /proc/meminfo').readlines()
sys_MemTotal = lines[0].split(':')[1].lstrip()
sys_MemTotal = convert_bytes(int(sys_MemTotal[:-3]))
#---------------------------------------------#
lines = os.popen('grep MemFree /proc/meminfo').readlines()
#---------------------------------------------#
sys_MemFree = lines[0].split(':')[1].lstrip()
sys_MemFree = convert_bytes(int(sys_MemFree[:-3]))
#---------------------------------------------#
mem_total = int(float(sys_MemTotal[:-3]))
mem_free  = int(float(sys_MemFree[:-3]))
#---------------------------------------------#
mem_50_percent = percentage(50,mem_total)
mem_80_percent = percentage(80,mem_total)
#---------------------------------------------#
if mem_free < mem_total:
        print("OK - %s memory used" % sys_MemFree)
        sys.exit(0)
elif mem_free == mem_50_percent:
        print("WARNING - %s memory used" % sys_MemFree)
        sys.exit(1)
elif sys_MemFree == mem_80_percent:
        print("CRITICAL - %s memory used" % sys_MemFree)
        sys.exit(2)
else:
        print("UNKNOWN -  error obtaining usage" % sys_MemFree)
        sys.exit(3)
