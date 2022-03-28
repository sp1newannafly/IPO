from urllib.parse import quote_from_bytes
p=(bytes("Строка 2", encoding="cp1251"))
print(quote_from_bytes(p))