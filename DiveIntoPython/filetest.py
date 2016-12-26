'''
Created on 2016/12/26

@author: nogami_kenji
'''

if __name__ == '__main__':
    proxy_url = ''
    proxy_port = ''
    proxy_user = ''
    proxy_pass = ''
    with open('test.txt', encoding='utf-8') as afile:
        txt = afile.read()
        if (len(txt.split('\n')) == 4):
            proxy_url, proxy_port, proxy_user, proxy_pass = txt.split('\n')
    
    print('proxy url = ' + proxy_url)
    print('proxy port = ' + proxy_port)
    print('proxy user = ' + proxy_user)
    print('proxy pass = ' + proxy_pass)
    
    