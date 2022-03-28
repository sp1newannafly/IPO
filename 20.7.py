from urllib.parse import urlunsplit
t = ('http', 'www.admin.ru:80', '/test.php;st', 'var=5', 'metka')
print(urlunsplit(t))