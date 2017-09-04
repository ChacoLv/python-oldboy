import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings

def db_handler():
    '''连接数据库'''
    conn_params = settings.DATABASE
    if conn_params["engine"] == 'file_storage':
        return file_db_handler(conn_params)
    elif conn_params["engine"] == 'mysql':
        pass

def file_db_handler(conn_params):
    db_path = "%s/%s"%(conn_params["path"],"accounts")
    return db_path
