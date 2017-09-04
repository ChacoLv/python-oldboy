import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings


def home_dir_handler(*args):
    "返回用户根目录"
    home_dir_params = settings.HOME_DIR
    username = args[0]
    home_path = "%s/%s"%(home_dir_params["home_path"],username)
    return home_path


#print(home_dir_handler("user1"))

user_home_dir = home_dir_handler("user1")  # 认证成功后，获取用户ftp家目录
#account_info["current_dir"] = user_home_dir  # 修改用户库中当前目录信息
list1 = os.listdir(user_home_dir)

