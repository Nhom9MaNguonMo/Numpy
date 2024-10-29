import pandas as pd
from numpy import array
from matplotlib import pyplot as plt
import numpy as np

# df=pd.read_csv('matplolib\diemPython.csv',index_col=0,header=0)
# in_data= array(df.iloc[:,:])

# print('Tong so sinh vien di thi la : ')
# tongsv=in_data[:,1]
# print(tongsv)
# print(np.sum(tongsv))

# diemA=in_data[:,3]
# diemBc=in_data[:,4]
# listClass=in_data[:,0]
# maxA=diemA.max()
# i, =np.where(diemA==maxA)

# print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxA))

# plt.plot(listClass, diemA, 'r-', label="Diem A")
# plt.plot(listClass,diemBc,'g-',label="Diem B +")

# plt.xlabel('Lớp')
# plt.ylabel('So sv dat diem ')
# plt.legend(loc='upper right')

# plt.show()


# pie chart
# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]
# mycolors = ["black","hotpink","b","#4CAF50"]
# plt.pie(y,labels = mylabels, colors = mycolors)
# plt.legend()
# plt.show()

x= np.array([10,20,30,40])
y = np.array([35,25,25,15])
plt.barh(x,y)
plt.show()
