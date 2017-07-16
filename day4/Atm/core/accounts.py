# -*- coding:utf-8 -*-
# LC
import json
import time
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import db_handler
from conf import settings

def load_current_balance(account_id):
    '''
    :return account balance and other basic info
    :param account_id:
    :return:
    '''
    db_path = db_handler.db_handler()
    account_file = "%s/%s.json"%(db_path,account_id)
    with open(account_file,'r') as f:
        acc_data = json.load(f)

        return acc_data

def dump_account(account_data):
    db_path = db_handler.db_handler()
    account_file = "%s/%s.json"%(db_path,account_data['id'])
    with open(account_file,"w") as f:
        json.dump(account_data,f)
    return True

