#coding:utf-8
import os
import sys
import logging
class Logger:
    logger = ""
    '''
    logger.level  级别从底到高 默认是logging.WARNING 30
        logging.NOTSET       0
        logging.DEBUG       10
        logging.INFO        20
        logging.WARNING     30
        logging.ERROR       40
        logging.CRITICAL    50
    '''
    levelAll        =  1
    levelDebug      = 10
    levelInfo       = 20
    levelWarn       = 30
    levelError      = 40
    levelCritical   = 50
    def __init__(self,LogName,level):
        self.logger=logging.getLogger(LogName)
        self.logger.setLevel(level)
        # 创建一个输出日志到控制台的StreamHandler
        hdr = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
        hdr.setFormatter(formatter)
        # 给logger添加上handler
        self.logger.addHandler(hdr)
    
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warn(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)
