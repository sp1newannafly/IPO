from urllib.parse import parse_qsl
s = "str=%D1%F2%F0%EE%EA%E0&v=10&v=20&t="
parse_qsl(s, encoding="cp1251")
print (parse_qsl(s))