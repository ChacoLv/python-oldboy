# -*- coding:utf-8 -*-
# LC
import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] ={'ServerAliveInterval':'45',
#                     'Compression':'yes',
#                     'CompressionLevel':'9'
#
# }
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'LC'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '80'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['USER'] = 'LC'
# with open('example.ini','w') as f:
#     config.write(f)
config.read('example.txt')
# sec = config.remove_section('bitbucket.org')
# config.write(open('example.txt','w'))

# config.add_section('XMMMMMM')
# config.write(open('example.txt','w'))
a = config.has_section('XMMMMMM')
config.set("XMMMMMM","server",'10.1.1.2')
config.write(open('example.txt','w'))