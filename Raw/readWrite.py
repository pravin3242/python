import pandas as pd
import os
import time


path = 'C:\\Users\\lnv0176\\Downloads\\Playwright-Python_Framework.xlsx'

sheet = 'Test Case'

read = pd.read_excel(path, sheet_name=sheet)

print(read)

o = open('D:\\raw.txt','w')

o.write(read.to_string())

o.close()

app = open('D:\\raw.txt','a')

app.write(read.to_string())

app.close()






