from urllib.parse import urlsplit
url = urlsplit("http://www.admin.ru:80/test.php;st?var=5#metka")
print(url)