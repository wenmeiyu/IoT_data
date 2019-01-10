# # -*- coding: UTF-8 -*-
# import pymysql as mdb
# import sys
#
# results =0
# # 将con设定为全局连接
# con = mdb.connect('localhost', 'root', '19880511', 'shuichan');
#     for i in range(len(results)):
#         if results[i][0] == 'XSCY10180101TEST0100029':
#             sheb_id = 1
#         else:
#             sheb_id = 2
#         sheb_num = results[i][0]
#         data_time = results[i][1]
#         get_time = results[i][2]
#         dis_o = results[i][3]
#         ph = results[i][4]
#         w_temp = results[i][5]
#         turbidity = results[i][6]
#
#         with con:
#             cur = con.cursor()
#             sql = "INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)" \
#                   "VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
#                       sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity)
#             cur.execute(sql)
#
#     con.close()