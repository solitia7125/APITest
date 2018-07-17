#!/usr/bin/env python
# coding: utf-8

import unittest
import PublicMethod as pm
import os


class TestFunc(unittest.TestCase):
    def setUp(self):
        print("start testing...")

    def test_1_register(self):
        print("测试register接口")
        filename = os.getcwd() + "/Authentication/Register.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_2_login(self):
        print("测试login接口")
        filename = os.getcwd() + "/Authentication/login.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_changepwd(self):
        print("测试Change_pwd接口")
        filename = os.getcwd() + "/Authentication/ChangePWD.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_setrole(self):
        print("测试setrole接口")
        filename = os.getcwd() + "/Authentication/SetRole.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_sign_up(self):
        print("测试signup接口")
        filename = os.getcwd() + "/Authentication/Signup.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_sms_send(self):
        print("测试sms_send接口")
        filename = os.getcwd() + "/Authentication/SMS_Send.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_update_userinfo(self):
        print("测试userinfo接口")
        filename = os.getcwd() + "/Authentication/Update_Userinfo.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_update_phone(self):
        print("测试update_phone接口")
        filename = os.getcwd() + "/Authentication/Update_Phone.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_wechat_code(self):
        print("测试wechat_code接口")
        filename = os.getcwd() + "/Authentication/Wechat_Code_For_Info.json"
        method = "POST"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_all_user(self):
        print("测试all_user接口:")
        filename = os.getcwd() + "/Authentication/All_User.json"
        method = "GET"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_User_Basic_Info(self):
        print("测试user_basic_info接口:")
        filename = os.getcwd() + "/Authentication/User_Basic_Info.json"
        method = "GET"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])

    def test_User_Detail_info(self):
        print("测试user_Detail_info接口:")
        filename = os.getcwd() + "/Authentication/User_Detail_Info.json"
        method = "GET"
        dict = pm.loadjson(filename, method)
        self.assertIsNotNone(dict)
        if dict is not None:
            self.assertEqual(200, dict['status code'])
            self.assertEqual(0, dict['result code'])
            self.assertEqual("success", dict['message'])


if __name__ == "__main__":
    unittest.main()
