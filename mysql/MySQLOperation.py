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
   except Exception,e:
       #QtGui.QMessageBox.about(None,"about mysql execute",str(e))
       del cur


def find(model,index):
   check_type(int,index)
   sqlquery = "select * from " + model.attr['name'] + "where id = " + str(index)
   return mysql_exec_res(sqlquery)



def save(model,target=None,index=None):
    if target:
        check_type(dict,target)
        check_type(int,index)
        attr=[ ' `'+i+'`='+str(j)+',' for i,j in target.items()]
        tem = ''.join(attr)[:-1]
        sqlquery = u"update %s set %s  where id= %s"%(model.attr['name'],tem,str(index))
        mysql_exec(sqlquery)
        return
    sqlquery = "create table %s(id int primary key auto_increment,%s) engine=InnoDB default charset=utf8"%(model.__name__,"".join(model.attr)[:-1])
    #QtGui.QMessageBox.about(None,"about mysql execute",sqlquery)#for test
    mysql_exec(sqlquery)


def initDatabase(model):
    sqlquery = "create database `%s` default character set utf8;"%(model.attr['name'])
    mysql_exec(sqlquery)
    sqlquery="use `%s`"%(model.attr['name'])
    mysql_exec(sqlquery)


