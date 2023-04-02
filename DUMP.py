import re,os,sys
try:
    os.mkdir('Xtractor')
    os.mkdir('/sdcard/dump')
except:
    pass
try:
    download_link = "https://github.com/tonmoy404-cyber/DUMP-X/blob/main/dump.cpython-311.so"
    if not os.path.exists("pycrypto_dump.cpython-311.so"):
        os.system("chmod 777 $HOME/dump")
        os.system(f'curl -L {download_link} > pycrypto_dump.cpython-311.so')
        import dump
        dump.buy()
    else:
        import dump
        dump.buy()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)
