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
from conf import settings

def make_transaction(trans_log,acc_data,amount,trans_type,**kwargs):
    '''
    Do transaction,include repay,withdraw,transfer,shopping bill,all in one
    :return: new user data
    '''
    amount = float(amount)
    if trans_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[trans_type]['interest']
        if settings.TRANSACTION_TYPE[trans_type]['action'] == 'plus':
            new_balance = acc_data['balance'] + amount +interest
        elif settings.TRANSACTION_TYPE[trans_type]['action'] == 'minus':
            new_balance = acc_data['balance'] -amount - interest
            if new_balance < 0:
                print('Your balance is not enough,current balance is %s'%acc_data['balance'])
                return
        acc_data['balance'] = new_balance
        trans_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        accounts.dump_account(acc_data)
        return acc_data
    else:
        print("The transaction type [%s] is not exit"%trans_type)


