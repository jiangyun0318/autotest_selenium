import os
import sys

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)

from util.handle_excel import excel_data
import unittest
import ddt
from keywordselenium.actionMethod import ActionMethod
import pytest

excel_path = base_path + '/data/keywords.xlsx'
data = excel_data.get_all_sheet(excel_path)
# print('excel_path', excel_path)
lis = []
for k in data:
    lis.append(tuple(k))
# print('data', lis)


class TestRunMain:

    action_method = ActionMethod()

    @pytest.mark.parametrize("case_id, a,a1,is_run,method,send_value,handle_value,except_result_method,except_result,a2", lis)
    # @pytest.mark.skipif(is_run='no')
    def test_run_case(self, case_id, a, a1, is_run, method, send_value, handle_value, except_result_method, except_result, a2):

        print(case_id, a, a1, is_run, method, send_value, handle_value, except_result_method, except_result)
        i = excel_data.get_rows_number(case_id, excel_path)
        self.run_method(method, send_value, handle_value)

        if except_result != None:
            except_value = self.get_except_result_value(except_result)
            if except_value[0] == 'text':
                result = self.run_method(except_result_method)
                if except_value[1] in result:
                    excel_data.excel_write_data(case_id, i, 10, "pass", excel_path)
                else:
                    excel_data.excel_write_data(case_id, i, 10, "fail", excel_path)
            elif except_value[0] == 'element':
                result = self.run_method(except_result_method, except_value[1])
                if result:
                    excel_data.excel_write_data(case_id, i, 10, "pass", excel_path)
                else:
                    excel_data.excel_write_data(case_id, i, 10, "fail", excel_path)
            else:
                print("没有else")
        else:
            print('预期结果为空,继续走~')

    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, method, send_value=None, handle_value=None):

        method_value = getattr(self.action_method, method)
        if send_value is None and handle_value is not None:
            result = method_value(handle_value)
        elif send_value is None and handle_value is None:
            result = method_value()
        elif send_value is not None and handle_value is None:
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result
