import json
import traceback
from json.decoder import JSONDecodeError

import requests


def loadjson(filename, method):
    dict = None
    try:
        # 读取请求的json对象
        f = open(filename)
        jsonFile = json.load(f)
        # 将全部json信息封装成dict
        if method == "POST":
            json_dict = post_file(jsonFile)
            # 关闭文件流
            f.close()
            # 调用getrespose方法
            dict = postresponse(method, json_dict["url"], json_dict["headers"], json_dict["data"])
        elif method == "GET":
            json_dict = get_file(jsonFile)
            # 关闭文件流
            f.close()
            # 调用getrespose方法
            dict = getresponse(method, json_dict["url"], json_dict["headers"])
        else:
            print("请求方法出错，GET和POST查看请求方法是否拼写正确！")
            return None
    except IOError:
        print("读取Json文件出错，请检查文件路径或者文件是否存在")
    finally:
        return dict


def postresponse(method, url, headers, payload):
    list = None
    try:
        # POST接口调用
        response = requests.request(method, url, headers=headers, data=json.dumps(payload))
        if response.status_code >= 400:
            print("请求链接响应失败！状态码：", response.status_code)
        else:
            # 对返回的JSON对象转义成python对象
            result = json.loads(response.text)
            # 获取响应的状态码和功能是否成功运行
            # print("Http Code:", response.status_code, "Message:", result["msg"])
            print("请求链接响应成功！状态码：", response.status_code)
            print("功能运行代码 CODE：", result["code"], "，运行信息：", result["msg"])
            list = {'status code': response.status_code, 'result code': result["code"], 'message': result["msg"]}
    except JSONDecodeError:
        print("json转换为map类型时出错，请查看响应返回的数据")
    except:
        traceback.print_exc()
    finally:
        return list


def getresponse(method, url, headers):
    list = None
    try:
        # POST接口调用
        response = requests.request(method, url, headers=headers)
        if response.status_code >= 400:
            print("请求链接响应失败！状态码：", response.status_code)
        else:
            # 对返回的JSON对象转义成python对象
            result = json.loads(response.text)
            # 获取响应的状态码和功能是否成功运行
            # print("Http Code:", response.status_code, "Message:", result["msg"])
            print("请求链接响应成功！状态码：", response.status_code)
            print("功能运行代码 CODE：", result["code"], "，运行信息：", result["msg"])
            list = {'status code': response.status_code, 'result code': result["code"], 'message': result["msg"]}
    except JSONDecodeError:
        print("json转换为map类型时出错，请查看响应返回的数据")
    except:
        traceback.print_exc()
    finally:
        return list


def post_file(file):
    # 请求地址
    url = file["url"]
    # 请求头
    headers = file["headers"]
    # 请求数据
    payload = file["data"]
    return {"url": url, "headers": headers, "data": payload}


def get_file(file):
    # 请求地址
    url = file["url"]
    # 请求头
    headers = file["headers"]
    return {"url": url, "headers": headers}
