from urllib.parse import urlunparse
t = ('http', 'www.admin.ru:80', '/test.php', '', 'var=5', 'metka')
print(urlunparse(t))