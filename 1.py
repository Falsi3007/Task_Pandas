import pandas as pd

#read csv file
df = pd.read_csv('qa.csv')
# print(df)

#display all rows
# pd.set_option('display.max.rows',181)
# print(df)

#using pivot 
table = pd.pivot_table(df, index=['hold_reason','confirmed_fraud'], columns=['canceled_year','canceled_month'], values=['latest_buyer_price'],
        aggfunc={'confirmed_fraud': "count", 'latest_buyer_price': "sum"},fill_value=0,dropna=False)
# print(table)

#rename column name 
table = table.rename(columns={'confirmed_fraud':'fraud_count'})
print(table)
