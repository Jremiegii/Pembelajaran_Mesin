import pandas as pd 

data = {'nama':['kenny','cahyo','egi','daniel'],
        'nim': [215314038,215314027,215314117,205314062],
        'umur':[20,25,22,21],
        'prodi': ['informatika','farmasi','Matematika','elektro']}

df = pd.DataFrame(data)
df_urut = df.sort_values(by='nim')
print(df_urut)

writer = pd.ExcelWriter('dataaa.xlsx')
df_urut.to_excel(writer, index=False, sheet_name='Sheet1')

writer._save()