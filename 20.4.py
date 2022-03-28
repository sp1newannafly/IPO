from urllib.parse import urlparse
u = urlparse("http://site.ru/add.php?v=5#metka")
print(u.query)
print(u.fragment)
