# -*- coding:utf-8 -*-
# LC
from core import auth
from core import accounts
from core import logger
from core import transaction
from core.auth import login_required
import time

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def account_info(acc_data):
    print(user_data)
























