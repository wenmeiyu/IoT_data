# -*- coding:utf-8 -*-
"""
make LSTM model analyze data to predict
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os

# ——————————————————导入数据——————————————————————
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                    date_parser=dateparse)
ts = np.array(adata['temperature'])  # 获取温度序列

# 以折线图展示ts
# plt.figure()
# plt.plot(ts)
# plt.show()

normalize_data = (ts - np.mean(ts)) / np.std(ts)  # 标准化
normalize_data = normalize_data[:, np.newaxis]  # 增加维度shape(2264,1)

# # create data  一个简单的线性拟合的例子
# x_data = np.random.rand(100).astype(np.float32)
# y_data = x_data * 0.1 + 0.3
# # 搭建模型
# Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 定义变量
# biases = tf.Variable(tf.zeros([1]))
# y = Weights * x_data + biases
# # 计算误差MSE
# loss = tf.reduce_mean(tf.square(y - y_data))  # loss是个tensor对象/实例
# # 传播误差
# optimizer = tf.train.GradientDescentOptimizer(0.5)  # 一个梯度下降法的优化器
# train = optimizer.minimize(loss)
# # 训练
# init = tf.global_variables_initializer()  # 初始化变量
# sess = tf.Session()#或者with tf.Session() as sess激活回话
# sess.run(init)  # Very important
# for step in range(201):
#     sess.run(train)
#     if step % 20 == 0:
#         print(step, sess.run(Weights), sess.run(biases))

# 生成训练集
# 设置常量
# time_step = 10  # 时间步
# rnn_unit = 5  # hidden layer units
# batch_size = 30  # 每一批次训练多少个样例
# input_size = 1  # 输入层维度   
# output_size = 1  # 输出层维度
# lr = 0.0006  # 学习率
# train_x, train_y = [], []  # 训练集
# for i in range(len(normalize_data) - time_step - 1):
#     x = normalize_data[i:i + time_step]
#     y = normalize_data[i + 1:i + time_step + 1]
#     train_x.append(x.tolist())
#     train_y.append(y.tolist())
# print('train_y',len(train_y))
#
# # ——————————————————定义神经网络变量——————————————————
# X = tf.placeholder(tf.float32, [None, time_step, input_size])  # 每批次输入网络的tensor
# Y = tf.placeholder(tf.float32, [None, time_step, output_size])  # 每批次tensor对应的标签
# # 输入层、输出层权重、偏置
# weights = {
#     'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
#     'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
# }
# biases = {
#     'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
#     'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
# }
#
# # ——————————————————定义神经网络变量——————————————————
# # def lstm(batch):  # 参数：输入网络批次数目
# w_in = weights['in']
# b_in = biases['in']
# input = tf.reshape(X, [-1, input_size])  # 需要将tensor转成2维进行计算，计算后的结果作为隐藏层的输入
# input_rnn = tf.matmul(input, w_in) + b_in
# input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])  # 将tensor转成3维，作为lstm cell的输入
# cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
# init_state = cell.zero_state(batch_size, dtype=tf.float32)
# output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state,dtype=tf.float32)
# # output_rnn是记录lstm每个输出节点的结果，final_states是最后一个cell的结果
# output = tf.reshape(output_rnn, [-1, rnn_unit])  # 作为输出层的输入
# w_out = weights['out']
# b_out = biases['out']
# pred = tf.matmul(output, w_out) + b_out
#
# #判断训练模型是否生成，已经生成则不再重新生成
# if os.access("./model/stock.model.meta", os.F_OK):
#     print ("stock.model.meta file is exist.")
# else:
#     print("stock.model.meta file is not exist.")
#     # # ——————————————————训练模型——————————————————
#     # 损失函数
#     loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))
#     train_op = tf.train.AdamOptimizer(lr).minimize(loss)
#     print('tf.global_variables()', tf.global_variables())
#     saver = tf.train.Saver(tf.global_variables())
#     with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
#         # 重复训练10000次
#         for i in range(10000):
#             step = 0
#             start = 0
#             end = start + batch_size
#             while (end < len(train_x)):
#                 _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[start:end], Y: train_y[start:end]})
#                 start += batch_size
#                 end = start + batch_size
#                 # 每10步保存一次参数
#                 if step % 10 == 0:
#                     print(i, step, loss_)
#                     print("保存模型：", saver.save(sess, './model/stock.model'))
#                 step += 1
#
# # # ————————————————预测模型————————————————————
# # 预测时只输入[1,time_step,input_size]的测试数据
# saver = tf.train.Saver(tf.global_variables())
# with tf.Session() as sess:
#     # 参数恢复
#     module_file = tf.train.latest_checkpoint('./model/')
#     saver.restore(sess, module_file)
#
#     # 取训练集最后一行为测试样本。shape=[1,time_step,input_size]
#     prev_seq = train_x[-1]
#     # next_seq = sess.run(pred, feed_dict={X: [prev_seq]})
#     # print('next_seq',next_seq)
#     predict = []
#     # 得到之后10个预测结果
#     for i in range(10):
#         next_seq = sess.run(pred, feed_dict={X: [prev_seq]})
#         predict.append(next_seq[-1])
#         # 每次得到最后一个时间步的预测结果，与之前的数据加在一起，形成新的测试样本
#         prev_seq = np.vstack((prev_seq[1:], next_seq[-1]))
#     predict.to_csv('../Data/predict_LSTM.csv')
#     # 以折线图表示结果
#     plt.figure()
#     plt.plot(list(range(len(normalize_data))), normalize_data, color='b')
#     plt.plot(list(range(len(normalize_data), len(normalize_data) + len(predict))), predict, color='r')
#     plt.show()
#
