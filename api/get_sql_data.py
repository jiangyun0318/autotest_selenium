import os
import sys

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)

from common.get_sql import mysql
from common import get_data


# 联办-商圈-查询
def get_sql(sql):
       sql_data = ''
       result = mysql.getOne(sql)
       for res in result:
              sql_data = result[res]
       return int(sql_data)


if __name__ == '__main__':
       print(get_sql(get_data.get_value('contry', '/data/sql_data.json')))
