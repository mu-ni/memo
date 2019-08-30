from sklearn.datasets import load_iris, load_boston
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

obj = KNeighborsClassifier()
iris = load_iris()
x = iris.data
y = iris.target

obj.fit(x, y)
y_pred = obj.predict(x)
print(y - y_pred)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print(y_pred - y_test)

loaded_data = load_boston()
data_x = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_x, data_y)
y_pred = model.predict(data_x)
print(model.coef_)
print(model.intercept_)
print(model.get_params())
print(model.score(data_x, data_y))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')
plt.show()

import numpy as np
import pandas as pd

d = {'one' : np.random.rand(10),
     'two' : np.random.rand(10)}

df = pd.DataFrame(d)

df.plot(style=['o','rx'])
plt.show()
