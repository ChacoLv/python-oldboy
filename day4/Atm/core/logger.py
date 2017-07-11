# -*- coding:utf-8 -*-
# LC
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import db_handler
from conf import settings
import  time

def logger(*args):
    pass

def trans_logger(acc_data,trans_type,amount,*args):
    '''
    实现交易功能，转账，消费，提现，还款，其中转账和消费存在收款人，则需要判断
    :return:
    '''
    trans_id = acc_data['id']
    logger_file = "%s/logs/%s"%(settings.BASE_DIR,settings.LOG_TYPES['transaction'])
    trans_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if settings.TRANSACTION_TYPE[trans_type]['receipt']:            #如果有收款人的，则将收款人信息加入日志,args传入收款人账号
        payee_id = args[0]
        log_info = "%s,%s,%s,%s,%s\n"%(trans_id,trans_type,amount,trans_time,payee_id)
    else:
        log_info = "%s,%s,%s,%s\n" % (trans_id, trans_type, amount, trans_time)
    with open(logger_file,'a') as f:
        f.write(log_info)
