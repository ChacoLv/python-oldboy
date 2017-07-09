# -*- coding:utf-8 -*-
# LC
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import db_handler
from conf import settings

def logger(*args):
    pass

def trans_logger(acc_data,trans_type,amount,trans_time,*args):
    trans_id = acc_data['id']
    logger_file = "%s/logs/%s"%(settings.BASE_DIR,settings.LOG_TYPES['transaction'])
    log_info = "%s,%s,%s,%s"%(trans_id,trans_type,amount,trans_time)
    with open("logger_file",'a') as f:
        json.dump(log_info,f)
