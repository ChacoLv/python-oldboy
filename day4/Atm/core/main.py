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

def query(acc_data):
    pass
@login_required
def withdraw(acc_data):
    '''
    print current credit account information and withdraw the money
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    old_balance = account_data['balance']
    current_balance = u'''-----balance information-----
    credit : %s
    balance:%s
    '''%(account_data['credit'],old_balance)
    exit_flag = False
    while not exit_flag:
        withdraw_amount = input("Please input your withdraw amount,'b' to exit:")
        if withdraw_amount.isdigit() and int(withdraw_amount)> 0:
            withdraw_amount = float(withdraw_amount)
            new_accout_data = transaction.make_transaction(trans_logger,account_data,withdraw_amount,'withdraw')
            new_balance = new_accout_data['balance']
            interest = old_balance -new_balance - withdraw_amount
            if new_balance:
                withdraw_info = '''
                --- withdraw information ---
                withdraw amount :%s
                balance :%s
                interest :%s
                '''%(new_balance,withdraw_amount,interest)
                print(withdraw_info)
        else:
            print("Invalid withdraw account,please re-type amount!")

        if withdraw_amount == 'b':
            exit_flag = True






def transfer(acc_data):
    pass

def repay(acc_data):
    pass

def account_bill(acc_data):
    pass

def logout(acc_data):
    pass


def interactive(acc_data):
    '''
    TO SELECT WHAT TO DO
    Query the credit card info
    Withdraw the credit card money
    Transfer money to others
    Repay the credit card money
    Do shopping with using the credit card
    Manager the credit card
    '''
    menu = u'''
    -----'Bank of Oil'-----
    1. 查询
    2. 提现
    3. 转账
    4. 还款
    5. 账单
    6. 退出
    '''
    print(menu)
    menu_dict = {
        '1':query,
        '2':withdraw,
        '3':transfer,
        '4':repay,
        '5':account_bill,
        "6":logout
    }
    exit_flag = False

    while not exit_flag:
        user_select = input(">>:").strip()
        if user_select in menu_dict.keys():
            menu_dict[user_select](acc_data)
        else:
            print("Invalid input,Please retry")

def run():
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated'] == True:
        user_data['account_data'] = acc_data
        interactive(user_data)

run()


















