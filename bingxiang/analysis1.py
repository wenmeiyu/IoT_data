import pandas as pd
import numpy as np

# if (fport != 36)
#     return {}
# var temperature = Number(bin[1] * 256 + bin[0]).toFixed(2);
# if (temperature > 32767)
#     temperature -= 65535;
# temperature = temperature * 0.01;
# temperature = temperature.toFixed(2);
# var humidity = Number((bin[3] * 256 + bin[2]) * 0.01).toFixed(2);
# if (humidity == null)
#     return {}
# var batteryvlotage = Number(bin[5] * 256 + bin[4]).toFixed(2);
# if (batteryvlotage == null)
#     return {}
# return {
#     T: temperature,
#     H: humidity,
#     V: batteryvlotage
# };

#  11:07   46f9211d490d  74.57	-17.21	3401
#  11:12   37f9391d490d  74.81	-17.36	3401

def to_num(str):

  list = str[0:2]
  temperature =int(str[2:4],16)*256+int(str[0:2],16)
  if (temperature > 32767):
      temperature -= 65535
  temperature = temperature * 0.01
  temperature = float('%.2f' % temperature)

  humidity=(int(str[6:8],16)*256+int(str[4:6],16))*0.01
  humidity=float('%.2f' % humidity)
  batteryvlotage = int(str[10:12],16)*256+int(str[8:10],16)

  return temperature,humidity,batteryvlotage

# str = '37f9391d490d'
# result=to_num(str)
# print(list)
# print(result)


data = pd.read_csv('data.csv',  encoding='utf-8')
data_time=data['time']

print(len(data))