# -*- coding:utf-8 -*-
# LC
import json,time,os
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params:
    :return:
    '''
    print("file db:",conn_params)
    db_path = "%s/%s"%(conn_params["path"],conn_params['name'])
    return file_execute

def db_handler():
    '''
    connect to db
    :return:
    '''
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['egine'] == 'mysql':
        pass

def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s'%(conn_params['path'],conn_params['name'])

    sql_list = sql.split('where')
    if sql_list[0].startswith("select") and len(sql_list) > 1:
        column,val = sql_list[1].strip().split("=")
        if column == "account":
            account_file = "%s/%s.json"%(db_path,val)
            if os.path.isfile(account_file):
                with open(account_file,'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("Account does not exit!")
    elif sql_list[0].startwith("update") and len(sql_list) > 1:
        column,val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json"%(db_path,val)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file,"w") as f:
                    acc_data = json.dump(account_data,f)
                return True




