# -*- coding:utf-8 -*-
# LC
import os
from core import db_handler
from conf import settings
from conf import logger
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



