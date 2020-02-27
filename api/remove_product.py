#!/usr/bin/python3

from python.webpage_functions import get_form_data, has_form_data
from python.addRemoveProduct import removeProduct
from json import dumps

output = dict(success=False, message='Error removing product')

if has_form_data():
    pid = get_form_data('pid')
    if pid is None:
        output['message'] = 'Error specifying pid'
    else:
        result = removeProduct(pid)
        if result == "Product successfully removed.":
            output['success'] = True
        output['message'] = result
else:
    output['message'] = 'No product specified to remove'

print('Content-Type: text/json')
print()
print(dumps(output))

