
import yaml
import pytest
import os, sys

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)


# 读取文件
def yaml_data_with_file(file_name):
    path = base_path + '/data/' + file_name + '.yml'
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


# 读取yaml数据中的key值，这里的yaml文件名是data
def yaml_data_with_key(key):
    return yaml_data_with_file('case_data')[key]


class Test_01():

    # 单参列表形式等价于
    # @pytest.mark.parametrize('name',['name1','name2'])
    # @pytest.mark.parametrize('name', yaml_data_with_key('join_list_data'))
    # def test_login(self, name):
    #     print('----')
    #     print(name)
    #     print('---')

    #  这里的多参给绑定元组方式
    #  ((value,passd)),[(value,passd),(value1,passd1)]
    #  yaml_data_with_key("value")中的value对应为data.yaml的键值
    # 相当于
    # @pytest.mark.parametrize(('name','password'),[('name3','password3'),('name4','password4')])
    @pytest.mark.parametrize(('name', 'password'), yaml_data_with_key('pro_list_data'))
    def test_login2(self, name, password):
        print('-----')
        print(name)
        print(password)
        print('-----')

    # 字典形式的数据
    # 字典形式就相当于{'name':'password'},此时他是一个整体那么在选择时就相当于
    # @pytest.mark.parametrize('dict1',[{'name':'name7','password':'password7'},{'name':'name8','password':'password8'}])
    # 这时就需要抓字典的key来实现参数化
    # @pytest.mark.parametrize('dict1', yaml_data_with_key('test_login2'))
    # def test_login3(self, dict1):
    #     print('-----')
    #     name=dict1['name']
    #     password=dict1['password']
    #     print(name)
    #     print(password)
    #     print('-----')


if __name__ == '__main__':
    pytest.main(['-s', 'read_yml.py'])
