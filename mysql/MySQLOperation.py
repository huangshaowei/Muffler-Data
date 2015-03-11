import MySQLdb
from ..tools import *
from PyQt4 import QtGui

conn = None 
def get_ConnValue():
    global conn
    return conn

def set_ConnValue(data):
    global conn 
    conn = data

def mysql_exec_res(sqlquery):
   try:
       global conn
       cur = conn.cursor()
       cur.execute(sqlquery)
       res = cur.fetchone()
   except Exception,e:
       QtGui.QMessageBox.about(None,"about mysql execute",str(e))
       del cur
   return res

def mysql_exec_res_all(sqlquery):
   try:
       global conn
       cur = conn.cursor()
       cur.execute(sqlquery)
       res = cur.fetchall()
   except Exception,e:
       QtGui.QMessageBox.about(None,"about mysql execute",str(e))
       del cur
   return res

def mysql_exec(sqlquery):
   try:
       global conn
       cur = conn.cursor()
       cur.execute(sqlquery)
       conn.commit()
       return True
   except Exception,e:
       QtGui.QMessageBox.about(None,"about mysql execute",str(e))
       del cur
       return False


def find(model,index):
   check_type(int,index)
   sqlquery = "select * from " + model.attr['name'] + "where id = " + str(index)
   return mysql_exec_res(sqlquery)

def createprocedure():
    sqlquery = "CREATE procedure getAllRecordWithOneField(IN p_in_field varchar(64),IN p_in_table varchar(64)) \
    begin \
    set @sqlcmd = concat('select `',p_in_field,'` from ',p_in_table);\
    prepare stmt from @sqlcmd;\
    execute stmt; \
    deallocate prepare stmt;\
    end;"
    try:
        mysql_exec(sqlquery)
    except Exception,e:
        QtGui.QMessageBox.about(None,"about mysql execute",str(e))

def createFuzzyQuerryProc():
    sqlquery = """create procedure proc_fuzzyQuery(IN p_in_part varchar(64),IN p_in_field varchar(64),IN p_in_table varchar(64)) \
    begin \
    set @sqlcmd = concat('select `',p_in_field,'` from ',p_in_table,' where `',p_in_field,'` like "',p_in_part,'%"');\
    prepare stmt from @sqlcmd;\
    execute stmt; \
    deallocate prepare stmt;\
    end;"""
    try:
        mysql_exec(sqlquery)
    except Exception,e:
        QtGui.QMessageBox.about(None,"about mysql execute",str(e))

def createAttrQueryProc():
    sqlquery = """ create procedure proc_attrQuery(IN p_in_attrs varchar(2000),IN p_in_condition varchar(64),IN p_in_table varchar(64))
    begin \
    set @sqlcmd = concat('select ',p_in_attrs,' from ',p_in_table,' where ',p_in_condition); \
    prepare stmt from @sqlcmd; \
    execute stmt; \
    deallocate prepare stmt;\
    end;
    """
    try:
        mysql_exec(sqlquery)
    except Exception,e:
        QtGui.QMessageBox.about(None,"about mysql execute",str(e))

def CreateAdminUser(name,passwd):
    try:
        sqlquery = "insert into users values(id,'admin','"+name+"','"+encryption(passwd)+"','admin')"
        QtGui.QMessageBox.about(None,"about mysql execute",sqlquery)
        mysql_exec(sqlquery)
    except Exception,e:
        QtGui.QMessageBox.about(None,"about mysql execute",str(e))

def save(model,target=None,index=None):
    if target:
        check_type(dict,target)
        check_type(int,index)
        attr=[ ' `'+i+'`='+str(j)+',' for i,j in target.items()]
        tem = ''.join(attr)[:-1]
        sqlquery = u"update %s set %s  where id= %s"%(model.attr['name'],tem,str(index))
        mysql_exec(sqlquery)
        return
    sqlquery = "create table if not exists %s(id int primary key auto_increment,%s) engine=InnoDB default charset=utf8"%(model.__name__,"".join(model.attr)[:-1])
    #QtGui.QMessageBox.about(None,"about mysql execute",sqlquery)#for test
    mysql_exec(sqlquery)


def initDatabase(model):
    sqlquery = "create database if not exists `%s` default character set utf8;"%(model.attr['name'])
    mysql_exec(sqlquery)
    sqlquery="use `%s`"%(model.attr['name'])
    mysql_exec(sqlquery)


