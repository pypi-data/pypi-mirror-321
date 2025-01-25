import json
from pathlib import Path

import pandas as pd
from pofile import get_files
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models

from potx.lib.CommonUtils import img2base64


def RET2excel(id, key, img_path, output_path=r'./', output_excel='RET2excel.xlsx'):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(id, key)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ocr_client.OcrClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.RecognizeGeneralInvoiceRequest()
        train_list = get_files(img_path)
        train_result = []
        for train_img in train_list:
            params = {
                "ImageBase64": img2base64(train_img)
            }
            req.from_json_string(json.dumps(params))

            # 返回的resp是一个RecognizeGeneralInvoiceResponse的实例，与请求对象对应
            resp = client.RecognizeGeneralInvoice(req)
            resp = json.loads(resp.to_json_string())
            single_ticket = resp['MixedInvoiceItems'][0]["SingleInvoiceInfos"]["ElectronicTrainTicketFull"]
            train_result.append(single_ticket)
            # 输出json格式的字符串回包
            # print(resp.to_json_string())
        print(train_result)
        # 检查输出文件名是否以.xlsx或.xls结尾，如果不是，抛出异常
        if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
            abs_output_excel = Path(output_path).absolute() / output_excel
        pd.DataFrame(train_result).to_excel(abs_output_excel)
    except TencentCloudSDKException as err:
        print(err)
