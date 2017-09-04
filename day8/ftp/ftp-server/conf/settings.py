import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATABASE ={
    'engine':'file_storage',
    'name':'accounts',
    'path':"%s/db" % BASE_DIR
}


HOME_DIR = {
    'home_path':"%s/ftp-dir"%BASE_DIR
}
