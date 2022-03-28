from urllib.request import urlopen
res = urlopen("http://mail.ru/testrobots.php")
print (res.read(34).decode("cp1251") )
