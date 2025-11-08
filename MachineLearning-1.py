import numpy as np
from numpy.random import randn

import pandas as pd
from pandas import Series, DataFrame
#import matplotlib as plt
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import rcParams


#address = 'D:\\Coursera\\MachineLearning-Linkdin\\mtcars.csv'
#cars = pd.read_csv(address)
#print(cars.head())

#cars.columns = ['car_name','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

#plt.show()

#cars.mpg.plot(kind='bar')
#plt.show()

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(x,y)
plt.show()


