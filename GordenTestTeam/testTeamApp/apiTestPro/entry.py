# -*- coding:utf-8 -*-

import time
import hmac
import hashlib
import json
import uuid
from decimal import Decimal


from Crypto.Cipher import AES
import base64


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = bytes('ff465fdecc764337', encoding='utf-8')

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


def decrypt(key, content):
    """
    AES解密
     key,iv使用同一个
    模式cbc
    去填充pkcs7
    :param key:
    :param content:
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # base64解码
    encrypt_bytes = base64.b64decode(content)
    # 解密
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result


def generateUnixTime():
    unixTime = int(time.time())
    return unixTime


def HMACSHA256Encrypt(val, key):
    signature = hmac.new(bytes(key, encoding='utf-8'), bytes(val, encoding='utf-8'),
                         digestmod=hashlib.sha256).digest()
    HEX = signature.hex()
    return HEX


# 补足字符串长度为16的倍数
def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)  # 返回bytes


def AESEncrypt(text, key):
    aes = AES.new(str.encode(key), AES.MODE_CBC, iv=str.encode('ff465fdecc764337'))  # 初始化加密器
    ncrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    return ncrypted_text


def GenerateSignature(app_key, api_secret):
    unixTime = generateUnixTime()
    print('unixTime', unixTime)
    signature = HMACSHA256Encrypt(f"{app_key}{str(unixTime)}{api_secret}", api_secret)
    print('signature', signature)


def GenerateRequestObj(api_secret):
    Name = input('请输入姓名：')
    CertificateNum = input('请输入身份证：')
    PhoneNum = input('请输入手机号：')
    CertificateType = 1
    request_list = []
    while True:
        operate = input('是否继续生成结算信息：y继续输入，n停止输入:')
        if operate == 'y':
            BankCardNum = input('请输入银行卡号：')
            BankName = input('请输入银行名称：')
            Money = input('请输入金额：')
            request_list.append(
                {
                    'Name': Name,
                    'CertificateNum': CertificateNum,
                    'PhoneNum': PhoneNum,
                    'CertificateType': CertificateType,
                    'BankCardNum': BankCardNum,
                    'BankName': BankName,
                    'Money': Money,
                    'OrderRandomCode': str(uuid.uuid4())
                })
        else:
            request_tr = json.dumps(request_list)
            print(encrypt(api_secret,request_tr))
            break

def GenerateQuerySettle(api_secret):
    code = input('请输入结算单号：')
    print(encrypt(api_secret,code))


if __name__ == '__main__':
    app_key = input('请输入app_key:')
    api_secret = input('请输入api_secret:')
    while True:
        operate = input('请输入操作类型：1生成签名，2添加结算单，3查询结算单:')
        if operate == '1':
            GenerateSignature(app_key, api_secret)
        elif operate == '2':
            GenerateRequestObj(api_secret)
        elif operate == '3':
            GenerateQuerySettle(api_secret)
        else:
            break
