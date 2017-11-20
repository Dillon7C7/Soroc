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


# {serial: {asset: (model, comment)}}
HDD = {}

print('Opening excel...')
workBook = openpyxl.load_workbook('HDDs.xlsx')
sheets = workBook.get_sheet_names()
HDDsheet = workBook.get_sheet_by_name(sheets[0])

for row in range(int(sysArgs['startRow']), int(sysArgs['endRow']) + 1): # iterate through first row to last

    serial = str(HDDsheet[sysArgs['serialCol'].upper() + str(row)].value).upper()
    asset = str(HDDsheet[sysArgs['assetCol'].upper() + str(row)].value).upper()
    model = str(HDDsheet[sysArgs['modelCol'].upper() + str(row)].value).upper()
    comment = str(HDDsheet[sysArgs['commentCol'].upper() + str(row)].value).upper()

    if serial == 'NONE': # skip the row if there are no values
        continue

    # HDD is a dictionary whose key is a serial and value is a tuple,
    # containing the asset tag, model, comment, + anything in the future
    HDD[serial] = (asset, model, comment)


    # HDD is a dictionary whose key is a serial and value is a dictionary
    # the inner dictionary's key is an asset tag and value is a
    # tuple of models and comments (perhaps sell/scrap as well in the future)
    #HDD[serial] = {asset: (model, comment)}


## -------------------------------------------------------------------------

##r = ['serial', 'asset', 'model', 'comment']

##def practice(l, val):
##    print(l + ' is: ' + val) 
for k, v in HDD.items():
    print('serial is: ' + k)
    print('asset is: ' + v[0])
    print('model is: ' + v[1])
    print('comment is: ' + v[2])
    print()
##    for i in range(len(r)):
##        if i == 0:
##            practice(r[i], k)
##        else:
##            practice(r[i], v[i-1])
##    print()
##    
