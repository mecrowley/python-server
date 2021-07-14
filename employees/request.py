EMPLOYEES = [
    {
        "id": 1,
        "name": "Emma Beaton",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Josie Winters",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "John Doe",
        "locationId": 2
    },
    {
        "id": 6,
        "name": "Daryl Jones",
        "locationId": 3
    }
]


def get_all_employees():
    """Returns a list of the employees
    """
    return EMPLOYEES

def get_single_employee(id):
    """get a single employee by its id
    """
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
    """add an employee to the database
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    """delete an employee from the database
    """
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """update an employee in the database
    """
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
