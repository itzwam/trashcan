import requests
import sys

print("[#] Python HaveIBeenPwned interface")

email = ""
if len(sys.argv) == 2:
  email = sys.argv[1]
else:
  email = raw_input('[?] Email : ')

print("[#] checking all reports for {}".format(email))

data = requests.get("https://haveibeenpwned.com/api/pasteaccount/{}".format(email))

count = 0
if data.status_code == 404 :
  print("[#] Huray your email is not in any paste \\o/")

elif data.status_code == 400:
  print("[#] Hmmm, the email is not in an understandable format, sorry")

elif data.status_code == 403:
  print("[#] It was not intended, please retry")

elif data.status_code == 429:
  print("[#] Stop spamming please :). Take your time and retry in 5 minutes")

elif data.status_code == 200:
  for report in data.json():
    count += 1 
    print("[#] ---------------------------------")
    print(u"[#] ID : {}".format(report['Id']))
    print(u"[#] Website : {}".format(report['Source']))
    print(u"[#] Paste name : {}".format(report['Title']))
    print(u"[#] Paste date : {}".format(report['Date']))
  print("[#] ---------------------------------")
  print("[#] Your email appeared in {} websites".format(count))
