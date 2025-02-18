import pandas as pd
import numpy as np

#read csv file
df = pd.read_csv('braintree_.csv')
# print(df)

c = ['US','IntI']
df["country"] = np.random.choice(c, size=len(df))
# print (df)

#using pivot 
table = pd.DataFrame(pd.pivot_table(df, index=['country','Response'], columns=['Year','Month'],
        aggfunc={'Month': "sum"})[('Month', 2023, 1)])
# print(table)

def func(k,sub):
    # ans = round(sub.loc[k].loc['Declined'].sum() *100 / sub.sum(),2)
    ans = round(sub.xs((k,'Declined'),level=[0,1],drop_level=False).sum() *100/sub.sum(),2)
    # print(sub.loc[k].loc['Declined'].sum()/sub.sum())
    return ans.astype(str)+'%'
    
df=(pd.concat([
    sub._append([sub.sum().rename(('', 'Total')),func(k,sub).rename(('','Declined Ratio'))])
    for k,sub in table.groupby(level=0)])
    # ._append(table.sum().rename(('Grand', 'Total')))
    )
# print(df)

def func1(sub):
    ans = round(sub.xs('Declined',level=1).sum()*100/sub.sum(),2)
    return ans.astype(str)+'%'

df1=(pd.concat([
    sub._append(sub.sum().rename(('Grand Total',k)))
    for k,sub in table.groupby(level=1)])
    ._append(table.sum().rename(('', 'Grand Total')))._append((func1(table)).rename(('','Declined Ratio')))
)
# print(df1)

t = pd.concat([df,df1])
# print(t.index.names)

t.index.names=['country','Response']
t=t.reset_index()
t= t.drop_duplicates()
t=t.set_index(['country','Response'])
print(t)


