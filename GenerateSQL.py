#coding:utf-8
import os
import sys
import Logger
import shutil

class GenerateSQL:
    FileName=""
    logger = ""#logging.getLogger('debuglog')
    sqlHeader=''
    trunsql=""
    decollator="@"
    tableName=""
    SqlPath=""
    def initLogger(self):
        self.logger=Logger.Logger(__file__,Logger.Logger.levelInfo)
        
    def readFile(self):
        if os.path.isfile(self.SqlPath+self.FileName):
            f = open(self.SqlPath+self.FileName,'r',2)
        else:
            self.logger.error("Invaild File Inputed")
            exit()
        lines = f.readlines()
        return lines

    def __init__(self,path):
        self.initLogger()
        self.SqlPath=path#+"/"
        self.logger.debug("path="+self.SqlPath);
        if(os.path.isdir(self.SqlPath+"sqls")):
            self.logger.info("============= Clean the Sqls dir =============")
            shutil.rmtree(self.SqlPath+"sqls")
        os.mkdir(self.SqlPath+"sqls")
        self.logger.info("============= init end ================")

    def setFileName(self,file):
        self.logger.debug("file="+file);
        self.FileName=file
        self.logger.debug("FileName="+self.FileName);
        self.tableName=self.FileName[0:self.FileName.find(".")]
        self.sqlHeader="insert into `mydb`.`" + self.tableName+"`(\n"
        self.trunsql='truncate table `mydb`.`'+self.tableName+'`; \n'
    
    #将字符串标记（添加引号）
    def markStr(self,out):
        self.logger.debug('markstrbegin:'+out)
        lists=out.split(self.decollator)
        i=0
        for list in lists:
            if list.isdigit()==False:
                list="'"+list+"'"
            if i==0:
                result=list
            else:
                result+=','+list
            i=1
        self.logger.debug('markstrend:'+result)
        return result

    #生成table字段
    def transField(self,out):
        self.logger.debug('transField:'+out)
        lists=out.split(self.decollator)
        i=0
        for list in lists:
            list='`'+list+'`'
            if i==0:
                result=list
            else:
                result+=','+list
            i=1
        self.logger.debug('transField:'+result)
        return result

    def convert(self):
        lines=self.readFile()
        i=0
        for line in lines:
            #将制表符替换成,
            self.logger.debug('origin:'+line)
            #去除换行符和替换制表符
            out=line.replace('\t',self.decollator)
            #去除讨厌的双引号
            out=out.replace('"','')
            out=out.replace('\n','')
            if i==0:#第0行时，生成表里字段头
                out=self.transField(out)
                sqlTbl=out+') VALUES\n'
            else:
                #替换空值部分
                while out.find(',,') != -1:
                    out=out.replace(",,",",0,")
                out=self.markStr(out)
                #fix bug替换最后一列空值部分为0
                while out.find('""') != -1:
                    out=out.replace('""','0')

                self.logger.debug('LineEND:'+out)
                #拼接sql本身
                if i==1:
                    sqlBody='('+out+')\n'
                else:
                    sqlBody+=','+'('+out+')\n'
            i+=1
        sql=self.trunsql+self.sqlHeader+sqlTbl+sqlBody+';'
        return sql
        
    def write(self):
        
        sqlfile=open(self.SqlPath+"sqls/"+self.tableName+'.sql','w',encoding='utf-8')
        sql=self.convert()
        sqlfile.write(sql)
        sqlfile.close()
        self.logger.info(self.tableName + ".sql Done!")


# test = GenerateSQL("./test")
# test.setFileName("test.tab");
# test.write()
