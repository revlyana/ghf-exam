x = b"hello"
a = str(x, encoding='ascii') == str(x, encoding='utf-8')
b = str(x) == str(x, encoding='utf-8')
print(a, b)
