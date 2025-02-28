import pandas as pd

#read csv
df = pd.read_csv('10_metrics_braintree_intrument.csv')
# print(df)

#pivot table
table = pd.pivot_table(df, index=['Payment Instrument Type','Card Type','Response'], columns=['Year','Month'], values=['Month'],
        aggfunc={'Response': "count"},dropna=False,fill_value=0)
# print(table)

df = df.loc(['Payment Instrument Type'].loc['Card Type'].loc['Response']==0)
df1 = table.drop(df,level=2,axis=0)
print(df)

# subtotal1=table.groupby(level=2).sum()     #last sum
# print(subtotal1)

# subtotal2=table.groupby(level=[0,1]).sum()      #rows total 
# print(subtotal2)

# subtotal3=table.groupby(level=0).sum()        #total of payment type vise
# print(subtotal3)

# subtotal4 = table.groupby(level=[0,2]).sum()      #rows payment type vise
# print(subtotal4)

# subtotal5 = table.groupby(level=[[2]]).sum()      #grand total 
# print(subtotal5)

# pivot2=pd.concat([subtotal1,subtotal2,subtotal3,subtotal4,subtotal5])
# print(pivot2)

# pd.set_option('display.max.rows',89)
# print(pivot2)

# pivot2.to_excel('result.xlsx')
