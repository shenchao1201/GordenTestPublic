# -*- coding:utf-8 -*-
def merchant_login(self, username, password, remember_login="false", return_url=""):
    api_name = '/api/User/Login'
    parameters = dict()
    parameters['username'] = username
    parameters['password'] = password
    parameters['rememberLogin'] = remember_login
    parameters['returnUrl'] = return_url
    return self.__post(api_name, parameters)['data']