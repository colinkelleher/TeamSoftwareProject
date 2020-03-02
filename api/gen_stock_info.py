#!/usr/bin/python3

from python.pdf_generator import generateStockInfo
from json import dumps

location = generateStockInfo()

print('Content-Type: text/json')
print()
print(dumps(dict(success=True, path=location)))
