# -*- coding:utf-8 -*-
# LC

import hashlib

# m = hashlib.md5()
# m.update("hello,你".encode(encoding='utf-8'))
# print(m.digest())
# print(m.hexdigest())
# m.update(b'who is you ')
# print(m.hexdigest())
# m2 = hashlib.md5()
# m2.update("hello,你who is you ".encode(encoding='utf-8'))
# print(m2.hexdigest())
#
# m3 = hashlib.sha3_224()
# m3.update(b"what is that")
# print(m3.hexdigest())

import hmac
h = hmac.new("你离得".encode(encoding='utf-8'),'加密的消息'.encode(encoding='utf-8'))  #中文需要编解码转换
h2 = hmac.new(b'it is key',b'this is message')

print(h.hexdigest())
print(h2.hexdigest())