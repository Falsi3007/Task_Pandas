import pandas as pd
#read csv file
df = pd.read_csv('tr_metrics_dataframe_raw.csv')
# print(df)

#for checking the dynamically output
# df = df[df['status'].isin(['Approved','Canceled'])]
# print(df.to_string())
 
#using pivot 
table = pd.pivot_table(df, index=['dibs_U_id','status'], columns=['Year','Month'],
        aggfunc={'Month': "count"},fill_value=0,dropna=False)
# print(table)

df=(pd.concat([
    sub._append(sub.sum().rename(('Total', '')))
    for k,sub in table.groupby(level=0)])
    # ._append(table.sum().rename(('Grand', 'Total')))
    )
# print(df)

df1=(pd.concat([
    sub._append(sub.sum().rename(('Grand Total',k)))
    for k,sub in table.groupby(level=1)])
    ._append(table.sum().rename(('', '')))
    )
print(df1)

t = pd.concat([df,df1])
# print(t)

t=t.reset_index()
t= t.drop_duplicates()
t=t.set_index(['dibs_U_id','status'])
print(t)
# t.to_excel('tr_report.xlsx')
