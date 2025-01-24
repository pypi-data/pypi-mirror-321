import os
import sys
import abc
import json

import yaml
import aiohttp
import requests

from chariot_scaffold import plugin_spec
from chariot_scaffold.core.base import Base
from chariot_scaffold.core.config import Lang
from chariot_scaffold.tools import generate_file
from chariot_scaffold.exceptions import TriggerError, PackError
from chariot_scaffold.tools import generate_online_pack, generate_offline_pack


requests.packages.urllib3.disable_warnings() # noqa


class Connection(Base):
    def __init__(self, model=None):
        """
        连接器
        :param model: 强类型校验
        """
        super().__init__(model=model)

    def hook(self):
        # connection = {}
        # print(self.input)
        # for k, v in self.input.items():
        #     connection[k] = {"title": v["title"], "description": v["description"], "type": v["type"]}
        #
        #     if v["required"]:
        #         connection[k]["required"] = v["required"]
        #     if v["default"] is not None:
        #         connection[k]["default"] = v["default"]
        #     if v.get("enum"):
        #         connection[k]["enum"] = v["enum"]

        plugin_spec.connection = self.input


class Action(Base):
    def __init__(self, title=None, description=None, model=None, example=None):  # noqa
        """
        动作
        :param title: 名称
        :param description: 描述
        :param model: 强类型校验
        """
        self.example = example
        super().__init__(title, description, model)

    def hook(self):
        actions = {
            self._func_name: {
                "title": self.lang_checking(self.title),
                "description": self.lang_checking(self.description),
                "input": self.input,
                "output":self.output
            }
        }

        if self.example is not None:
            actions[self._func_name]["example"] = self.example

        # for k, v in self.input.items():
        #     actions[self._func_name]["input"][k] = {"title": v["title"], "description": v["description"],
        #                                             "type": v["type"]}
        #
        #     if v["required"]:
        #         actions[self._func_name]["input"][k]["required"] = v["required"]
        #     if v["default"] is not None:
        #         actions[self._func_name]["input"][k]["default"] = v["default"]
        #     if v.get("enum"):
        #         actions[self._func_name]["input"][k]["enum"] = v["enum"]
        #
        # if not self.output.get("output"):
        #     actions[self._func_name]["output"] = self.output
        #     # # 返回值注解绑定
        #     # for k, v in self.output.items():
        #     #     print(k, v)
        #     #     actions[self._func_name]["output"][k] = {
        #     #         "title": v["title"],
        #     #         "description": v["description"],
        #     #         "type": v["type"]
        #     #     }
        #     # print(actions[self._func_name]["output"])
        # else:
        #     # 默认返回值绑定
        #     actions[self._func_name]["output"]["output"] = {
        #         "title": Lang("输出", "output").convert(),
        #         "description": Lang("系统默认输出", "System Default Output").convert(),
        #         "type": self.output["output"]["type"]
        #     }

        plugin_spec.actions.update(actions)


class Trigger(Base):
    def __init__(self, title=None, description=None, model=None, trigger_type="alarm_receivers"):  # noqa
        """
        触发器
        :param title: 名称
        :param description: 描述
        :param model: 强类型校验
        :param trigger_type: 触发器类型, 目前就两种告警触发器和资产触发器即alarm_receivers, asset_receivers. 默认alarm_receivers.
        """
        trigger_types = ["alarm_receivers", "asset_receivers"]
        if trigger_type not in trigger_types:
            raise TriggerError("请传入一个正确的触发器类型")

        self.trigger_type = trigger_type
        super().__init__(title, description, model)

    def hook(self):
        trigger = {
            self._func_name: {
                "title": self.lang_checking(self.title),
                "description": self.lang_checking(self.description),
                "input": self.input}
        }
        # for k, v in self.input.items():
        #     trigger[self._func_name]["input"][k] = {
        #         "title": v["title"],
        #         "description": v["description"],
        #         "type": v["type"]
        #     }
        #
        #     if v["required"]:
        #         trigger[self._func_name]["input"][k]["required"] = v["required"]
        #     if v["default"] is not None:
        #         trigger[self._func_name]["input"][k]["default"] = v["default"]
        #     if v.get("enum"):
        #         trigger[self._func_name]["input"][k]["enum"] = v["enum"]

        eval(f"plugin_spec.{self.trigger_type}.update(trigger)")  # 若类型异常则检查trigger_types是否存在于plugin_spec


class TriggerExtend:
    def __init__(self, dispatcher_url, cache_url):
        self.__session = requests.Session()
        self.dispatcher_url = dispatcher_url
        self.cache_url = cache_url

    def send(self, alarm):
        """发送告警给千乘"""
        # 通过该打印接口的响应可以得到告警转发的状态码和提示
        response = self.__session.post(self.dispatcher_url, verify=False, json=alarm)
        return response.json()

    async def async_send(self, session: aiohttp.ClientSession, data):
        async with session.post(self.dispatcher_url, json=data) as response:
            return await response.json()

    def set_cache(self, data):
        cache = {
            "method": "set",
            "data": json.dumps(data),
        }
        response = self.__session.post(self.cache_url, json=cache, verify=False)
        return response.json()

    async def async_set_cache(self, session: aiohttp.ClientSession, data):
        # async with ClientSession() as session
        cache = {
            "method": "set",
            "data": json.dumps(data),
        }
        async with session.post(self.cache_url, json=cache) as response:
            return await response.json()

    def get_cache(self):
        method = {
            "method": "get"
        }
        response = self.__session.post(self.cache_url, json=method, verify=False)
        return response.json()

    async def async_get_cache(self, session: aiohttp.ClientSession):
        method = {
            "method": "get"
        }
        async with session.post(self.cache_url, json=method) as response:
            return await response.json()


class Pack(metaclass=abc.ABCMeta):
    __platform = None

    def __init__(self):
        self.trigger_no_need_connection = False # 用于触发器绑定或者解绑连接器，用于触发器启动无需运行连接器的情况
        self.create_trigger_extend()
        self.before_startup()

    @abc.abstractmethod
    def connection(self, *args, **kwargs):
        ...

    def before_startup(self):
        ...

    def after_closing(self):
        ...

    @classmethod
    def plugin_config_init(
            cls, name, title=None, description=None, version=None, tags: list | None = None, vendor="chariot",
            types: list | None = None, platform="linux/amd64", category=""
    ):
        """
        初始化参数配置
        :param name: 插件id, 以字母、下划线方式命名, 例如chariot_plugin. 请勿使用特殊字符
        :param title: 插件标题, 即展示在千乘页面的插件名称
        :param description: 插件描述, 即展示在千乘页面的插件描述
        :param version: 插件版本
        :param tags:    插件标签, 为了方便在插件社区里搜索
        :param vendor:  作者
        :param types: 自定义类型
        :param platform: 平台架构默认使用x86或者amd64, 镜像默认使用python:3.10.7-slim
        除此之外其他架构的tag还有 linux/amd64 linux/arm64/v8 linux/ppc64le linux/mips64le linux/arm/v7 linux/386 按需选择.
        若指定架构后仍然无法打包, 请手动pull一下指定平台的python镜像, 若pull成功则打包也能成功, 若pull失败请排查相关问题后再打包.
        :param category: 插件类型的分类名称
        :return:
        """
        
        cls.__platform = platform
        plugin_spec.entrypoint = os.path.split(os.path.abspath(
            sys.modules[cls.__module__].__file__))[-1].replace('.py','')
        plugin_spec.types = {}
        plugin_spec.module = cls.__name__
        plugin_spec.title = cls.lang_checking(title) if title else cls.lang_checking(cls.__name__)
        plugin_spec.version = version if version else "0.1.0"
        plugin_spec.description = cls.lang_checking(description)

        plugin_spec.name = name
        plugin_spec.tags = tags if tags else []
        plugin_spec.vendor = vendor  # 作者
        plugin_spec.type = category

        def custom_types():
            # 自定义类型绑定
            # 通过pydantic中Basemodel来绑定
            _types = {}
            if types is not None:
                for i in types:
                    if i.__class__.__name__ == "ModelMetaclass":
                        _types[i.__name__] = {}
                        for k,v in i.__annotations__.items():
                            assert len(v.__metadata__) >= 2, PackError("Annotated中至少需要包含title, description")
                            param_type = v.__origin__
                            ano_title = v.__metadata__[0]
                            ano_description = v.__metadata__[1]

                            _types[i.__name__][k] = {
                                    "title": cls.lang_checking(ano_title),
                                    "description": cls.lang_checking(ano_description),
                                    "type": param_type.__name__
                                }

                # print(_types)
                plugin_spec.types = _types
        custom_types()

    @staticmethod
    def lang_checking(param):  # 兼容过去默认绑定中文的插件
        if isinstance(param, str):
            return {"zh-CN": param}
        elif isinstance(param, Lang):
            return param.convert()

    @classmethod
    def generate_online_pack(cls, path=None):
        file_path = os.path.abspath(sys.modules[cls.__module__].__file__) if path is None else path
        assert os.path.exists(file_path), PackError("目录不存在")
        generate_online_pack(file_path, plugin_spec.name, plugin_spec.vendor, plugin_spec.version)

    @classmethod
    def generate_offline_pack(cls, path=None):
        file_path = os.path.abspath(sys.modules[cls.__module__].__file__) if path is None else path
        assert os.path.exists(file_path), PackError("目录不存在")
        generate_offline_pack(file_path, plugin_spec.name, plugin_spec.vendor, plugin_spec.version, cls.__platform)

    @classmethod
    def multi_name_detect(cls, func_name):
        """注册类重名检测"""
        if func_name in cls.__dict__.keys() and func_name != "__init__":
            raise PackError("注册类方法名请勿与插件类方法重名")

    def create_trigger_extend(self):
        """热加载Session"""
        if plugin_spec.alarm_receivers or plugin_spec.asset_receivers:
            self.register(TriggerExtend, *(self.dispatcher_url, self.cache_url))

    def register(self, object_: object, *args, **kwargs):
        """
        注册其他类方法到插件中, 用于分模块编写插件，便于阅读。*args, **kwargs是给你传的object用的。
        """
        obj = object_(*args, **kwargs)  # noqa
        for k, v in object_.__dict__.items():
            if hasattr(v, "__call__") and k != "__init__":
                self.multi_name_detect(k)
                exec(f"self.__dict__[k] = obj.{k}")

    def create_yaml(self, path=None):
        file_path = path if path is not None else "./"
        assert os.path.exists(file_path), PackError("目录不存在")
        stream = open(os.path.join(file_path, "plugin.spec.yaml"), 'w', encoding='utf8')
        yaml.safe_dump(self.json, stream, allow_unicode=True, sort_keys=False, default_flow_style=False)

    def generate_project(self, path=None):
        self.create_yaml(path=path)
        generate_file(module=plugin_spec.module, entrypoint=plugin_spec.entrypoint, path=path)

    @property
    def yaml(self):
        return yaml.safe_dump(self.json, allow_unicode=True, sort_keys=False)

    @property
    def json(self):
        return plugin_spec.dict()

    @property
    def dispatcher_url(self):
        return "http://127.0.0.1:10001/transpond"

    @dispatcher_url.setter
    def dispatcher_url(self, url):
        self.dispatcher_url = url

    @property
    def cache_url(self):
        return ""

    @cache_url.setter
    def cache_url(self, url):
        self.cache_url = url

    @property
    def webhook_url(self):
        return ""

    @webhook_url.setter
    def webhook_url(self, url):
        self.webhook_url = url

    def __repr__(self):
        return plugin_spec.model_dump_json()
