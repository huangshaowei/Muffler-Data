# FreeCAD TemplatePyMod module  
# (c) 2007 Juergen Riegel LGPL

# Get the Parameter Group of this module
#ParGrp = App.ParamGet("System parameter:Modules").GetGroup("Test")

# Set the needed information
#ParGrp.SetString("HelpIndex",        "Test/Help/index.html")
#ParGrp.SetString("WorkBenchName",    "Database")

from .controllers import *
from .models import *
from .mysql import *
from .views import *
from .test import *