import pandas as pd

dict = {'1-1': ('1','2',None), '1-2': ('1', None,'3')}

a = pd.DataFrame(dict)


writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
a.to_excel(writer, sheet_name='Sheet1')
writer.save()