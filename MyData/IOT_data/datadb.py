# -*- coding:utf-8 -*-
"""
链接远程数据库
"""
import MySQLdb

# conn = MySQLdb.connect(host='210.75.252.89', user='iot_root', passwd='123456', db='iot', charset='utf8',port = 3306,)
# c_cursor = conn.cursor()  # 创建一个光标，然后通过光标执行sql语句
# c_cursor.execute("select * from tb_customer limit 10")
# values = c_cursor.fetchall()  # 取出cursor得到的数据
# print(values)
# c_cursor.close();
# conn.close()  #最后记得关闭光标和连接，防止数据泄露


# db = MySQLdb.connect(host='218.17.171.90', user='dingzhiwen', passwd='Dzw@123456', db='siat_iot', charset='utf8')
# cur = db.cursor()
# cur.execute("select * from tb_sensor_data limit 1")
# result = cur.fetchall()
# print(result)


db = MySQLdb.connect(host='218.17.171.90', user='dingzhiwen', passwd='Dzw@123456', db='siat_iot', charset='utf8')
cur = db.cursor()
cur.execute("select tb2.eui,tb2.temperature 温度,tb2.humidity 湿度, tb2.batt 电量,tb2.current 电流,tb2.voltage 电压,tb2.power 功率,tb2.ts 获取时间,tb1.name 传感器名称,tb3.name 所属设备,tb4.name 所属酒店\
                                            from tb_sensor_data tb2 LEFT JOIN tb_sensor tb1 on tb1.code = tb2.eui LEFT JOIN tb_equipment tb3 on tb3.equipment_id = tb1.equipment_id \
                                            LEFT JOIN tb_customer tb4 on tb4.customer_id = tb1.customer_id where (tb2.eui='9896830000000008' or tb2.eui='9896830000000002' or tb2.eui = '9896830000000003' \
                                             or tb2.eui='9896830000000004' or tb2.eui = '9896830000000006' or tb2.eui = '3786E6ED0034004B' or \
                                             tb2.eui = '3768B26900230053' or tb2.eui = '4768B269002B0059' or tb2.eui = '4768B269001F003F' or \
                                             tb2.eui='4778B269003B002F' or tb2.eui='3430363057376506' or tb2.eui='3430363067378B07' or tb2.eui = '3430363064378607' \
                                             or tb2.eui='343036305D375E05' or tb2.eui = '3430363064378007') limit 10")
result = cur.fetchall()
print(result)
