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

def print_trans_info(trans_type,balance,amount,interest):
    #打印交易信息
    transaction_info = '''
    --- %s information ---
    balance :%s
    %s amount :%s
    interest :%s
    ''' % (trans_type,balance,trans_type,amount, interest)
    print(transaction_info)

def print_balance_info(acc_data):
    #打印账号余额信息
    account_data = accounts.load_current_balance(acc_data['account_id'])
    balance = account_data['balance']
    current_balance = u'''-----balance information-----
    credit : %s
    balance:%s
    '''%(account_data['credit'],balance)

@login_required
def query(acc_data):
    #实现自定义时间范围查询交易记录功能
    account_data = accounts.load_current_balance(acc_data['account_id'])
    account_id = account_data['id']
    balance = account_data['balance']
    credit = account_data['credit']
    expired_date = account_data['expire_date']
    acc_info = '''
    -----Account information-----
    Card ID:%s
    Credit:%s
    Balance:%s
    Expired Date:%s
    '''%(account_id,credit,balance,expired_date)
    print(acc_info)
    start_date = input("Please input querying start date(%Y-%m-%d):")
    start_date_timestamp = time.mktime(time.strptime("%s 0:0:0"%start_date,"%Y-%m-%d %H:%M:%S"))
    end_date = input("Please input querying end date(%Y-%m-%sd):")
    end_date_timestamp = time.mktime(time.strptime("%s 23:59:59"%end_date,"%Y-%m-%d %H:%M:%S"))
    trans_log = logger.load_log("transactions",acc_data)    #交易记录提取
    print('''
    -----transaction information-----
    strat date:%s
    end date:%s
    '''%(start_date,end_date))
    print("\t%-10s%-15s%-10s%-12s%-22s%-10s"%
          ("ID","Type","Amount","Interest","Date","Payee"))
    for line in trans_log:
        line_list = line.split(",")
        trans_log_timestamp = time.mktime(time.strptime(line_list[4],"%Y-%m-%d %H:%M:%S"))
        if start_date_timestamp <= trans_log_timestamp<= end_date_timestamp:
            if len(line_list) == 5:
                print("\t%-10s%-15s%-10s%-12s%-22s"%
                      (line_list[0],line_list[1],line_list[2],line_list[3],line_list[4]))
            else:
                print("\t%-10s%-15s%-10s%-12s%-22s%-10s" %
                      (line_list[0], line_list[1], line_list[2], line_list[3], line_list[4],line_list[5]))


@login_required
def withdraw(acc_data):
    '''
    print current credit account information and withdraw the money
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    old_balance = account_data['balance']
    print_balance_info(acc_data)
    exit_flag = False
    while not exit_flag:
        withdraw_amount = input("Please input your withdraw amount,'b' to exit:")
        if withdraw_amount.isdigit() and int(withdraw_amount)> 0:
            withdraw_amount = float(withdraw_amount)
            new_account_data = transaction.make_transaction(account_data,withdraw_amount,'withdraw')
            new_balance = new_account_data['balance']
            interest = old_balance -new_balance - withdraw_amount
            interest = round(interest,2)
            logger.trans_logger(account_data, 'withdraw', withdraw_amount,interest)
            old_balance = new_balance
            if new_balance:
                print_trans_info('withdraw', new_balance, withdraw_amount, interest)
        else:
            print("Invalid withdraw account,please re-type amount!")

        if withdraw_amount == 'b':
            exit_flag = True

@login_required
def transfer(acc_data):
    '''
    transfer money to others,and log the information in transaction log
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    old_balance = account_data['balance']
    print_balance_info(acc_data)
    exit_flag = False
    while not exit_flag:
        payee_id = input("Please input payee account id,'b to exit':")
        if payee_id == 'b':
            exit_flag = True
            continue
        else:
            re_payee_id = input("Please input payee account id again:")
            if payee_id == re_payee_id:
                payee_data = accounts.load_current_balance(payee_id)
                trans_amount = input("Please input transfer amount:")
                trans_amount = float(trans_amount)
                new_account_data = transaction.make_transaction(account_data,trans_amount, 'transfer')
                new_balance = new_account_data['balance']
                interest = old_balance - new_balance - trans_amount
                interest = round(interest,2)
                old_balance = new_balance
                logger.trans_logger(account_data, 'transfer', trans_amount,interest,payee_id)
                new_payee_data = transaction.make_transaction(payee_data,trans_amount, 'repay')         #收款人按着还款处理，即账号加钱
                logger.trans_logger(payee_data, 'repay', trans_amount,0)

                if new_balance:
                    print_trans_info('transfer',new_balance,trans_amount,interest)
            else:
                print("payee_id is invalid,retry!!!")

@login_required
def repay(acc_data):
    #还款，实现还款功能
    account_data = accounts.load_current_balance(acc_data['account_id'])
    old_balance = account_data['balance']
    print_balance_info(acc_data)
    exit_flag = False
    while not exit_flag:
        repay_amount = input("Please input your repay amount,'b' to exit:")
        if repay_amount.isdigit() and int(repay_amount) > 0:
            new_account_data = transaction.make_transaction(account_data,repay_amount,'repay')
            new_balance = new_account_data['balance']
            repay_amount = float(repay_amount)
            interest = new_balance - old_balance - repay_amount
            logger.trans_logger(account_data, 'repay',repay_amount,0)
            if new_balance:
                print_trans_info('repay',new_balance,repay_amount)
        elif repay_amount == 'b':
            exit_flag = True

@login_required
def account_bill(acc_data):
    #查看账号所有交易记录信息
    account_data = accounts.load_current_balance(acc_data['account_id'])
    trans_log = logger.load_log('transactions',acc_data)
    total_payout = 0
    total_payin = 0
    interest = 0
    print('-----transaction information-----')
    for line in trans_log:
        print(line)
        line = line.split(",")
        if line[1] != 'repay':
            total_payout += float(line[2])
        else:
            total_payin += float(line[0])
        interest += float(line[3])                                             #计算总的支出利息
    print("\n-----Total information-----")
    print("total_payout:%s"%total_payout)
    print("total_interest:%s"%interest)
    print("total_payin:%s"%total_payin)




def logout(acc_data):
    return True


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
        print(menu)
        user_select = input(">>:").strip()
        if user_select in menu_dict.keys():
            res = menu_dict[user_select](acc_data)
            if res == True:
                break
        else:
            print("Invalid input,Please retry")


def run():
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated'] == True:
        user_data['account_data'] = acc_data
        interactive(user_data)

run()


















