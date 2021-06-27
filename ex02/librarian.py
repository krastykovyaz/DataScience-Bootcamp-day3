#!/usr/bin/env python
import os, sys


def main():
    try:
        if os.path.split(os.path.split(os.path.split(sys.executable)[0])[0])[1] != 'lnoisome':
            print('Invalid venv')
            sys.exit()
        with open('requirements.txt', 'w') as f:
            f.write('beautifulsoup4\npytest')
        os.system('pip install -r requirements.txt')
        os.system('pip freeze > requirements.txt')
    except:
        sys.exit()


if __name__ == '__main__':
    main()
