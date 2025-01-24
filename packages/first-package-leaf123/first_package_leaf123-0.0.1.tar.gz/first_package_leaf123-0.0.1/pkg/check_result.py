# -*- coding: utf-8 -*-

import datetime
import time
import re


class CheckResult:

    def compare_expected(self, response_dict, expected_list, params_config, session, instance_aid, week_check,
                         action):
        reason = {'cplc': params_config.get('cplc'), 'case_session': session}
        actual_value = ''
        compare_result = False
        week_tag = False
        data_dict = response_dict
        update_tag = False
        if not expected_list:
            return True, week_tag, update_tag, reason

        resp_code = response_dict.get('resp_code')
        resp_msg = response_dict.get('resp_msg')
        result_code = response_dict.get('result_code')
        result_msg = response_dict.get('result_msg')
        next_action = response_dict.get('next_action')
        code = response_dict.get('code')
        message = response_dict.get('message')
        expected_dict = {}
        for expected_dict in expected_list:
            key = expected_dict.get('key')
            method = expected_dict.get('method')
            if method == 'value_unequal':
                update_tag = True
            expected = expected_dict.get('expected')

            if isinstance(expected, str):
                expected_res = re.match(r'\${(.+)}', expected)  # ${}表示从设备数据中取值
            else:
                expected_res = ''

            if isinstance(expected, int):
                pass
            elif expected_res:
                expected_key = expected_res.group(1)
                expected = params_config.get(expected_key)
            elif expected == 'default' and key == 'instance_aid':
                expected = instance_aid

            if key == 'resp_code':
                actual_value = resp_code if resp_code else result_code
            elif key == 'resp_msg':
                actual_value = resp_msg if resp_msg else result_msg
            elif key == 'result_code':
                actual_value = result_code if result_code else resp_code
            elif key == 'result_msg':
                actual_value = result_msg if result_msg else resp_msg
            elif key == 'next_action':
                actual_value = next_action
            elif key == 'code':
                actual_value = code
            elif key == 'message':
                actual_value = message

            if 'value_equal' == method:
                compare_result = self.judgeValueEqual(expected, actual_value)
            elif 'value_equal_ignore_field_type' == method:
                compare_result = self.judgeValueEqualIgnoreFieldType(expected, actual_value)
            elif 'value_unequal' == method:
                compare_result = self.judgeValueUnequal(expected, actual_value)
            elif 'length_equal' == method:
                compare_result = self.judgeLengthEqual(expected, actual_value)
            elif 'length_unequal' == method:
                compare_result = self.judgeLengthUnequal(expected, actual_value)
            elif 'contain' == method:
                compare_result = self.judgeContain(expected, actual_value)
            elif 'not_contain' == method:
                compare_result = self.judgeNotContain(expected, actual_value)
            elif 'validate' == method:
                compare_result = self.judgeValidate(actual_value)
            elif 'invalidate' == method:
                compare_result = self.judgeInvalidate(actual_value)
            elif 'empty' == method:
                compare_result = self.judgeEmpty(actual_value)
            elif 'not_empty' == method:
                compare_result = self.judgeNotEmpty(actual_value)
            elif 'date_format' == method:
                compare_result = self.checkDateFormat(actual_value)
            elif 'be_one_of' == method:
                expected = expected.replace(' ', '')
                compare_result = self.judgeBeOneOf(expected, actual_value)
            elif 'not_existed' == method:
                compare_result = self.judgeNotExisted(expected, actual_value)
            elif 'size_equal' == method:
                compare_result = self.judgeSizeEqual(expected, actual_value)
            expected_dict['expected_value'] = expected
            expected_dict['actual_value'] = actual_value
            if not compare_result:
                if action == 'db_query':
                    temp_ori_dict = week_check.get(key)
                    if temp_ori_dict:  # 有配置才做弱校验
                        week_check_list = temp_ori_dict.get('week_check')
                        if method in week_check_list:  # 弱校验
                            compare_result = True
                            week_tag = True
                            continue
                        else:
                            break
                    else:
                        week_tag = False
                else:
                    if key in week_check:  # 弱校验
                        compare_result = True
                        week_tag = True
                        continue
                    else:
                        break
        if not compare_result:
            reason.update(expected_dict)
        return compare_result, week_tag, update_tag, reason

    # 判断值是否相等
    def judgeValueEqual(self, expected, actual_value):
        return expected == actual_value

    # 判断值是否相等,忽略值类型
    def judgeValueEqualIgnoreFieldType(self, expected, actual_value):
        return str(expected) == str(actual_value)

    # 判断值是否不相等
    def judgeValueUnequal(self, expected, actual_value):
        return (str(expected).upper() != str(actual_value).upper())

    # 判断长度是否相等
    def judgeLengthEqual(self, expected, actual_value):
        if not actual_value:
            return False
        return (len(actual_value) == int(expected))

    # 判断长度是否不等
    def judgeLengthUnequal(self, expected, actual_value):
        if not actual_value:
            return False
        return (len(actual_value) != int(expected))

    # 判断actual_value字符串中是否包含expected字符
    def judgeContain(self, expected, actual_value):
        return (str(actual_value).upper().find(str(expected).upper()) >= 0)

    # 判断actual_value字符串中是否不包含expected字符
    def judgeNotContain(self, expected, actual_value):
        return (str(actual_value).upper().find(str(expected).upper()) < 0)

    # 判断卡片有效期是否合法（是否在有效期内）
    def judgeValidate(self, actual_value):
        now = datetime.datetime.now()
        # 转换成时间数
        timeArray_now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp_now = time.mktime(timeArray_now)
        if '-' in actual_value:
            timeArray = time.strftime(actual_value, "%Y-%m-%d")
        else:
            timeArray = time.strftime(actual_value, "%Y%m%d")
        timestamp = time.mktime(timeArray)
        return (timestamp_now <= timestamp)

    # 判断卡片有效期是否不合法（已超出有效期）
    def judgeInvalidate(self, actual_value):
        now = datetime.datetime.now()
        # 转换成时间数
        timeArray_now = time.strptime(now, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp_now = time.mktime(timeArray_now)

        if '-' in actual_value:
            timeArray = time.strftime(actual_value, "%Y-%m-%d")
        else:
            timeArray = time.strftime(actual_value, "%Y%m%d")
        timestamp = time.mktime(timeArray)
        return (timestamp_now > timestamp)

    # 判断字符串是否为None
    def judgeEmpty(self, actual_value):
        return (actual_value == None or actual_value == '')

    # 判断字符串是否不为Non
    def judgeNotEmpty(self, actual_value):
        return (actual_value != None and actual_value != '')

    # 检查日期格式
    def checkDateFormat(self, actual_value):
        try:
            if "-" in actual_value:
                time.strptime(actual_value, "%Y-%m-%d")
            else:
                time.strptime(actual_value, "%Y%m%d")
            return True
        except:
            return False

    # 判断actual_value是否是expected中的某一个
    def judgeBeOneOf(self, expected, actual_value):
        expected_list = expected.split('|')
        if isinstance(actual_value, int):
            expected_list = list(map(lambda x: int(x), expected_list))
        elif isinstance(actual_value, float):
            expected_list = list(map(lambda x: float(x), expected_list))
        return (actual_value in expected_list)

    def judgeNotExisted(self, expected, actual_value):
        if isinstance(expected, dict):
            if isinstance(actual_value, list):
                for val in actual_value:
                    if isinstance(val, dict):
                        if len(expected) == len(expected.items() & val.items()):
                            return False
                else:
                    return True
            else:
                if len(expected) == len(expected.items() & actual_value.items()):
                    return False
                else:
                    return True
        else:
            return (expected not in actual_value)

    def judgeSizeEqual(self, expected, actual_value):
        return len(actual_value) == int(expected)


check = CheckResult()
