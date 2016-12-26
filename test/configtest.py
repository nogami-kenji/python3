'''
Created on 2016/12/26

@author: nogami_kenji
'''

import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config['default']['proxy_url'])
    print(config['default']['proxy_port'])
    print(config['default']['proxy_user'])
    print(config['default']['proxy_pass'])
    