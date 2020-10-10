# coding=utf-8

import configparser
import os
import sys

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)


class HandleInit:

    def load_ini(self):
        file_path = base_path + '/config/config.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    # 获取ini里面的value
    def get_value(self, key, node=None):
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


get_init_data = HandleInit()


if __name__ == "__main__":
    hi = HandleInit()
    print(hi.get_value("username", "DB"))
