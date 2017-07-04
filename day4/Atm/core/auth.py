# -*- coding:utf-8 -*-
# LC
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import db_handler
from conf import settings
from core import logger
import json
import time

def login_required(func):
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated")
    return wrapper

def acc_auth(account,password):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json"%(db_path,account)
    if os.path.isfile(account_file):
        with open("account_file","r") as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_data'],"%Y-%m-%d"))
                if time.time() > exp_time_stamp:
                    print("Account %s has expired,please contact the back"%account)
                else:
                    return account_data
            else:
                print("Account ID or password is incorrect!")
    else:
        print("Account does not exit")

def acc_login(user_data,log_obj):
    '''
    account login program
    :param user_data:
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("Account ID:")
        password = input("Password:")
        auth =  acc_auth(account,password)
        if auth:    #if return is Not None，means passed the authenticated
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print("welcome %s login!"%account)
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts"%account)
        exit()





