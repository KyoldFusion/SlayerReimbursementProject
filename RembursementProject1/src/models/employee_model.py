from json import JSONEncoder


class Employee:

    def __init__(self, employee_id, first_name, last_name, tier, employee_password, employee_username, email):
        self._employee_id = employee_id
        self._first_name = first_name,
        self._last_name = last_name,
        self._tier = tier
        self._employee_password = employee_password,
        self._employee_username = employee_username,
        self._email = email


class Credentials:

    def __init__(self, employee_password, employee_username):
        self._employee_password = employee_password
        self._employee_username = employee_username


class Manager:

    def __init__(self, employee_id):
        self._employee_id = employee_id


class managersEncoder(JSONEncoder):

    def default(self, manager):
        if isinstance(manager, Manager):
            return manager.__dict__
        else:
            return super().default(manager)


class credentialsEncoder(JSONEncoder):

    def default(self, employee):
        if isinstance(employee, Credentials):
            return employee.__dict__
        else:
            return super().default(self, employee)


class employeeEncoder(JSONEncoder):

    def default(self, employee):
        if isinstance(employee, Employee):
            return employee.__dict__
        else:
            return super().default(self, employee)
