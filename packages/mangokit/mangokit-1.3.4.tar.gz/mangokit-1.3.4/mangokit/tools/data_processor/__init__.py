# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description:
# @Time   : 2023-03-07 8:24
# @Author : 毛鹏
import json
import re

from mangokit.exceptions import ERROR_MSG_0028, ERROR_MSG_0002, ERROR_MSG_0047, MangoKitError
from mangokit.tools.data_processor.cache_tool import CacheTool
from mangokit.tools.data_processor.coding_tool import CodingTool
from mangokit.tools.data_processor.encryption_tool import EncryptionTool
from mangokit.tools.data_processor.json_tool import JsonTool
from mangokit.tools.data_processor.random_character_info_data import RandomCharacterInfoData
from mangokit.tools.data_processor.random_number_data import RandomNumberData
from mangokit.tools.data_processor.random_string_data import RandomStringData
from mangokit.tools.data_processor.random_time_data import RandomTimeData

"""
ObtainRandomData类的函数注释必须是： “”“中间写值”“”
"""


class ObtainRandomData(RandomNumberData, RandomCharacterInfoData, RandomTimeData, RandomStringData):
    """ 获取随机数据 """

    def regular(self, func: str):
        """
        反射并执行函数
        :param func: 函数
        :return:
        """
        match = re.search(r'\((.*?)\)', func)
        if match:
            try:
                content = json.loads(match.group(1))
                if not isinstance(content, dict):
                    content = {'data': match.group(1)}
            except json.decoder.JSONDecodeError:
                content = {'data': match.group(1)}

            func = re.sub(r'\(' + match.group(1) + r'\)', '', func)
            try:
                if content['data'] != '':
                    return getattr(self, func)(**content)
                return getattr(self, func)()
            except AttributeError:
                raise MangoKitError(*ERROR_MSG_0047)


class DataClean(JsonTool, CacheTool, EncryptionTool, CodingTool):
    """存储或处理随机数据"""
    pass


class DataProcessor(ObtainRandomData, DataClean):

    def __init__(self):
        ObtainRandomData.__init__(self)
        DataClean.__init__(self)

    def replace(self, data: list | dict | str | None) -> list | dict | str | None:
        if not data:
            return data
        if isinstance(data, list):
            return [self.replace(item) for item in data]
        elif isinstance(data, dict):
            return {key: self.replace(value) for key, value in data.items()}
        else:
            return self.replace_str(data)

    @classmethod
    def specify_replace(cls, data: str, replace: str):
        replace_list = re.findall(r"\${.*?}", str(data))
        if len(replace_list) > 1:
            raise MangoKitError(*ERROR_MSG_0028)
        return data.replace(replace_list[0], replace)

    def replace_str(self, data: str) -> str:
        """
        用来替换包含${}文本信息，通过读取缓存中的内容，完成替换（可以是任意格式的文本）
        @param data: 需要替换的文本
        @return: 返回替换完成的文本
        """
        replace_list = re.findall(r"\${.*?}", str(data))
        for replace_value in replace_list:
            key_text = self.remove_parentheses(replace_value)
            args = key_text.split(",")
            if len(args) == 2:
                key_text = args[0].strip()
                key = args[1].strip()
            else:
                key_text = args[0].strip()
                key = None
            # 检查key是否有值，有值则直接返回
            if key:
                key_value = self.get_cache(key)
                if key_value:
                    return key_value
            match = self.identify_parentheses(key_text)
            if match:
                value = self.regular(key_text)
            else:
                value = self.get_cache(key_text)
            if value is None:
                raise MangoKitError(*ERROR_MSG_0002, value=(key_text,))
            if key:
                self.set_cache(key, value)
            data = data.replace(replace_value, str(value))
        return data

    @classmethod
    def remove_parentheses(cls, data: str) -> str:
        return data.replace("${", "").replace("}", "").strip()

    @classmethod
    def identify_parentheses(cls, value: str):
        return re.search(r'\((.*?)\)', str(value))

    @classmethod
    def is_extract(cls, string: str) -> bool:
        return True if re.search(r'\$\{.*\}', string) else False


if __name__ == '__main__':
    # 把变量进行使用，并且存到环境中
    str_ = "${number_time_5(),flow名称}"
    r = DataProcessor()
    print(r.replace(str_))
    print(r.replace('${md5_32_small(123456)}'))
    # # 多层嵌套
    # str_ = "${姓名：${name}}"
    # r.set_cache('name', 'maopeng')
    # r.set_cache('姓名：maopeng', '27')
    # print(r.replace(str_))
