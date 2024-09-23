import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor

# 确保目录存在
os.makedirs('./蓝心羽lxy/', exist_ok=True)

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7Cu999Jt5ma6NXowqJWk6xDRSD9UQFu9oELRrK7kcxLXA%7C1720128733%7C882854b2f751d377fd0e0a643437142394902d098b65f1dc53b7b677304ce732; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e38528068cf3ed5006787595f8125d6e732a224cad0cc15268783cce28423ef9edeac9df95372bd2856ba97d6affae2a441ece6347c86bb5a9eb4f66920adb9b0774947fb4ab17fd69659bf873bcf7d25369aa8; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1440; dy_sheight=900; csrf_session_id=cb77c6272182ea232397ebeade13b721; strategyABtestKey=%221720128731.714%22; s_v_web_id=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg; xgplayer_user_id=563125062684; passport_csrf_token=1a73ccb87c124427b98ce26c3e3bef94; passport_csrf_token_default=1a73ccb87c124427b98ce26c3e3bef94; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; fpk1=U2FsdGVkX1/QDYxRXOqpHp1rfH7toucMUiGZUIu8ueEKPuppxOUrcN/vlk/TcLnqsqpIxvYZRNCDliw1lzPyuA==; fpk2=5f4591689f71924dbd1e95e47aec4ed7; xg_device_score=7.90435294117647; bd_ticket_guard_client_web_domain=2; __ac_nonce=0668714f500229d92a6e; __ac_signature=_02B4Z6wo00f016DW37AAAIDDl.Ib7ArUE9eg9tsAAI6765; SEARCH_RESULT_LIST_TYPE=%22single%22; x-web-secsdk-uid=5b8693a7-98e3-496d-b1e0-c1f2609a16af; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.558%7D; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e38528068cf3ed5006787595f8125d6e732a224cad0cc15268783cce28423ef9edeac9de04e98036d9b6fd79268e8e98df65643d9b495ed2e12e1a8853604a1dde36a83abeed548865e7f1725361ec7b7d31f28503edf8e00551f973c5a8658a057ab561b75be225a6fcded6886e2f9e7255ad7e70c80ec8c6d46fbee8f2f0ee515b6a3a81f7d974da140f5816dcc4f5e20b4096dd0c19473e5922e373473aa865eeace; biz_trace_id=fe094ac0; passport_assist_user=Cj2I_qxpThHS6PgxYFgY2qcIDD0GVgvAyaAKHGnfD174NlS5ed0hFA3_AJKmS0A4oP7CMm0Z6UNNYVyCRrSvGkoKPEQPRM9jd3MSlc6fhmi2r4Y7bsukklRWL3NRG3W_CbpOWbA33NuHFtkO4J3k8kC7qv9_3JdLVNvOTx5ZtRD15dUNGImv1lQgASIBA-rmK3Y%3D; n_mh=V2T3CBlTh1bwKAP1tMhgT9g7p30qFG0hRCZIDn_iv7E; sso_uid_tt=a550b5d7d3cecb318b754e36a9a47f94; sso_uid_tt_ss=a550b5d7d3cecb318b754e36a9a47f94; toutiao_sso_user=dd3316b690cb2592ad815a6131612bb1; toutiao_sso_user_ss=dd3316b690cb2592ad815a6131612bb1; sid_ucp_sso_v1=1.0.0-KDI5M2YxNGNhODdjMWNmYzYyZmZhN2Y1OGE1YzZmMDVkNDY5ZGViNjYKHwjKv9XHgQMQ-aqctAYY7zEgDDCBgfrbBTgGQPQHSAYaAmxmIiBkZDMzMTZiNjkwY2IyNTkyYWQ4MTVhNjEzMTYxMmJiMQ; ssid_ucp_sso_v1=1.0.0-KDI5M2YxNGNhODdjMWNmYzYyZmZhN2Y1OGE1YzZmMDVkNDY5ZGViNjYKHwjKv9XHgQMQ-aqctAYY7zEgDDCBgfrbBTgGQPQHSAYaAmxmIiBkZDMzMTZiNjkwY2IyNTkyYWQ4MTVhNjEzMTYxMmJiMQ; passport_auth_status=2a1710f49397d3ca1fcd6d37d7c892ec%2C; passport_auth_status_ss=2a1710f49397d3ca1fcd6d37d7c892ec%2C; uid_tt=6597eefc27f1df42c45263ef98ac19a6; uid_tt_ss=6597eefc27f1df42c45263ef98ac19a6; sid_tt=494dc414826126160f52a9afc75e0534; sessionid=494dc414826126160f52a9afc75e0534; sessionid_ss=494dc414826126160f52a9afc75e0534; publish_badge_show_info=%220%2C0%2C0%2C1720128878819%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=adc87c7f9e651c503cd3c54aa75df62e; __security_server_data_status=1; sid_guard=494dc414826126160f52a9afc75e0534%7C1720128894%7C5183998%7CMon%2C+02-Sep-2024+21%3A34%3A52+GMT; sid_ucp_v1=1.0.0-KGUwMmM4ODc1Mjk2MTdmMjNjYmYwNGE2YjcxNjEwODczNDUzZmJlZmMKGQjKv9XHgQMQ_qqctAYY7zEgDDgGQPQHSAQaAmhsIiA0OTRkYzQxNDgyNjEyNjE2MGY1MmE5YWZjNzVlMDUzNA; ssid_ucp_v1=1.0.0-KGUwMmM4ODc1Mjk2MTdmMjNjYmYwNGE2YjcxNjEwODczNDUzZmJlZmMKGQjKv9XHgQMQ_qqctAYY7zEgDDgGQPQHSAQaAmhsIiA0OTRkYzQxNDgyNjEyNjE2MGY1MmE5YWZjNzVlMDUzNA; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; pwa2=%220%7C0%7C1%7C0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAfKHYxpQA-p5sJFbCoXbS4O5O9wLS6jVjp6TILDFo6A8%2F1720195200000%2F0%2F1720129004110%2F0%22; odin_tt=9ea81be20743a9e88b703cc6025ac3ac784ec1d60c8633147ad4b0703598ca36b228127e4fb7444787c8da006afe27d8; download_guide=%223%2F20240705%2F0%22; WallpaperGuide=%7B%22showTime%22%3A1720129650224%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A12%2C%22cursor2%22%3A0%7D; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSXdaekxTT3VTTnJWdUpuTGtNc3NCRk91VzA4MUd2TFZwT2plY3NWQWdmSng1ZHFxNWpsUlNXVUxXRzNvaG1UUWNHWXlmdjFnTTY4elBMWVJJWUJjc2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}

urls = [
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=5F0Fp-GcX9_bQbgRbXHHVsjgpd-0E4vqv4wm3PjdYr1nmjdwx4JANnys1Crlqge2SJMUbqC4XIwNGDwjwv6WqyrlvpdKWOReBKKyhhZdt9lcX7IUMoz5HkWq6A8m-lA%3D&a_bogus=Q7mwBf8DdE2sgfSh5fVLfY3q6-a3YDiP0trEMD2f7nVipy39HMO29exLhy0vJjWjNs%2FDIb6jy4haO3rMic2bA3vX98DKl2Kh-g00t-P2so0j5ZkHejuDnUmF-vT-SaBp5vV3xcXmy7dtzuRplnAJ5k1cthMea56%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1714557664000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=5F0Fp-GcX9_bQbgRbXHHVsjgpd-0E4vqv4wm3PjdYr1nmjdwx4JANnys1Crlqge2SJMUbqC4XIwNGDwjwv6WqyrlvpdKWOReBKKyhhZdt9lcX7IUMoz5HkWq6A8m-lA%3D&a_bogus=xjWqBmwhdkITvDSh5fVLfY3q64l3YDiO0trEMD2fsdViey39HMPd9exLhysv0ymjNs%2FDIebjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PZR98bs1Xcey0grUvq-hs1tFn25kp-EKigq7lHFbYplnAy5wZvPjoja3LkFk6FOoQd&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1703412163000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=5F0Fp-GcX9_bQbgRbXHHVsjgpd-0E4vqv4wm3PjdYr1nmjdwx4JANnys1Crlqge2SJMUbqC4XIwNGDwjwv6WqyrlvpdKWOReBKKyhhZdt9lcX7IUMoz5HkWq6A8m-lA%3D&a_bogus=mXRwBdgfmEdT6fWg5fVLfY3q6U13YDiO0trEMD2fZnViCL39HMPE9exLhysv8wyjNs%2FDIebjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pg-Imcs14yeLhgrUvq-hs1tFn25kp-EKigq7lHFbYplnAy5wZvPjoja3LkFk6FOoB2&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1681552850000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=E7mqBQ06Dk2p6DSf5fVLfY3q66M3YDiO0trEMD2fYxVibg39HMOy9exLhysvQpDjNs%2FDIebjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PDRoYcs1satLhgrUvq-hs1tFn25kp-EKigq7lHFbYplnAy5wZvPjoja3LkFk6FOoB6&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1655024433000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=xXW0%2FVgfmEDBXfyf5fVLfY3q63-3YDiO0trEMD2fUnViay39HMTl9exLhysvstyjNs%2FDIebjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pk-9R7s109CLGgrUvq-hs1tFn25kp-EKigq7lHFbYplnAy5wZvPjoja3LkFk6FOosn&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1640685634000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=m7RMQmhfmD2sXfyh5fVLfY3q6RH3YDiO0trEMD2f%2FVViH639HMPU9exLhysvhXEjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PZ528S-3ine6WmnsJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG27L%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1625738848000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=x6WhMDzDmEfBXVWD5fVLfY3q6Xp3YDiO0trEMD2f%2FVVi9g39HMY09exLhysvgmEjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PZ52f7-rine6DknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2bf%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1620987100000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=OfW0MVghDkITXf6g5fVLfY3q6Ur3YDiO0trEMD2flxVin639HMTZ9exLhysvDW6jNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PZ-I8y53inCgWDrsJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2yE%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1618137235000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=O7RMMVhgDi2kvD6D5fVLfY3q66l3YDiO0trEMD2fGVVizy39HMYP9exLhysvlcLjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PZ-IRy53inCgmDrsJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2yE%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1612692018000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=xf8hQmugdkds6DSX5fVLfY3q65q3YDiO0trEMD2fMVViTL39HMPz9exLhysv-oSjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pg52mb-3iJe6R8nsJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2Hb%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1609498612000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=d6WM%2FmuDmEdTvfyD5fVLfY3q6l13YDiO0trEMD2fTnViPg39HMTQ9exLhysv48ujNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pg-o67-riJCygknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2au%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1605524463000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=YJWMQdhgdigB6Dyv5fVLfY3q6vM3YDiO0trEMD2f4nViLg39HMOH9exLhysvIpRjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pg-2f7-piJC6Dkn4Jx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2Gy%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1597490254000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=Q6WqQmgDDEgTgf6h5fVLfY3q61-3YDiO0trEMD2f7nViig39HMTI9exLhysv30WjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PgR9m7-riJtLRknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2yE%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1590488599000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=mvRhQdhhdEgPgfWv5fVLfY3q65M3YDiO0trEMD2fWVViEL39HMY99exLhysvVPWjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PgR967-riJtLgknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2ru%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1585046437000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=DfRwQmLXDiITffy65fVLfY3q6f-3YDiO0trEMD2fHVViWg39HMPt9exLhysvKZSjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Ph-oWa5NijCy8MrGJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2rg%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1580637962000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=Y780QRgvDEgNkfyg5fVLfY3q6W33YDiO0trEMD2f2VVily39HMTu9exLhysvzCLjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Ph-oRS5NijCymmrGJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2rD%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1573210854000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=OXmwBfuhDDINff6X5fVLfY3q6VP3YDiO0trEMD2fUdVi-L39HMOQ9exLhysvTEYjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PhR9Dy-rijtLfDnTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2aR%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1565154376000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=m6RwBR8hDkIi6VWg5fVLfY3q6533YDiO0trEMD2fExVi-g39HMTE9exLhysvT0jjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pd5oWGRpiHey80J4Jx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2em%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1554464850000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=xXR0%2F5g6DE2pvd6h5fVLfY3q6XP3YDiO0trEMD2ftVVi6639HMTJ9exLhysvol8jNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pd-o8e5NiHCyWBrGJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2y6%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1547989562000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=EJWZQmLDDDdTfD6k5fVLfY3q6Rr3YDiO0trEMD2fgnVi1y39HMT59exLhysvwtujNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pd-ofc5piHCyD%2Fr4Jx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2HR%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1544618767000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=Y680BdhhDk6B6DS65fVLfY3q66N3YDiO0trEMD2fLxVif639HMY69exLhysvx4gjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PdR987-riHtLWknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2rW%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1540984575000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=YvRh%2FdzvDDDPDfSg5fVLfY3q6fF3YDiO0trEMD2feVVi3y39HMYa9exLhysviaLjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-PdR967-riHtLgknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2Jj%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1537588045000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=OXWZMD8vmDdp6D6h5fVLfY3q6AZ3YDiO0trEMD2fjVVi8g39HMPm9exLhysvCgfjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pp-o87-ri9CyWknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2Sf%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg',
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAGGlljVJpNH62x8ZZIsk3BcAag0N3VxzSMe4DF1NTjLA&max_cursor=1534146587000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=200&webid=7387896494597064203&msToken=EnCdW66InSkUwH8yVgviTxY9wo6CknSdfg6fof3_MSVTgYMrN9NzYhLn8EbIJn_O_3SuiRl_gwQud3u9XaSgjR590B6agEOm77N8vTUVtQKkTvWZvJqdBDLtL1yVid4%3D&a_bogus=xXRZQQ8kDidNDDy65fVLfY3q66B3YDiO0trEMD2fRxViML39HMTJ9exLhysvtKjjNs%2FDIejjy4hSY3NMic2bA3vX98DKl2Kh-g00t-Pp-o67-ri9CygknTJx5kTlFe-M57NAiOk0y7caFuRDA9oHmhc-T6ZCcHhMHjDISpcG2t6%3D&verifyFp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg&fp=verify_ly7s8fzo_TIFvsTpX_PgpI_4Oad_9Jfy_42IWwaafAbWg'
]

for url in urls:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功
    data_list = response.json().get('aweme_list')

    # 打印描述和视频地址
    for i in data_list:
        print(i.get('desc'), i.get('video').get('play_addr').get('url_list')[0])

    # 保存视频
    for item in data_list:
        video_url = item.get('video').get('play_addr').get('url_list')[0]
        video_name = re.sub(r'[<>:"/\\|?*\n]', '', item.get('desc'))  # 清理不合法字符
        video_path = f'./蓝心羽lxy/{video_name}.mp4'

        # 下载并保存视频
        video_response = requests.get(video_url, headers=headers)
        video_response.raise_for_status()  # 检查视频请求是否成功
        with open(video_path, 'wb') as f:
            f.write(video_response.content)
        print(video_name, '下载完成!')

with ThreadPoolExecutor(max_workers=32) as executor:
    for url in urls:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        data_list = response.json().get('aweme_list')

        # 打印描述和视频地址
        for item in data_list:
            video_url = item.get('video').get('play_addr').get('url_list')[0]
            video_name = re.sub(r'[<>:"/\\|?*\n]', '', item.get('desc'))  # 清理不合法字符
            video_path = f'./蓝心羽lxy/{video_name}.mp4'

            # 下载并保存视频
            video_response = requests.get(video_url, headers=headers)
            video_response.raise_for_status()  # 检查视频请求是否成功
            with open(video_path, 'wb') as f:
                f.write(video_response.content)
            print(video_name, '下载完成!')
