import  matplotlib.pyplot as plt
import numpy as np
import xlrd
import pprint

def moving_average(y, n=3):
    ret = [np.array([y1 for y1 in y[max(ind-n//2, 0):min(ind+n-n//2, len(y))]]).mean() for ind in range(len(y))]
    # print(ret)
    return ret

workbook = xlrd.open_workbook('mgn.xlsx')
worksheet = workbook.sheet_by_index(3)
print(list([x for x in worksheet.col_values(0)][124:157]))
x = np.array([float(x) for x in list([x for x in worksheet.col_values(0)][124:157])])
y = np.array([float(y) for y in list([y for y in worksheet.col_values(1)][124:157])])
y1 = moving_average(y,10)
# x, y = zip(*sorted((xVal, np.mean([yVal for a, yVal in zip(x, y) if xVal==a])) for xVal in set(x)))
plt.plot(x,y,'b-')
plt.plot(x,y1,'r-')
plt.plot([0,90],[0,0],'k-')
plt.show()

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('mgn1.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

print(y1)

# Iterate over the data and write it out row by row.
for xp, y in zip(x,y1):
    worksheet.write(row, col,     xp)
    worksheet.write(row, col + 1, y)
    row += 1

workbook.close()
print(list(zip(x,y1)))