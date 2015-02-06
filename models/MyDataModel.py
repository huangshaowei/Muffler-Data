import MyElementParser

class MyDataModel:
    def __init__(self):
        self.node = None
        self.tables = None
        curstom_field = []
        
    def Parser(self,data):
        if data == None:
            return
        p = MyElementTree(data,"utf8")
        self.node = p.parser()
        self.tables = root.getChildren("table")
        pass 