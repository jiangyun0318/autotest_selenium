import requests
from common import get_data
import json
from common.get_init import get_init_data


# 写字楼查询接口
def pro_api_query(data):

    base = get_init_data.get_value('host', 'HTTP')
    url = base + '/property/queryMoPropertyJointListPC'
    header = {"Content-Type": "application/json"}
    re = requests.request("post", url=url, data=json.dumps(data), headers=header).json()
    return int(re['data']['total'])


# 联合办公查询接口
def join_api_query(data):

    base = get_init_data.get_value('host', 'HTTP')
    url = base + '/jointOffice/queryMoJointList'
    header = {"Content-Type": "application/json"}
    re = requests.request("post", url=url, data=json.dumps(data), headers=header).json()
    return int(re['data']['total'])


# 整租办公室接口
def off_api_query(data):

    base = get_init_data.get_value('host', 'HTTP')
    url = base + '/office/queryMoOfficeList'
    header = {"Content-Type": "application/json"}
    re = requests.request("post", url=url, data=json.dumps(data), headers=header).json()
    return int(re['data']['total'])


if __name__ == '__main__':
    print(pro_api_query(get_data.get_value('contry')))
