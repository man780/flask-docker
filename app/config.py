"""Config"""
import configparser

config = configparser.ConfigParser()


def init_config(path):
    """Config init"""
    config.optionxform = str
    config.read(path)
