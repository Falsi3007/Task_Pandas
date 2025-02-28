import pandas as pd

#read csv file
df = pd.read_csv('tr_metrics_dataframe_raw.csv')
df = df[df['status'].isin(['Approved','Canceled'])]
# print(df.to_string())
# df.drop(columns=['id'],inplace=True)
# print(df.columns)
# print(df)

table = pd.pivot_table(df, index=['dibs_U_id','status'], columns=['Year','Month'],values=['id'],
        aggfunc="count",fill_value=0,dropna=False)
# print(table)

df=(pd.concat([
    sub._append(sub.sum().rename(('Total', '')))
    for k,sub in table.groupby(level=0)]))
# print(df)

df1=(pd.concat([
    df._append(grand.sum().rename(('Grand Total',k)))
    for k,grand in df.groupby(level=1)]))
# print(df1)

t = df1.loc['Grand Total'].rename({'':'z'}).sort_values('status').rename({'z':''})
t['dibs_U_id']=['Grand Total']*4
t1 = t.reset_index()
t2 = t1.set_index(['dibs_U_id','status'])
t3 = pd.concat([df1,t2])
# print(t3)

df2 = t3.reset_index()
df3 = df2.drop_duplicates(keep='last')
# print(df3)
df4 = df3.set_index(['dibs_U_id','status'])
print(df4)
