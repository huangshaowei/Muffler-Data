from ..models import *
from ..views import *
from ..controllers import *
import os
def run():
    try:
        user = Users()
        car = CarModels(user)
        project = Projects(car)
        database = Database(project)
        database.Parser(os.getcwd()+"\\..\\Mod\\Database\\MufflerData\\config\\database.xml")
        database.initialise()
    except Exception,e:
        print e
    return [user,car,project]


def testModelsManager():
    mol = ModelsManager(os.getcwd()+"\\..\\Mod\\Database\\MufflerData\\config\\database.xml")
    mol.Establish()
    project = mol.getCorrespondenceModel("projects")
    user    = mol.getCorrespondenceModel("users")
    testProject(user)
    

def testManagerController():
    M = ManagerController()
    M.ViewPanel.show()


def testProject(p):
    for attr in p.attr:
        print attr
    for field in p.curstom_field:
        print field



def testMySQLOper():
    pass

def testProjectController():
    pass
    

def test():
    print __file__
    print __line__


def testModels():
    pass

def testDatabaseController():
    pass
    
################################################
