# 示例代码：
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model
import numpy as np

def linear1():
    rnames = ['tid', 'tdate', 'rev']
    rdata = pd.read_csv('../Data/test.csv', header=None, names=rnames)
    # print(rdata)
    # #时间序列类型数据,比如股票代码，日期，日收益
    #  tid   tdate              rev
    #  1     2009-01-01    0.003
    #  1     2009-01-02    0.005
    #  1     2009-01-03    -0.004
    #  2     2009-01-01    0.007
    #  2     2009-01-03    0.004
    #  3     2009-01-02    -0.004
    #  3     2009-01-03    0.001
    # #  ...
    # #1. 数据处理
    # #移除rev为空的值
    cdata = rdata[rdata.rev.notnull()]
    # print(cdata)
    # #tid类型转换成字符型
    cdata['tid'].astype(str)
    # #按照tid分组统计频数
    tid_count = cdata['tid'].value_counts()
    print(tid_count)
    # # #结果：
    # # 3    973
    # # 2    962
    # # 1    893
    # #分层索引，以对tid进行行转列
    indxdata = cdata.pivot('tdate', 'tid')
    print(indxdata[:10])
    # # #结果：
    # #                 rev
    # # tid               1        2        3
    # # 2009-01-06  0.06076  0.02985  0.03000
    # # 2009-01-07 -0.03009 -0.00579 -0.00678
    # # 2009-01-08 -0.03903  0.00583 -0.02382
    # # 2009-01-09  0.02604 -0.00144  0.01420
    # # 2009-01-12  0.00101 -0.01161 -0.00237
    # # 2009-01-13 -0.03955 -0.03524 -0.01946
    # # 2009-01-14  0.07708  0.04870  0.03515
    # # 2009-01-15  0.00980 -0.00580 -0.00449
    # # 2009-01-16  0.03106  0.01021  0.01782
    #
    # #由于1，2，3频数不等，转换后出现缺失值
    # #缺失值插补为均值
    filldata = indxdata.fillna(indxdata.mean())
    print(filldata)
    #               rev
    # tid             1       2       3
    # tdate
    # 2009-01-01  0.003  0.0070 -0.0015
    # 2009-01-02  0.005  0.0055 -0.0040
    # 2009-01-03 -0.004  0.0040  0.0010
    # indxdata.dropna() 删除缺失值
    #
    # #2. 描述统计（频数，均值，标准差，分位数）
    print(filldata.describe())
    # # #结果：
    # # rev                1           2           3
    # # count  973.000000  973.000000  973.000000
    # # mean     0.000843    0.000754    0.000329
    # # std      0.021283    0.021971    0.014343
    # # min     -0.089100   -0.099450   -0.067440
    # # 25%     -0.010480   -0.011000   -0.007110
    # # 50%      0.000843    0.000000    0.000730
    # # 75%      0.009670    0.011000    0.008500
    # # max      0.100080    0.100000    0.061150
    #
    # #相关性分析， 不同股票收益之间关系
    print(filldata.corr())
    # # #结果：
    # #              1         2         3
    # #     1    1.000000  0.562656  0.699232
    # #     2    0.562656  1.000000  0.692138
    # #     3    0.699232  0.692138  1.000000
    # #1，3相关性较高
    # #3. 绘制图形
    # filldata.plot()
    # plt.show()
    ts = filldata.cumsum()  # 收益累计和
    ts.plot()
    plt.show()
    #
    # #4. 简单线性回归
    # #分组建模,测试数据
    sampleR = 0.8
    x = filldata.ix[:, 1:2]
    y = filldata.ix[:, 0]
    print('x',x)
    print('y',y)
    nsample = len(y)
    sampleBoundary = int(nsample * sampleR)
    print('sampleBoundary', sampleBoundary)
    shffleIdx = np.arange(nsample)
    print('shffleIdx', shffleIdx)
    np.random.shuffle(shffleIdx)
    print('shffleIdx2', shffleIdx)
    train_x = x.ix[shffleIdx[:sampleBoundary]]
    print('train_x', train_x)
    train_y = y[shffleIdx[:sampleBoundary]]
    print('train_y', train_y)
    test_x = x.ix[shffleIdx[sampleBoundary:]]
    print('test_x', test_x)
    test_y = y[shffleIdx[sampleBoundary:]]
    print('test_y', test_y)
    #线性回归模型
    LR = sklearn.linear_model.LinearRegression()
    LR.fit(train_x,train_y)
    predict_y = LR.predict(test_x)
    print('predict_y', predict_y)
    # #结果评估误差率，R方，回归系数，绘制图形
    # ysample = range(len(test_y))
    # error = np.linalg.norm(predict_y-test_y,ord=1)/len(test_y)
    # print ("Error: %.2f" %(error))
    # print('Coefficients: \n', LR.coef_)
    # print("Residual sum of squares: %.2f"
    #       % np.mean((predict_y - test_y) ** 2))
    # print('Variance score: %.2f' % LR.score(test_x, test_y))
    # plt.plot(ysample,predict_y,'r--',label="Predict")
    # plt.plot(ysample,test_y,'g:',label="True")
    # plt.show()
    # #模型预测
    # LR = sklearn.linear_model.LinearRegression()
    # LR.fit(x,y)
    # pre_y = LR.predict(x)
    # #保存预测结果
    # res = pd.DataFrame(pre_y)
    # res.to_csv('../Data/result.csv',header=None,index=False)


def linear2():
    rnames = ['tid','1', '2','3']
    filldata = pd.read_csv('../Data/test1.csv', header=None, names=rnames)
    print(filldata)
    print(filldata.describe())
    # ts = filldata.cumsum()  # 收益累计和
    # ts.plot()
    # plt.show()
    sampleR = 0.8
    x = filldata.ix[:, 2]
    y = filldata.ix[:, 0:2]
    print('x',x)
    print('y',y)
    nsample = len(y)
    sampleBoundary = int(nsample * sampleR)
    print('sampleBoundary', sampleBoundary)
    shffleIdx = range(nsample)


linear1()