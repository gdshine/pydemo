import configparser
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini')


class Config(object):

    def __init__(self):
        self.path = conf_dir
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path, encoding='utf-8')

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def set(self, field, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True

    def getItems(self, field):
        try:
            self.cf.items(field)
        except:
            return False
        return True


def r_config(config_file_path, field, key):
    rf = configparser.ConfigParser()
    try:
        rf.read(config_file_path, encoding='utf-8')
        if sys.platform == "win32":
            result = rf.get(field, key).replace('base_dir', str(BASE_DIR))
        else:
            result = rf.get(field, key).replace('base_dir', str(BASE_DIR))
    except:
        sys.exit(1)
    return result


def w_config(config_file_path, field, key, value):
    wf = configparser.ConfigParser()
    try:
        wf.read(config_file_path)
        wf.set(field, key, value)
        wf.write(open(config_file_path, 'w'))
    except:
        sys.exit(1)
    return True


def getkeys(config_file_path, field):
    rf = configparser.ConfigParser()
    try:
        rf.read(config_file_path, encoding='utf-8')
        if sys.platform == "win32":
            result = rf.options(field)
        else:
            result = rf.options(field)
    except:
        sys.exit(1)
    return result

if __name__ == '__main__':
    a = getkeys(conf_dir, 'browser')
    for s in a:
        print(s)
    b = r_config(conf_dir, 'remoteurl', 'url')
    print(type(a))
    print(b)