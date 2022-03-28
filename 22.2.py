from urllib.request import urlopen
res = urlopen("http://mail.ru/testrobots.php")
print (res.readline(100).decode("cp1251") )