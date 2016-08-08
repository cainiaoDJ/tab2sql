#coding:utf-8
import os
import sys
import Logger
import GenerateSQL

def listdir(dirPath):
    lists=os.listdir(dirPath)
    fileNameList=[]
    for file in lists:
        #print (file)
        if os.path.isfile(dirPath+file):
            type=file.split('.',1)[1]
            #print (type)
            if type == 'tab' :
                fileNameList.append(file)
    return fileNameList

dirPath="./test/"
if __name__ == "__main__":
    logger=Logger.Logger("batchlogger",Logger.Logger.levelInfo)
    fileList=listdir(dirPath)
    genSql=GenerateSQL.GenerateSQL(dirPath)
    for file in fileList:
        logger.debug("file : " + file)
        genSql.setFileName(file)
        genSql.write()
