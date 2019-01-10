# -*- coding: UTF-8 -*-
import pymysql as mdb


def mysql_create():
    db =  mdb.connect('localhost', 'root', '19880511', 'shuichan');# 连接数据库编码注意是utf8，不然中文结果输出会乱码
    sql_create = "CREATE TABLE DUMPLINGS (id CHAR(10),order_no CHAR(50),order_title VARCHAR(265),publish_desc VARCHAR(265),game_name VARCHAR(265)," \
                 "game_area VARCHAR(265),game_area_distinct VARCHAR(265),order_current VARCHAR(3908),order_content VARCHAR(3908),order_hours CHAR(10)," \
                 "order_price FLOAT(10),add_price FLOAT(10),safe_money FLOAT(10),speed_money FLOAT(10),order_status_desc VARCHAR(265)," \
                 "order_lock_desc VARCHAR(265),cancel_type_desc VARCHAR(265),kf_status_desc VARCHAR(265),is_show_pwd TINYINT,game_pwd CHAR(50)," \
                 "game_account VARCHAR(265),game_actor VARCHAR(265),left_hours VARCHAR(265),created_at VARCHAR(265),account_id CHAR(50)," \
                 "mobile VARCHAR(265),mobile2 VARCHAR(265),contact VARCHAR(265),contact2 VARCHAR(265),qq VARCHAR(265)," \
                 "PRIMARY KEY (`id`),UNIQUE KEY `no`(`order_no`))ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8"
    sql_key = "CREATE UNIQUE INDEX id ON DUMPLINGS(id)"
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS DUMPLINGS")
    cursor.execute(sql_create)  # 执行SQL语句
    cursor.execute(sql_key)
    db.close()  # 关闭数据库连




def IntoMysql(results):
    db = mdb.connect('localhost', 'root', '19880511', 'shuichan');
    cursor = db.cursor()
    for j in range(len(results)):
        try:
            sql = "INSERT INTO shuichan(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity) VALUES ("
            for i in range(len(results[j])):
                sql = sql + "'" + results[j][i] + "',"
            sql = sql[:-1] + ")"
            sql = sql.encode('utf-8')
            cursor.execute(sql)
            db.commit()
        except:
            pass
    db.close()



##begin
con = mdb.connect('localhost', 'root', '19880511', 'shuichan');
results=[['XSCY10180101TEST0100029','2016/9/2 0:00','2018/9/1 23:59', 4.45,7.67,26,5],['XSCY10180101TEST0100030','2016/9/2 0:00','2018/9/1 23:59', 4.45,7.67,26,5]]
print(results[0][0])

for i in range(len(results)):

  if results[i][0]=='XSCY10180101TEST0100029':
      sheb_id =1
  else:
      sheb_id =2
  sheb_num = results[i][0]
  data_time = results[i][1]
  get_time = results[i][2]
  dis_o = results[i][3]
  ph = results[i][4]
  w_temp = results[i][5]
  turbidity = results[i][6]

  with con:
      cur = con.cursor()
      sql = "INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)" \
            "VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity)
      cur.execute(sql)

con.close()



# result = get_data()
# json_to_python = json.loads(result)
# result_data = json_to_python['data']
# result_key = list(result_data.keys())
# # print(result_key[0])
# # a=datetime.datetime.strptime(result_data[result_key[0]]['T3'], '%Y-%m-%d %H:%M') + datetime.timedelta(minutes=-1)
# # aa=a.strftime('%Y-%m-%d %H:%M')
# # print(aa)
# results = [[] for i in range(len(result_key))]
#
# for i in range(len(result_key)):
#     results[i].append(result_key[i])
#     a = datetime.datetime.strptime(result_data[result_key[i]]['T3'], '%Y-%m-%d %H:%M') + datetime.timedelta(minutes=-1)
#     aa = a.strftime('%Y-%m-%d %H:%M')
#     results[i].append(aa)
#     results[i].append(result_data[result_key[i]]['T3'])
#     results[i].append(result_data[result_key[i]]['C1'] + result_data[result_key[i]]['C2'])
#     results[i].append(result_data[result_key[i]]['C3'] + result_data[result_key[i]]['C4'])
#     results[i].append(result_data[result_key[i]]['C5'])
#     results[i].append(result_data[result_key[i]]['C17'] + result_data[result_key[i]]['C18'])
#
# print(results)