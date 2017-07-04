# -*- coding:utf-8 -*-
# LC
import os
import time
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import auth
from core import accounts
from core import logger
from core import transaction
from core.auth import login_required

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def account_info(acc_data):
    print(user_data)

def interactive(acc_data):
    pass



def run():
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated'] == True:
        user_data['account_data'] = acc_data
        interactive(user_data)

run()


















