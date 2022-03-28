from http.client import HTTPConnection
from urllib.parse import urlencode
data = urlencode({"color": "Красный", "var": 15}, encoding="cp1251")
headers = { "User-Agent": "MySpider/1.0",
"Accept": "text/html, text/plain, application/xml",
"Accept-Language": "ru, ru-RU",
"Accept-Charset": "windows-1251",
"Referer": "/index.php" }
con = HTTPConnection("mail.ru")
con.request("GET", "/testrobots.php?%s" % data, headers=headers)
result = con.getresponse()
print (result.read().decode("cp1251" ))
con.close() 