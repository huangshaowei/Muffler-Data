import MySQLdb

class MyDataOperation:
    def __init__(self):
        self.server = "127.0.0.1"
        self.port   = "3306"
        self.name   = "root"
        self.password = ""
        sel.conn = MySQLdb.connect(server,name,password)
    def Add(self):
        self.beforeAdd()
        self.addData(conn)
        self.afterAdd()
    def update(self):
        self.beforeUpdate()
        self.updateData(conn)
        self.afterUpdate()
    def delete(self):
        self.beforeDelete()
        self.deleteData(conn)
        self.afterDelete()
    def select(self):
        self.beforeSelect()
        self.SelectData(conn)
        self.afterSelect()
    def create(self):
        pass
    def beforeAdd(self):
        pass
    def addData(self):
        pass
    def afterAdd(self):
        pass
    def beforeUpdate(self):
        pass
    def updateData(self):
        pass
    def afterUpdate(self):
        pass
    def beforeDelete(self):
        pass
    def deleteData(self):
        pass
    def afterDelete(self):
        pass
    def beforeSelect(self):
        pass
    def SelectData(self):
        pass
    def afterSelect(self):
        pass