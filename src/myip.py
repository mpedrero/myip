import urllib
import time
import re

while True:
	web = open("url.html","w")
	f = urllib.urlopen("http://checkip.dyndns.org")
	webstring = f.read()
	ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', webstring )
	print ip[0]," -> ", time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
	web.write(ip[0])
	web.write(" -> ")
	web.write(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
	web.close()
	time.sleep(3600);