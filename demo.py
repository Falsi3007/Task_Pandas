import pandas as pd
#read csv file
df = pd.read_csv('10_metrics_braintree_intrument.csv')
# print(df)

#using pivot 
table = pd.pivot_table(df, index=['Payment Instrument Type','Card Type','Response'], columns=['Year','Month'], values=['Month'],
        aggfunc={'Response': "count"},dropna=False,fill_value=0)
# print(table)

df=(pd.concat([
    sub._append(sub.sum().rename(('','','Total')))
    for k,sub in table.groupby(level=[0,1])])
    # ._append(table.sum().rename(('Grand', 'Total')))
    )
# print(df)

df1=(pd.concat([
    sub._append(sub.sum().rename(('Total','','')))
    for k,sub in table.groupby(level=0)])
    ._append(table.sum().rename(('Grand', 'Total','')))
    )
# print(df1)

# df1=(pd.concat([
#     sub._append(sub.sum().rename(('Grand Total',k)))
#     for k,sub in table.groupby(level=1)])
#     ._append(table.sum().rename(('', '')))
#     )
# print(df1)

t = pd.concat([df,df1])
# print(t)

t=t.reset_index()
t= t.drop_duplicates()
t=t.set_index(['Payment Instrument Type','Card Type'])
# print(t)
t=t.to_string()
print(t)
