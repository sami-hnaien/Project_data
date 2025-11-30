import configparser
import os
import sys

sys.path.append("../")


class Config:
    def __init__(self, conf_file):
        self.config = configparser.RawConfigParser()  # python object to parse config
        self.config.read(conf_file)

    def getParam(self, section, param):
        return self.config.get(section, param)
