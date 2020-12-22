# -*- coding:utf-8 -*-
import requests
import json
import uuid
import random
import string

from testTeamApp.apiTestPro import entry
from testTeamApp.apiTestPro.common import ts_url


def generator_datas(paytype):
    # user_data = dict()
    # value = int(input("输入随机数"))#random.randint(1, 4)
    # if value <=2:
    #     user_data['Name'] = '梁珊珊'
    #     user_data['CertificateNum'] = '220381198903110625'
    #     user_data['PhoneNum'] = '18500594890'
    #     user_data['IsVerifyPhone'] = 2 #0按商户配置1校验2不校验
    #     user_data['CertificateType'] = '1'
    #     user_data['BankCardNum'] = '6222620410007380137'
    #     user_data['BankName'] = '交通银行'
    #     user_data['Money'] = 1.6  # round(random.uniform(1,2),2)
    #     randomCode = str(uuid.uuid4())
    #     print(f'randomCode :    {randomCode}')
    #     user_data['OrderRandomCode'] = randomCode
    #     user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    #     if user_data['PayType'] == '3':
    #         user_data['PayAccount'] = '18500594890'  # input('输入支付宝账号')
    #     elif user_data['PayType'] == '4':
    #         user_data['WxAppid'] = 'wxeb8241a5bc7e3a71'  # wxeb8241a5bc7e3a71
    #         user_data['WxOpenId'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqU'  # o4olEvw5Z7g-rtVm3vtc6bBchwqU
    # else:
    #     user_data['Name'] = '陈号俊'
    #     user_data['CertificateNum'] = '13028119870629351'#'130281198706293517'
    #     user_data['PhoneNum'] = '18612693620'#18612693629
    #     user_data['IsVerifyPhone'] = 2
    #     user_data['CertificateType'] = '1'
    #     user_data['BankCardNum'] = '6222020200086470768'
    #     user_data['BankName'] = '招商银行立水桥支行'
    #     user_data['Money'] = 1.3 #round(random.uniform(1, 2), 1)
    #     user_data['OrderRandomCode'] = str(uuid.uuid4())
    #     randomCode = str(uuid.uuid4())
    #     print(f'randomCode :    {randomCode}')
    #     user_data['OrderRandomCode'] = randomCode
    #     user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  # 1银行卡2微信3支付宝
    #     if user_data['PayType'] == '3':
    #         user_data['PayAccount'] = input('输入支付宝账号')
    #     elif user_data['PayType'] == '4':
    #         user_data['WxAppid'] = 'wxeb8241a5bc7e3a71'  # wxeb8241a5bc7e3a71
    #         user_data['WxOpenId'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqU'  # o4olEvw5Z7g-rtVm3vtc6bBchwqU
    # return user_data
    #
    # request_list.append(generator_datas())

    # user_data = dict()
    # user_data['Name'] = '陈号俊'
    # user_data['CertificateNum'] = '130281198706293517'
    # user_data['PhoneNum'] = '18612693629'
    # user_data['CertificateType'] = '1'
    # user_data['BankCardNum'] = '6222020200086470768'
    # user_data['BankName'] = '招商银行立水桥支行'
    # user_data['Money'] = 1.18 #round(random.uniform(1, 2), 1)
    # user_data['OrderRandomCode'] = str(uuid.uuid4())
    # randomCode = str(uuid.uuid4())
    # print(f'randomCode :    {randomCode}')
    # user_data['OrderRandomCode'] = randomCode
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  # 1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = input('输入支付宝账号')
    # # elif user_data['PayType'] == '2':
    #     # user_data['WxOpenId'] = input('输入微信openid')
    # return user_data

    # # usedata
    user_data = dict()
    user_data['Name'] = '沈超'
    user_data['CertificateNum'] = '110223198812017877'
    user_data['PhoneNum'] = '15810162994'
    user_data['IsVerifyPhone'] = 2
    user_data['CertificateType'] = '1'
    user_data['BankCardNum'] = '6222620910010348757'
    user_data['BankName'] = '交通银行'
    user_data['Money'] = 1.3#round(random.uniform(1,2),2)
    randomCode = str(uuid.uuid4())
    print(f'randomCode :    {randomCode}')
    user_data['OrderRandomCode'] = randomCode
    #user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    user_data['PayType'] = str(paytype)  # 1银行卡2微信3支付宝
    if user_data['PayType'] == '3':
        user_data['PayAccount'] = '15810162994'#input('输入支付宝账号')
    elif user_data['PayType'] == '4':
        user_data['WxAppid'] = 'wxeb8241a5bc7e3a71'#wxeb8241a5bc7e3a71
        user_data['WxOpenId'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqU'#o4olEvw5Z7g-rtVm3vtc6bBchwqU
    # elif user_data['PayType'] == '2':
    #     user_data['WxOpenId'] = input('输入微信openid')
    return user_data


    # user_data = dict()
    # user_data['Name'] = ' ·星·霖霖 · '#王雅阁
    # user_data['CertificateNum'] = 'aA0123456789'
    # user_data['PhoneNum'] = '18500594890'
    # user_data['CertificateType'] = '3'
    # user_data['BankCardNum'] = '6214831007454132'
    # user_data['BankName'] = '招商银行'
    # user_data['Money'] = 1.3  # round(random.uniform(100,10000),2)
    # randomCode = str(uuid.uuid4())
    # print(f'randomCode :    {randomCode}')
    # user_data['OrderRandomCode'] = randomCode
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  # 1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = input('输入支付宝账号')
    # # elif user_data['PayType'] == '2':
    # #     user_data['WxOpenId'] = input('输入微信openid')
    # return user_data

    # user_data = dict()
    # user_data['Name'] = '王艺颖'
    # user_data['CertificateNum'] = '120105198909084527'
    # user_data['PhoneNum'] = '17610899890'
    # user_data['CertificateType'] = '1'
    # user_data['BankCardNum'] = '6214831222354281'
    # user_data['BankName'] = '招商银行'
    # user_data['Money'] = 1.2 #round(random.uniform(1,2),1)
    # user_data['OrderRandomCode'] = str(uuid.uuid4())
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  #1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = input('输入支付宝账号')
    # # elif user_data['PayType'] == '2':
    # #     user_data['WxOpenId'] = input('输入微信openid')
    # return user_data

    # user_data = dict()
    # user_data['Name'] = '尉龙'
    # user_data['CertificateNum'] = '230828198901117417'
    # user_data['PhoneNum'] = '18501353599'
    # user_data['CertificateType'] = '1'
    # user_data['BankCardNum'] = '6216690100002712411'
    # user_data['BankName'] = '中国银行'
    # user_data['Money'] = 8.4
    # user_data['OrderRandomCode'] = str(uuid.uuid4())
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  #1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = input('输入支付宝账号')
    # # elif user_data['PayType'] == '2':
    # #     user_data['WxOpenId'] = input('输入微信openid')
    # return user_data

    # user_data = dict()
    # user_data['Name'] = '韩霞'
    # user_data['CertificateNum'] = '63212219840104002X'
    # user_data['PhoneNum'] = '13671325743'
    # user_data['CertificateType'] = '1'
    # user_data['BankCardNum'] = '6225880112695698'
    # user_data['BankName'] = '招商银行'
    # user_data['Money'] = 15 #round(random.uniform(1, 2), 1)
    # user_data['OrderRandomCode'] = str(uuid.uuid4())
    # randomCode = str(uuid.uuid4())
    # print(f'randomCode :    {randomCode}')
    # user_data['OrderRandomCode'] = randomCode
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝')  # 1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = input('输入支付宝账号')
    # # elif user_data['PayType'] == '2':
    #     # user_data['WxOpenId'] = input('输入微信openid')
    # return user_data


# appkey = "aa27f964-2b19-4d12-8653-3cbb405d3f90".replace('-','')
# apisecret = "4cc78f9b606944599217bf811a375ed8" #CCtestss40

# testss61
# appkey = "c58b4c55-0b56-426b-b247-1fea1359ef80".replace('-','')
# apisecret = "9f9ee2231fb447589d9d138a3db11300"

appkey = "7195c07d-2219-42ce-ac0a-b5f14f888ce1".replace('-','')
apisecret = "e91a9a4ddde24532a2995f63e8c58ee7" #CC_testssyq01

# appkey = "50099a55-97f8-42fd-a1c6-e099f657f7bc".replace('-','')
# apisecret = "2e68a7c220ef4003a3add3845bc3d5b9" #CCtestss41offlinesign

# appkey = "7af591be-72e4-4959-a9f8-d758bb2e3cb0".replace('-','')
# apisecret = "6c3c85aa6e444afa8307788ccb35dde6" #CCyq_testss02

# appkey = "7fb006a7-eda5-4b5a-bb62-62a085eee2f1".replace('-','')
# apisecret = "50c5c992f612460e8b14b41148895fdb" #testsss01

# appkey = "cadc7b03-31c4-4734-9b3a-0b501f6a5f21".replace('-','')
# apisecret = "1ebcce61c9b844508e10da511f8eaa02" #CCtestss56apisign

# testssapi 11111、APISStest
# appkey = "e6fbff0cb3af4490bb1af131ace1e5f4"
# apisecret = "66b2b14c719245928aeaadc5ba6fef56"

# CCyq_testss02
# appkey = "7af591be-72e4-4959-a9f8-d758bb2e3cb0".replace('-','')
# apisecret = "6c3c85aa6e444afa8307788ccb35dde6"

# CCtestss55
# appkey = "ba48851f-c176-410c-94f5-fd8cd80611ea".replace('-','')
# apisecret = "bbcbdb78d01b458287e3f5cb01953c26"

# testss38
# appkey = "5054c8cd-8050-4954-90de-8db617670d86".replace('-','')
# apisecret = "47bda1c0bd204dee993804603eeef4ce"

# 乐卡
# appkey = "9678aa77-20d8-462c-b598-29967e6da2dc".replace('-','')
# apisecret = "7d86d1e5c972431d8a3c9dab54535301"

# 兜趣
# appkey = "f4e0f8ef-a47e-4cad-a3b4-3b7c91155aa7".replace('-','')
# apisecret = "f4ba742df9a642efa837c8ed7f96cfd0"

def GenerateHeader():
    timestamp = entry.generateUnixTime()
    return {
        'accept': "text/plain",
        'Content-Type': "application/json",
        # 'callback_url': "aHR0cHM6Ly90ZW5jZW50LmdpdGh1Yi5pby93ZXB5L2RvY3VtZW50Lmh0bWwjLw==",
        'callback_url':"aHR0cHM6Ly9hcGktanMtdHMud2V0YXguY29tLmNuL2FwaS9DYWxsQmFja1Rlc3QvbG9n",#https://api-js-ts.wetax.com.cn/api/CallBackTest/log
        # 'callback_url': "aHR0cDovLzEwLjMwLjQuMTQ6MjcwMTcvYXBpL0NhbGxCYWNrVGVzdC9sb2c=",#http://10.30.4.14:27017/api/CallBackTest/log ，uat环境
        'appkey':appkey,
        'request_id':str(uuid.uuid4()),
        'timestamp':str(timestamp),
        'sign_type':'sha256',
        'signature':entry.HMACSHA256Encrypt(f'{appkey}{str(timestamp)}{apisecret}',apisecret),
        'version':'1.0',
        'project_code':'XM201EAA283C05CF',#testssyq01
         'batch_return':''
    }

def post(urls ,parameters,headers):
    response = None
    try:
        response = requests.post(urls ,data=json.dumps(parameters) ,headers=headers)
        result = json.loads(response.text)
        return result
    except Exception as ex:
        print(ex)

def merchant_login(self, username, password, remember_login="false", return_url=""):
    api_name = '/api/User/Login'
    parameters = dict()
    parameters['username'] = username
    parameters['password'] = password
    parameters['rememberLogin'] = remember_login
    parameters['returnUrl'] = return_url
    return post(api_name, parameters)['data']

def merchant_balace(accountType):
    getAmount_url = ts_url+'/api/balance/getamount'
    parameters = []
    #accoutType = input('输入账户类型')
    accoutType = accountType#新增
    parameters.append({
        'AccountType':accoutType
    })
    data = entry.encrypt(apisecret, json.dumps(parameters))
    res = {'余额':post(getAmount_url,{'data':data} ,GenerateHeader())}
    return res


def project_amount():
    getAmount_url = ts_url+'/api/balance/getprojectamount'
    dict = {'balance_subject': 1}
    dict2 = {'balance_subject': 1, "include_project": True}
    dict3 = {'balance_subject': 2, "include_project": False}
    dict4 = {'balance_subject': 2,"include_project":False,"project_code":["XM203AC832A29944","XM203AA79106AB86"]}
    dict5 = {'balance_subject': 2, "include_project": False, "project_code": ["XM203AC832A29940", "XM203AA79106AB80"]}
    dict6 = {"include_project": False, "project_code": ["XM203AC832A29944", "XM203AA79106AB86"]}
    res = {}
    data = entry.encrypt(apisecret, json.dumps(dict))
    #print({'项目余额':post(getAmount_url,{'data':data} ,GenerateHeader())})
    res1 = {'Project balance':post(getAmount_url,{'data':data} ,GenerateHeader())}
    data2 = entry.encrypt(apisecret, json.dumps(dict2))
    #print({'项目余额': post(getAmount_url, {'data': data2}, GenerateHeader())})
    res2 = {'Project balance': post(getAmount_url, {'data': data2}, GenerateHeader())}
    data3 = entry.encrypt(apisecret, json.dumps(dict3))
    #print({'项目余额': post(getAmount_url, {'data': data3}, GenerateHeader())})
    res3 = {'Project balance': post(getAmount_url, {'data': data3}, GenerateHeader())}
    data4 = entry.encrypt(apisecret, json.dumps(dict4))
    #print({'项目余额': post(getAmount_url, {'data': data4}, GenerateHeader())})
    res4 = {'Project balance': post(getAmount_url, {'data': data4}, GenerateHeader())}
    data5 = entry.encrypt(apisecret, json.dumps(dict5))
    #print({'项目余额': post(getAmount_url, {'data': data5}, GenerateHeader())})
    res5 = {'Project balance': post(getAmount_url, {'data': data5}, GenerateHeader())}
    data6 = entry.encrypt(apisecret, json.dumps(dict6))
    #print({'项目余额': post(getAmount_url, {'data': data6}, GenerateHeader())})
    res6 = {'Project balance': post(getAmount_url, {'data': data6}, GenerateHeader())}
    res = str(json.dumps(res1))+str(json.dumps(res2))+str(json.dumps(res3))+str(json.dumps(res4))+str(json.dumps(res5))+str(json.dumps(res6))
    #res.update(res2)
    return res

def GetbalanceByOrderCode(OrderCode):
    getAmount_url = ts_url+'/api/balance/getbalance'
    #OrderCode = input('输入OrderCode')
    OrderCode = OrderCode
    data = entry.encrypt(apisecret, OrderCode)
    #print(post(getAmount_url, {'data': data}, GenerateHeader()))
    res = post(getAmount_url, {'data': data}, GenerateHeader())
    return res

def GetBalanceByOrderRandomCode(OrderRandomCode):
    getAmount_url = ts_url+'/api/balance/GetBalanceByOrderRandomCode'
    #OrderRandomCode = input('输入账户OrderRandomCode')
    OrderRandomCode = OrderRandomCode
    data = entry.encrypt(apisecret, OrderRandomCode)
    #print(post(getAmount_url, {'data': data}, GenerateHeader()))
    res = post(getAmount_url, {'data': data}, GenerateHeader())
    return res


#打开签约API开关
def Signagreement():
    signagreement_url = ts_url+'/api/balance/signagreement'
    parameters =[]
    parameters.append({
        'name': '梁珊珊',
        'idnumber': '220381198903110625',
        'phonenum': '13904083572',
        'merchantid': 'cadc7b03-31c4-4734-9b3a-0b501f6a5f21'
    })
    param = {
        'name': '梁珊珊',
        'idnumber': '220381198903110625',
        'phonenum': '18500594890',
        # 'name': '陈号俊',
        # 'idnumber': '130281198706293517',
        # 'phonenum': '18612693629',
        'merchantid': '5054c8cd-8050-4954-90de-8db617670d86'
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    #print({'签约': post(signagreement_url, {'data': data}, GenerateHeader())})
    res = {'签约': post(signagreement_url, {'data': data}, GenerateHeader())}
    return res

# 签约pdf10分钟有效.获取签约结果
def Queryagreement():
    queryagreement_url = ts_url+'/api/balance/QueryAgreement'
    param = {
        'name': '梁珊珊',
        'idnumber': '220381198903110625'
        # 'name': '陈号俊',
        # 'idnumber': '130281198706293517'
    }
    data = entry.encrypt(apisecret, json.dumps(param))

    #print({'签约': post(queryagreement_url, {'data': data}, GenerateHeader())})
    res = {'签约': post(queryagreement_url, {'data': data}, GenerateHeader())}
    return res

def Createproject():
    createproject_url = ts_url+'/api/balance/createproject'
    param = {
        'projectname': '项目名称PROJECT3',
        'allowbalance': False
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    #print(post(createproject_url, {'data': data}, GenerateHeader()))
    res = post(createproject_url, {'data': data}, GenerateHeader())
    return res

def Getporjectlist(proname):
    getprojectlist_url = ts_url+'/api/balance/getprojectlist'
    #proname = input('输入项目名称')
    proname = proname
    param = {
        'projectname': proname
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    print(data)
    #print(post(getprojectlist_url, {'data': data}, GenerateHeader()))
    res = post(getprojectlist_url, {'data': data}, GenerateHeader())
    return res

def Refundbalance():
    getprojectlist_url = ts_url+'/api/balance/refundbalance'
    # list = ['22ed5937-4d0a-46be-ad31-26ec3a98a9a2']
    list = ['d5123675-1f58-4ce3-ba89-5b6514e26e57']
    # dict = {'settlement_code': list}
    dict = {'random_code':list}
    data = entry.encrypt(apisecret, json.dumps(dict))
    print(data)
    #print(post(getprojectlist_url, {'data': data}, GenerateHeader()))
    res = post(getprojectlist_url, {'data': data}, GenerateHeader())
    return res

#根据结算单流水号或者结算单随机号获取电子回单图片地址.请在结算单到1000状态后调接口获取回单（一般为10分钟左右）
def Getelectronicreceipturl():
    getprojectlist_url = ts_url+'/api/balance/getelectronicreceipturl'
    list = ['22ed5937-4d0a-46be-ad31-26ec3a98a9a2']
    # dict = {'settlement_code': list}
    dict = {'random_code': list}
    data = entry.encrypt(apisecret, json.dumps(dict))
    print(data)
    #print(post(getprojectlist_url, {'data': data}, GenerateHeader()))
    res = post(getprojectlist_url, {'data': data}, GenerateHeader())
    return res

def CreateForBatch(paytype):
    nums = 1  # 商户批次账单
    urls = ts_url + "/api/Balance/CreateForBatch"
    request_list = []
    pc = 1  # 结算单据数量
    code = str(uuid.uuid4())

    if nums == 1:
        if pc == 1:
            request_list.append(generator_datas(paytype))
            result = post(urls, {"data": entry.encrypt(apisecret, json.dumps(request_list))}, GenerateHeader())
            print(result)
            return str(result.text)
        else:
            for r in range(pc):
                request_list.append(generator_datas(paytype))
            result = post(urls, {"data": entry.encrypt(apisecret, json.dumps(request_list))}, GenerateHeader())
            print(result)
            return str(result.text)
    else:
        for r in range(nums):
            request_list = []
            for x in range(random.randint(1, 3)):
                request_list.append(generator_datas(paytype))
            result = post(urls, {"data": entry.encrypt(apisecret, json.dumps(request_list))}, GenerateHeader())
            print(result)
            return str(result.text)


if __name__ == '__main__':
    operate = input('请输入操作接口：1查询余额，2创建结算单，3根据OrderRandomCode查询结算单,4根据OrderCode查询结算单,'
                    '5签约授权,6创建项目,7获取项目,8获取签约结果,9结算单退款10获取项目余额,11获取电子回单')
    if operate == '1':
        merchant_balace()
    elif operate == '3':
        GetBalanceByOrderRandomCode()
    elif operate == '4':
        GetbalanceByOrderCode()
    elif operate == '5':
        Signagreement()
    elif operate == '6':
        Createproject()
    elif operate == '7':
        Getporjectlist()
    elif operate == '8':
        Queryagreement()
    elif operate == '9':
        Refundbalance()
    elif operate == '10':
        project_amount()
    elif operate == '11':
        Getelectronicreceipturl()
    elif operate == '2':
        nums = 1    #商户批次账单
        urls = ts_url+"/api/Balance/CreateForBatch"
        request_list = []
        pc = 1     #结算单据数量
        code = str(uuid.uuid4())

        if nums == 1:
            if pc == 1:
                request_list.append(generator_datas("1"))
                result = post(urls, {"data": entry.encrypt(apisecret, json.dumps(request_list))}, GenerateHeader())
                print(result)
            else:
                for r in range(pc):
                    request_list.append(generator_datas())
                result = post(urls, {"data": entry.encrypt(apisecret, json.dumps(request_list))}, GenerateHeader())
                print(result)
        else:
            for r in range(nums):
                request_list = []
                for x in range(random.randint(1,3)):
                    request_list.append(generator_datas())
                result = post(urls,{"data":entry.encrypt(apisecret,json.dumps(request_list))},GenerateHeader())
                print(result)
