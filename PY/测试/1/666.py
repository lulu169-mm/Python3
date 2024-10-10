# import re
# import requests
#
# cookies = {
#     'RK': 'IZO1TjzjnU',
#     'ptcz': '71b5301fdbf20d5cbaaf3d8a5606b5a9fbacec3902fab2c10eb329d84102f6b8',
#     '_t_qbtool_uid': '9bd9b6ed481e7c682a2fdd54377988cb',
#     '_ga': 'GA1.1.1747267275.1728291687',
#     '_ga_TPFW0KPXC1': 'GS1.1.1728291687.1.1.1728292480.0.0.0',
#     'fqm_pvqid': '8413a77b-e52c-4e46-993e-a2a02c5f9db1',
#     'pgv_pvid': '3566078884',
#     'fqm_sessionid': 'b0e37e74-2578-4e99-8bc0-2cf7d200adad',
#     'pgv_info': 'ssid=s2868928290',
#     '_qpsvr_localtk': '0.9950584187607385',
#     'login_type': '1',
#     'psrf_musickey_createtime': '1728448519',
#     'psrf_qqunionid': '564CF352CA5A9EDC35C013B06C600342',
#     'uin': '2493770457',
#     'psrf_qqaccess_token': '2058E1B01AE53654688A8C7ADB619408',
#     'psrf_access_token_expiresAt': '1736224519',
#     'qqmusic_key': 'Q_H_L_63k3NRymAx8Plw1ZHPDHXOQ_gE1U0HkSFEwuremcWm05pYfYPgyBRtgePnWXzUdvC1w75sMZcv1ZDdWPBK1czPkhC9Hs',
#     'psrf_qqrefresh_token': 'C30E653BC8E716816FF381585879CAAC',
#     'euin': 'owvqoiSloevk7z**',
#     'wxrefresh_token': '',
#     'tmeLoginType': '2',
#     'psrf_qqopenid': 'CB6455850097DD5AF41D9706DE4A0EF9',
#     'wxunionid': '',
#     'qm_keyst': 'Q_H_L_63k3NRymAx8Plw1ZHPDHXOQ_gE1U0HkSFEwuremcWm05pYfYPgyBRtgePnWXzUdvC1w75sMZcv1ZDdWPBK1czPkhC9Hs',
#     'wxopenid': '',
# }
#
# headers = {
#     'authority': 'ws6.stream.qqmusic.qq.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-dest': 'audio',
#     'referer': 'https://y.qq.com/',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'q-ua2': 'PR=SE&CO=WBK&QV=3&PL=WIN&PB=GE&PPVN=12.4.0.6073&COVC=049400&CHID=2100110000&RL=2880*1800&MO=SE&VE=GA&BIT=64&OS=10.0.22631',
#     'q-guid': '9bd9b6ed481e7c682a2fdd54377988cb',
#     # 'cookie': 'RK=IZO1TjzjnU; ptcz=71b5301fdbf20d5cbaaf3d8a5606b5a9fbacec3902fab2c10eb329d84102f6b8; _t_qbtool_uid=9bd9b6ed481e7c682a2fdd54377988cb; _ga=GA1.1.1747267275.1728291687; _ga_TPFW0KPXC1=GS1.1.1728291687.1.1.1728292480.0.0.0; fqm_pvqid=8413a77b-e52c-4e46-993e-a2a02c5f9db1; pgv_pvid=3566078884; fqm_sessionid=b0e37e74-2578-4e99-8bc0-2cf7d200adad; pgv_info=ssid=s2868928290; _qpsvr_localtk=0.9950584187607385; login_type=1; psrf_musickey_createtime=1728448519; psrf_qqunionid=564CF352CA5A9EDC35C013B06C600342; uin=2493770457; psrf_qqaccess_token=2058E1B01AE53654688A8C7ADB619408; psrf_access_token_expiresAt=1736224519; qqmusic_key=Q_H_L_63k3NRymAx8Plw1ZHPDHXOQ_gE1U0HkSFEwuremcWm05pYfYPgyBRtgePnWXzUdvC1w75sMZcv1ZDdWPBK1czPkhC9Hs; psrf_qqrefresh_token=C30E653BC8E716816FF381585879CAAC; euin=owvqoiSloevk7z**; wxrefresh_token=; tmeLoginType=2; psrf_qqopenid=CB6455850097DD5AF41D9706DE4A0EF9; wxunionid=; qm_keyst=Q_H_L_63k3NRymAx8Plw1ZHPDHXOQ_gE1U0HkSFEwuremcWm05pYfYPgyBRtgePnWXzUdvC1w75sMZcv1ZDdWPBK1czPkhC9Hs; wxopenid=',
#     'range': 'bytes=0-',
# }
#
# params = {
#     'guid': '6460247475',
#     'vkey': '0B95A94A226F9F632279DA997E723950DAEABB0865D590D43C5C3D617707982D1B00883BE3BFB5DC4036A4CF6F3DAF5744FC2F1D89556164',
#     'uin': '2493770457',
#     'fromtag': '120032',
#     'src': 'C400002iTFsz4Qb94P.m4a',
# }
#
# response = requests.get(
#     'https://ws6.stream.qqmusic.qq.com/C400000CRC6H12jgF8.m4a',
#     # 'https://y.qq.com/n/ryqq/toplist/4',
#     # 'https://ws6.stream.qqmusic.qq.com/C400003crGaO3GPDXh.m4a',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )
#
# with open('1.mp3', 'wb') as f:
#     f.write(response.content)

# # print(response.text)
# # 批量提取思路
# # 正则提取file":{"media_mid":"000CRC6H12jgF8",.....}里的media_mid
# # 然后拼接url
#
#
# # media_mid = re.findall(r'"media_mid":"(.*?)"', res1)
# # base_url = "https://ws6.stream.qqmusic.qq.com/"
# # for i in media_mid:
# #     print(base_url + 'C400' + i + '.m4a')
#
# # TODO:到这里获取批量url没有问题,下一步是获取 vkey ,有一个play.js,需要逆向(可以补环境)
# # requests.get(base_url+'C400'+i+'.m4a',params=params,cookies=cookies,headers=headers)
# # with open('C400'+i+'.mp3','wb') as f:
# #     f.write(response.content)



