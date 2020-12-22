import uuid

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import random

# Create your views here.
from testTeamApp.apiTestPro import entry
from django.shortcuts import render,redirect
from testTeamApp.apiTestPro import interface
from testTeamApp.apiTestPro.common import ts_url
#对外api测试
def PostapiTestTs(request):
    resMsg = ""
    if request.method == 'POST':
        operate=request.POST.get('selectInfo',"0")
        paytype = request.POST.get('paytype',"0")#银企互联打款渠道
        accountType = request.POST.get('accountType', "0")#查询余额类型1、商户余额 2、抵扣券余额
        OrderRandomCode = request.POST.get('OrderRandomCode', "0")
        OrderCode = request.POST.get('OrderCode', "0")
        proname = request.POST.get('proname', "0")#项目名称




        if operate == "0":
            resMsg = "请选择需要验证的功能!"
        else:
            if operate == '2':
                if accountType == "0":
                    resMsg = "查询余额需要选择账户类型!"
                else:
                    resMsg = interface.merchant_balace(accountType)
            elif operate == '3':
                if OrderRandomCode == "0":
                    resMsg = "请输入OrderRandomCode!"
                else:
                    resMsg = interface.GetBalanceByOrderRandomCode(OrderRandomCode)
            elif operate == '4':
                if OrderCode == "0":
                    resMsg = "请输入OrderCode!"
                else:
                    resMsg = interface.GetbalanceByOrderCode(OrderCode)
            elif operate == '5':
                resMsg = interface.Signagreement()
            elif operate == '6':
                resMsg = interface.Createproject()
            elif operate == '7':
                if proname == "0":
                    resMsg = "请输入项目名称!"
                else:
                    resMsg = interface.Getporjectlist(proname)
            elif operate == '8':
                resMsg = interface.Queryagreement()
            elif operate == '9':
                resMsg = interface.Refundbalance()
            elif operate == '10':
                resMsg = interface.project_amount()
            elif operate == '11':
                resMsg = interface.Getelectronicreceipturl()
            elif operate == '1':
                if paytype == "0":
                    resMsg = "创建结算单需要选择支付类型!"
                else:
                    nums = 1  # 商户批次账单
                    urls = ts_url + "/api/Balance/CreateForBatch"
                    request_list = []
                    pc = 1  # 结算单据数量
                    code = str(uuid.uuid4())

                    if nums == 1:
                        if pc == 1:
                            request_list.append(interface.generator_datas(str(paytype)))
                            print(str(paytype))
                            result = interface.post(urls, {"data": entry.encrypt(interface.apisecret, json.dumps(request_list))}, interface.GenerateHeader())
                            print(interface.GenerateHeader())
                            print(urls)
                            print(interface.apisecret)
                            print(result)
                            resMsg = result
                        else:
                            for r in range(pc):
                                request_list.append(interface.generator_datas(str(paytype)))
                            result = interface.post(urls, {"data": entry.encrypt(interface.apisecret, json.dumps(request_list))}, interface.GenerateHeader())
                            print(result)
                            resMsg = result
                    else:
                        for r in range(nums):
                            request_list = []
                            for x in range(random.randint(1, 3)):
                                request_list.append(interface.generator_datas(str(paytype)))
                            result = interface.post(urls, {"data": entry.encrypt(interface.apisecret, json.dumps(request_list))}, interface.GenerateHeader())
                            print(result)
                            resMsg = result
            print(operate)
    return render(request, 'apiTestTs.html', {'resMsg': resMsg})


def login(request):
    # request 包含用户提交的所有信息
    error_msg = ""
    if request.method == 'POST':
    # 获取用户通过post 提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'admin' and pwd == "admin":
            #跳转到响应页面 ("/"相当于前面的地址127.1.0.0:8000)
            #error_msg = "登录成功"
            return redirect('/apiTestTs')
        else:
            #用户名密码不匹配
            error_msg = "错了 !!!!天啊!!"
            #error_msg 替换html文件 相同字段文字
    return render(request, 'login.html',{'error_msg':error_msg})
#对外Api验证首页
def apiTestTs(request):
    return render(request, 'apiTestTs.html',{})

def login_check(request):
  '''登录校验视图'''
  # 浏览器提交的信息就保存在request里面
  # request.POST保存的是POST提交的参数
  # request.GET保存的是GET提交的参数
  # 1.获取提交的用户名和密码
  username = request.POST.get('username')
  passwoed = request.POST.get('password')
  # 2.进行登录校验
  # 实际开发的时候，用户名和密码保存在数据库中
  # 模拟
  if username == 'zhangyue' and passwoed == '123456':
     # 正确,跳转到首页index
    return redirect('/index')
  else:
     # 错误
    return redirect('/login')
  # 3.返回应答










#废弃
def post(request):
      if request.method == 'POST':  # 当提交表单时
          dic = {}
          # 判断是否传参
          if request.POST:
              a = request.POST.get('a', 0)
              b = request.POST.get('b', 0)
              c = request.headers.get('abc', 0)
              print(c)
              #信息头判断
              appKey = request.headers.get('appKey', 0)
              requestId = request.headers.get('requestId', 0)
              timestamp = request.headers.get('timestamp', 0)
              sign = request.headers.get('sign', 0)

              if appKey  and requestId  and timestamp  and sign :

                  # 判断参数中是否含有a和b
                  if a and b:
                      res = add_args(a, b)
                      dic['number'] = res
                      dic = json.dumps(dic)
                      res = { "code": "0000", "msg": "成功", "data":"" }
                      return HttpResponse(json.dumps(res))
                  else:
                      return HttpResponse('输入错误')
              else:
                res = { "code": "1000", "msg": "headersERR", "data":"" }
                return HttpResponse(json.dumps(res))
          else:
              return HttpResponse('输入为空')
      else:
          return HttpResponse('方法错误')

def add_args(a, b):
    return a+b