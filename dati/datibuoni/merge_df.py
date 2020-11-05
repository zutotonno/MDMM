import pandas as pd

df1 = pd.read_csv('dati1New/GLPK_exec.csv')
df1=df1.add_suffix('_GLPK')
df1.rename({'instance_GLPK':'instance'},axis=1, inplace=True)
df1.set_index('instance', inplace=True)

df2 = pd.read_csv('dati1NewCbc/CBC_exec.csv')
df2=df2.add_suffix('_CBC')
df2.rename({'instance_CBC':'instance'},axis=1, inplace=True)
df2.set_index('instance', inplace=True)

df = df1.join(df2, how='outer')

print(df)

df.to_csv('All_solvers.csv',index=True)