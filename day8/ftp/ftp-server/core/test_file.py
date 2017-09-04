import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(sys.path)
sys.path.append(BASE_DIR)


print(BASE_DIR)
print(sys.path)