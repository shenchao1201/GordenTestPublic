# -*- coding:utf-8 -*-
import requests,json
import uuid
import random

from testTeamApp.apiTestPro import entry
from testTeamApp.apiTestPro.common import ts_url


def generator_datas():
    # user_data = dict()
    # value = int(input('输入随机数'))#random.randint(1, 10)
    # if value <=2:
    #     user_data['name'] = '梁珊珊'
    #     user_data['certificate_num'] = '220381198903110625'
    #     user_data['phone_num'] = '18500594890'
    #     user_data['is_verify_phone'] = 2 #0按商户配置1校验2不校验
    #     user_data['certificate_type'] = '1'
    #     user_data['bankcard_num'] = '6222620410007380137'
    #     user_data['bank_name'] = '交通银行'
    #     user_data['settle_amount'] = 1.4  # round(random.uniform(1,2),2)
    #     orderRandomCode = str(uuid.uuid4())
    #     print(f'randomCode :    {orderRandomCode}')
    #     user_data['order_random_code'] = orderRandomCode
    #     user_data['payment_way'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    #     if user_data['payment_way'] == '3':
    #         user_data['payment_account'] = ''  # input('输入支付宝账号')
    #     elif user_data['payment_way'] == '4':
    #         user_data['wx_appid'] = 'wxeb8241a5bc7e3a71'  # wxeb8241a5bc7e3a71
    #         user_data['wx_openid'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqUa11'  # o4olEvw5Z7g-rtVm3vtc6bBchwqU
    # else:
    #     user_data['name'] = '陈号俊'
    #     user_data['certificate_num'] = '130281198706293517'
    #     user_data['phone_num'] = '18612693620'#18612693629
    #     user_data['is_verify_phone'] = 1  # 0按商户配置1校验2不校验
    #     user_data['certificate_type'] = '1'
    #     user_data['bankcard_num'] = '6222020200086470768'
    #     user_data['bank_name'] = '招商银行'
    #     user_data['settle_amount'] = 1.1  # round(random.uniform(1,2),2)
    #     orderRandomCode = str(uuid.uuid4())
    #     print(f'randomCode :    {orderRandomCode}')
    #     user_data['order_random_code'] = orderRandomCode
    #     user_data['payment_way'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    #     if user_data['payment_way'] == '3':
    #         user_data['payment_account'] = ''  # input('输入支付宝账号')
    #     elif user_data['payment_way'] == '4':
    #         user_data['wx_appid'] = 'wxeb8241a5bc7e3a71'  # wxeb8241a5bc7e3a71
    #         user_data['wx_openid'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqUa11'  # o4olEvw5Z7g-rtVm3vtc6bBchwqU
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

    # user_data = dict()
    # user_data['Name'] = '梁珊珊'
    # user_data['CertificateNum'] = '220381198903110625'
    # user_data['PhoneNum'] = '18500594890'
    # user_data['CertificateType'] = '1'
    # user_data['BankCardNum'] = '6222620410007380137'
    # user_data['BankName'] = '交通银行'
    # user_data['Money'] = 50000.5#round(random.uniform(1,2),2)
    # randomCode = str(uuid.uuid4())
    # print(f'randomCode :    {randomCode}')
    # user_data['OrderRandomCode'] = randomCode
    # user_data['PayType'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    # if user_data['PayType'] == '3':
    #     user_data['PayAccount'] = ''#input('输入支付宝账号')
    # elif user_data['PayType'] == '4':
    #     user_data['WxAppid'] = 'wxeb8241a5bc7e3a71'#wxeb8241a5bc7e3a71
    #     user_data['WxOpenId'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqU'#o4olEvw5Z7g-rtVm3vtc6bBchwqU
    # # elif user_data['PayType'] == '2':
    # #     user_data['WxOpenId'] = input('输入微信openid')
    # return user_data

    #usedata
    user_data = dict()
    user_data['name'] = '梁珊珊'
    user_data['certificate_num'] = '220381198903110625'
    user_data['phone_num'] = '18500594890'
    user_data['certificate_type'] = '1'
    user_data['bankcard_num'] = '6222620410007380137'
    user_data['bank_name'] = '交通银行'
    user_data['settle_amount'] = 3.3#round(random.uniform(1,2),2)
    orderRandomCode = str(uuid.uuid4())
    print(f'randomCode :    {orderRandomCode}')
    user_data['order_random_code'] = orderRandomCode
    user_data['payment_way'] = input('输入支付渠道1银行卡2微信3支付宝4第三方微信支付')  # 1银行卡2微信3支付宝
    if user_data['payment_way'] == '3':
        user_data['payment_account'] = '18500594890'#input('输入支付宝账号')
    elif user_data['payment_way'] == '4':
        user_data['wx_appid'] = 'wxeb8241a5bc7e3a71'#wxeb8241a5bc7e3a71
        user_data['wx_openid'] = 'o4olEvw5Z7g-rtVm3vtc6bBchwqUa11'#o4olEvw5Z7g-rtVm3vtc6bBchwqU
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

# testssapi 11111
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
        'callback_url':"aHR0cHM6Ly9hcGktanMtdHMud2V0YXguY29tLmNuL2FwaS9DYWxsQmFja1Rlc3QvbG9n",#https://api-js-ts.wetax.com.cn/api/CallBackTest/log
        # 'callback_url': "aHR0cDovLzEwLjMwLjQuMTQ6MjcwMTcvYXBpL0NhbGxCYWNrVGVzdC9sb2c=",#http://10.30.4.14:27017/api/CallBackTest/log ，uat环境
        'appkey':appkey,
        'request_id':str(uuid.uuid4()),
        'timestamp':str(timestamp),
        'sign_type':'sha256',
        'signature':entry.HMACSHA256Encrypt(f'{appkey}{str(timestamp)}{apisecret}',apisecret),
        'version':'2.0',
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

def merchant_balace():
    getAmount_url = ts_url+'/api/balance/getamount'
    parameters = []
    accoutType = input('输入账户类型')
    parameters.append({
        'AccountType':accoutType
    })
    data = entry.encrypt(apisecret, json.dumps(parameters))
    print({'余额':post(getAmount_url,{'data':data} ,GenerateHeader())})

def project_amount():
    getAmount_url = ts_url+'/api/balance/getprojectamount'
    dict = {'balance_subject': 1}
    dict2 = {'balance_subject': 1, "include_project": True}
    dict3 = {'balance_subject': 2, "include_project": False}
    dict4 = {'balance_subject': 2,"include_project":False,"project_code":["XM203AC832A29944","XM203AA79106AB86"]}
    dict5 = {'balance_subject': 2, "include_project": False, "project_code": ["XM203AC832A29940", "XM203AA79106AB80"]}
    dict6 = {"include_project": False, "project_code": ["XM203AC832A29944", "XM203AA79106AB86"]}
    data = entry.encrypt(apisecret, json.dumps(dict))
    print({'项目余额':post(getAmount_url,{'data':data} ,GenerateHeader())})
    data2 = entry.encrypt(apisecret, json.dumps(dict2))
    print({'项目余额': post(getAmount_url, {'data': data2}, GenerateHeader())})
    data3 = entry.encrypt(apisecret, json.dumps(dict3))
    print({'项目余额': post(getAmount_url, {'data': data3}, GenerateHeader())})
    data4 = entry.encrypt(apisecret, json.dumps(dict4))
    print({'项目余额': post(getAmount_url, {'data': data4}, GenerateHeader())})
    data5 = entry.encrypt(apisecret, json.dumps(dict5))
    print({'项目余额': post(getAmount_url, {'data': data5}, GenerateHeader())})
    data6 = entry.encrypt(apisecret, json.dumps(dict6))
    print({'项目余额': post(getAmount_url, {'data': data6}, GenerateHeader())})

def GetbalanceByOrderCode():
    getAmount_url = ts_url+'/api/balance/getbalance'
    # status1004
    dict1 = {'order_random_code': '26632222-cfdc-4676-b504-c30abd7d260e'}
    data1 = entry.encrypt(apisecret, json.dumps(dict1))
    print(post(getAmount_url, {'data': data1}, GenerateHeader()))
    dict2 = {'settlement_code': 'JS205E73B1B30D51'}
    data2 = entry.encrypt(apisecret, json.dumps(dict2))
    print(post(getAmount_url, {'data': data2}, GenerateHeader()))

    # status1000
    dict3 = {'order_random_code': '8b717261-c585-41f0-b2d9-6dfa5b9f4049'}
    data3 = entry.encrypt(apisecret, json.dumps(dict3))
    print(post(getAmount_url, {'data': data3}, GenerateHeader()))
    dict4 = {'settlement_code': 'JS205E57F1670AFF'}
    data4 = entry.encrypt(apisecret, json.dumps(dict4))
    print(post(getAmount_url, {'data': data4}, GenerateHeader()))

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
        'phonenum': '13904083572',
        # 'name': '陈号俊',
        # 'idnumber': '130281198706293517',
        # 'phonenum': '18612693629',
        'merchantid': '5054c8cd-8050-4954-90de-8db617670d86'
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    print({'签约': post(signagreement_url, {'data': data}, GenerateHeader())})

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

    print({'签约': post(queryagreement_url, {'data': data}, GenerateHeader())})

def Createproject():
    createproject_url = ts_url+'/api/balance/createproject'
    param = {
        'projectname': '项目名称PROJECT3',
        'allowbalance': False
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    print(post(createproject_url, {'data': data}, GenerateHeader()))

def Getporjectlist():
    getprojectlist_url = ts_url+'/api/balance/getprojectlist'
    proname = input('输入项目名称')
    param = {
        'projectname': proname
    }
    data = entry.encrypt(apisecret, json.dumps(param))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

def Refundbalance():
    getprojectlist_url = ts_url+'/api/balance/refundbalance'
    list = ['JS201H718813F261']
    dict = {'settlement_code': list}

    data = entry.encrypt(apisecret, json.dumps(dict))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

def Verifycertificatenum():
    getprojectlist_url = ts_url+'/api/verify/verifycertificatenum'
    name = '邱邱' #梁珊珊
    cernum = '230125197708087320'#220381198903110625
    list = {"user_name": name, "certificate_num":cernum}
    data = entry.encrypt(apisecret, json.dumps(list))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

def Verifybankcard():
    getprojectlist_url = ts_url+'/api/verify/verifybankcard'
    name = '梁珊珊'
    cernum = '220381198903110625'
    bankcard = '6222620410007380137'
    list = {"user_name": name,"certificate_num":cernum,"bankcard_num":bankcard}
    data = entry.encrypt(apisecret, json.dumps(list))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

def Verifyiphonenum():
    getprojectlist_url = ts_url+'/api/verify/verifyiphonenum'
    name = '邱晨旭'
    cernum = '230125197708087365'
    iphonenum = '18500110022'
    list = {"user_name": name,"certificate_num":cernum,"iphone_num":iphonenum}
    data = entry.encrypt(apisecret, json.dumps(list))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

def Getelectronicreceipturl():
    getprojectlist_url = ts_url+'/api/balance/getelectronicreceipturl'
    list = ['22ed5937-4d0a-46be-ad31-26ec3a98a9a2']
    # dict = {'settlement_code': list}
    dict = {'order_random_code': list}
    data = entry.encrypt(apisecret, json.dumps(dict))
    print(data)
    print(post(getprojectlist_url, {'data': data}, GenerateHeader()))

if __name__ == '__main__':
    operate = input('请输入操作接口：1查询余额，2创建结算单,4查询结算单,5签约授权,6创建项目,7获取项目,8获取签约结果,9结算单退款,'
                    '11身份证验证,12银行卡验证，13手机号验证，14获取电子回单')
    if operate == '1':
        merchant_balace()
    # elif operate == '3':
    #     GetBalanceByOrderRandomCode()
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
        Verifycertificatenum()
    elif operate == '12':
        Verifybankcard()
    elif operate == '13':
        Verifyiphonenum()
    elif operate == '14':
        Getelectronicreceipturl()
    elif operate == '2':
        nums = 1    #商户批次账单
        urls = ts_url+"/api/Balance/CreateForBatch"
        request_list = []
        pc = 1      #结算单据数量
        code = str(uuid.uuid4())

        if nums == 1:
            if pc == 1:
                request_list.append(generator_datas())
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
