import requests
import configparser
import time

import logset
import recordData
import recordJob
from datetime import datetime
# 获取日志记录器
logger = logset.setup_logging()

# 读取配置文件
config = configparser.ConfigParser()
with open('config.ini', 'r', encoding='utf-8') as config_file:
    config.read_file(config_file)

# 获取 external_host 配置
external_host = config['DEFAULT']['external_host']
province = config['DEFAULT']['province']
channel_user = config['DEFAULT']['channel_user']

def get_order():
    url = f"{external_host}/datapay/openapi/feeautomock/getOrder"
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'province': province,
        'timestmap': time.time() * 1000,
        'channel_user': channel_user
    }
    logger.info(url)
    logger.info(data)
    response = requests.post(url, headers=headers, data=data)
    logger.info(response)
    if response.status_code == 200:
        if(response.json().get('res')=='1'):
            logger.info("获取到订单")

            recordJob.jobPause()  # 一次只处理一单 。 暂停任务

            return response.json()
        else:
            logger.info("没有订单")
            return None


    else:
        logger.info(f"Error: {response.status_code}")
        return None


def push_order(order_data):
    url = f"{external_host}/datapay/openapi/feeautomock/result"
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'orderno': order_data['resdata']['orderno'],
        'timestmap': time.time() * 1000,
        'channel_user': channel_user
    }
    logger.info(url)
    logger.info(data)
    response = requests.post(url, headers=headers, data=data)
    logger.info({response})
    if response.status_code == 200:
        if(response.json().get('res')=='1'):
            logger.info("订单推送成功")
            recordJob.jobPause()  # 一次只处理一单 。 暂停任务
            order_data['pushstatus'] ='推送成功'
        else:
          logger.info("订单推送失败")
          order_data['pushstatus']='推送失败'

    else:
        logger.info(f"Error: {response.status_code}")
        order_data['pushstatus'] = '推送异常'

    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    order_data['pushtime'] = formatted_time
    recordData.addData(order_data)
    # 这里可以添加推送订单的逻辑
    logger.info(f"Pushing order: {order_data}")
    recordJob.jobRun()  # 恢复任务
    # 示例：假设有一个推送接口
    # push_url = 'http://example.com/push_order'
    # push_response = requests.post(push_url, json=order_data)
    # return push_response.json()

