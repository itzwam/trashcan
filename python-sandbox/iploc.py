import requests
import sys
import json
import ipaddress

############################
# showinfos(ip)
#
def showinfos(ip):
  response = requests.get("http://ip-api.com/json/{}?fields=130623".format(ip))
  infos = response.json()
  version = ipaddress.ip_address(u"{}".format(ip)).version
  print(u"ip : {} (ipv{})".format(infos['query'],version))
  print(u"country : {} ({})".format(infos['country'],infos['countryCode']))
  print(u"region : {} ({})".format(infos['regionName'],infos['region']))
  print(u"city : {} ({})".format(infos['city'],infos['zip']))
  print(u"isp : {} ({})".format(infos['isp'],infos['org']))
  print(u"isMobile : {}".format(infos['mobile']))
  print(u"reverse dns : {}".format(infos['reverse']))
  print(u"AS : {} ({})".format(" ".join(infos['as'].split()[1:]),infos['as'].split()[0]))

############################
# blah blah
#

if len(sys.argv) == 1:
  ip = requests.get("http://api.ipify.org").text
  showinfos(ip)
else:
  for ip in sys.argv[1:]:
    showinfos(ip)

