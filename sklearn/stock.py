import pandas as pd
import numpy as np
import datetime
import pandas_datareader as web
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing, svm, model_selection
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 11, 20)
df = web.DataReader("XOM", "yahoo", start, end)
print(df.head())
print(df.tail())
print(df.index)

df = df[['Open',  'High',  'Low',  'Close', 'Volume']]
df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
df = df[['Close', 'HL_PCT', 'PCT_change', 'Volume']]
print(df.head())
print(len(df))

forecast_col = 'Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df))) # 5days
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)

print(df.shape)
print(df.tail())
X = np.array(df.drop(['label'], 1)) #axis 默认为0，指删除行，因此删除columns时要指定axis=1；
X = preprocessing.scale(X) # 对X的数据进行规范化处理，让X的数据服从正态分布

X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
print(X)
print(X.shape)
print(X_lately)
print(X_lately.shape)

print(df)
y = np.array(df['label'])
print(y)
print(y.shape)
X_train, X_test, y_train ,y_test = model_selection.train_test_split(X,y,test_size=0.2)

clf = LinearRegression()
clf.fit(X_train,y_train)# TODO
accuracy = clf.score(X_test,y_test)
print(accuracy)

forecast_set = clf.predict(X_lately)
print(forecast_set,accuracy,forecast_out)

style.use('ggplot')
df['Forecast']=np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
print(last_date,last_unix)
one_day = 86400
next_unix = last_unix + one_day + one_day * 2 # weekend

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
print(df.tail())

df['Close'].plot()
df['Forecast'].plot()
plt.xlabel("Date");
plt.ylabel("Price");
plt.show()
