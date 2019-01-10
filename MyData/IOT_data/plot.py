import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x_list = [1,2,3,4,5]
y_list = [1,2,3,4,5]

ddata=np.array(pd.read_csv('ddata.csv'))
testdata=np.array(pd.read_csv('testdata.csv'))
traindata=np.array(pd.read_csv('traindata.csv'))
print(ddata)
x=np.arange(500)
y=ddata[1016:1516,1]
y1=traindata[1016:1516,1]
x2=np.arange(510)
y2=testdata[1016:1526,1]

# x=np.arange(1516)
# y=ddata[:1516,1]
# y1=traindata[:1516,1]
# x2=np.arange(1526)
# y2=testdata[:1526,1]

#创建图并命名
plt.figure('all predict image')
ax = plt.gca()

#设置x轴、y轴名称
ax.set_xlabel('x')
ax.set_ylabel('y')

#画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标 #参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
ax.plot(x, y1, color='b', linewidth=1, alpha=0.5)
ax.plot(x2, y2, color='b', linewidth=1, alpha=0.5)
ax.scatter(x, y, c='b', s=26, alpha=0.3)
plt.vlines(500, 0, 8, colors = "b", linestyles = "dashed")

plt.show()


# #创建图并命名
# plt.figure('Line fig')
# ax = plt.gca()
#
# #设置x轴、y轴名称
# ax.set_xlabel('x')
# ax.set_ylabel('y')
#
# #画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标 #参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
# ax.plot(x_list, y_list, color='b', linewidth=1, alpha=0.5)
# ax.scatter(x_list, y_list, c='b', s=26, alpha=0.3)
#
#
# plt.show()