from configparser import ConfigParser


# Common tasks like reading config files and data files
def read_config(section, key):
    config = ConfigParser()
    config.read('config/config.ini')
    return config.get(section, key)
