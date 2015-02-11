from .carModels import *
from .projectModels import *
from .databaseModels import *

Models=[CarModels,Project]

################class MyModels manager the Models' establish and use ############
class ModelsManager:
    def __init__(self,path):
        self.path = path
        self.MgrModels = []
        pass
    def Establish(self):
        global Models
        if self.MgrModels:
            return
        model = None
        for mol in Models:
            model = mol(model)
            self.MgrModels += [model]
        if model:
            database = Database(model)
            database.Parser(self.path)
            database.initialise()
        else:
            raise BaseException("database is not ready yet")
    def getCorrespondenceModel(self,name):
        for model in self.MgrModels:
            if model.__name__ == name:
                return model