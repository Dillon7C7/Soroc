#! python3

## Non-modular messy version 1

import openpyxl, sys
from openpyxl.utils import get_column_letter, column_index_from_string


if len(sys.argv) != 7:
    
    print('reuse.py USAGE: [serial # column] [asset # column] [model column] ' +
          '[comments column] [starting row] [ending row] -- Extract information ' +
          'from excel')

    sys.exit()

# these values store a command line argument
sysArgNames = ['fileName', 'serialCol', 'assetCol', 'modelCol', 'commentCol',
               'startRow', 'endRow']
sysArgs = {}

# error if we use sysArgNames instead of system args
for a in range(1, len(sys.argv)):
    sysArgs[sysArgNames[a]] = sys.argv[a]


# {serial: (asset, model, comment)}
HDD = {}

print('Opening excel...')
try:
    workBook = openpyxl.load_workbook('HDDs.xlsx')
except FileNotFoundError:
    print('daaayyyym')
    sys.exit()
sheets = workBook.get_sheet_names()
HDDsheet = workBook.get_sheet_by_name(sheets[0])


def excelData(excelSheet, element):
    return str(excelSheet[sysArgs[element].upper + str(row)].value).upper()

for row in range(int(sysArgs['startRow']), int(sysArgs['endRow']) + 1): # iterate through first row to last

    serial = excelData(HDDsheet, 'serialCol')
    asset = excelData(HDDsheet, 'assetCol')
    model = excelData(HDDsheet, 'modelCol')
    comment = excelData(HDDsheet, 'commentCol')

    if serial == 'NONE': # skip the row if there are no values
        continue

    # HDD is a dictionary whose key is a serial and value is a tuple,
    # containing the asset tag, model, comment, + anything in the future
    HDD[serial] = (asset, model, comment)


## -------------------------------------------------------------------------
## remove later...
for k, v in HDD.items():
    print('serial is: ' + k)
    print('asset is: ' + v[0])
    print('model is: ' + v[1])
    print('comment is: ' + v[2])
    print()
