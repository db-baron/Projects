#See
# https://pypi.python.org/pypi/pyexcel-ods/0.2.1

# This 'from' statement works in Python3 (but not 2) interactive mode when you're inside the dir pyexcel-ods
from pyexcel_ods3 import get_data

get_data.path.append("pyexcel_ods3/pyexcel-ods")

#data = get_data("Start_Stop_Continue.ods")
columnB_data = get_data("Start_Stop_Continue.ods", start_column=2, column_limit=1)

import json

print(json.dumps(columnB_data))

