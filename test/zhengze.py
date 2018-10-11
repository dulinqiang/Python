import re

code='hasdfgxxIxxsfffh234xxlovexxsdsfs44xxyouxxsggus7'
b=re.findall('xx.*xx',code)
c=re.findall('\Bsd',code)
print(c)
