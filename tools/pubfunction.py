

################################ some functions use in global #####################


def check_type(prototype,target):
    if not isinstance(target,prototype):
        raise BaseException("find:index is not a " +str(type(prototype())))
        

def check_empty(target):
    if target.text() == '':
        return True
        

def get_str(target):
    return " '%s'"%(target)