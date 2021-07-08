import src.dao.employee_dao as edao
import src.models.employee_model as Employee
from src.models.employee_model import Credentials
from src.models.employee_model import Manager


def credentials_pass(password, user):
    try:
        x = edao.check_credential(password, user)
        x = Credentials(*x[0]).__dict__
        return x
    except:
        failed = {}
        return failed


def grab_id(username):
    try:
        x = edao.grab_id(username)
        c = []
        for val in x:
            c.append(val)
        return c

    except:
        failed = {}
        return failed


def grab_session(username):
    x = edao.grab_id(username)
    z = []
    for c in x:
        z.append(c)
    return z


def grab_managers():
    x = edao.grab_managers()

    manage_dict = []

    for val in x:
        manage_dict.append(val[0])

    return manage_dict


def grab_managers_specify(username):
    x = edao.grab_managers_bool(username)

    manage_dict = []

    for val in x:
        manage_dict.append(val[0])

    return manage_dict
