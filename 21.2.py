from http.client import HTTPConnection
headers = { "User-Agent": "MySpider/1.0",
"Accept": "text/html, text/plain, application/xml",
"Accept-Language": "ru, ru-RU",
"Accept-Charset": "windows-1251",
"Referer": "/index.php" }
con = HTTPConnection("mail.ru")
con.request("HEAD", "/testrobots.php?%s")
result = con.getresponse()
print (result.msg)
result.read()
con.close()
