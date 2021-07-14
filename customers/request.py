CUSTOMERS = [
    {
        "id": 2,
        "name": "Kenneth Dedmon",
        "address": "8645 Oak Valley St"
    },
    {
        "id": 3,
        "name": "Lisa Easterling",
        "address": "2 Cardinal Lane"
    },
    {
        "id": 4,
        "name": "Lindsay Walker",
        "address": "323 Ramblewood St",
        "email": "lindsay@walkerjewelry.com"
    },
    {
        "address": "77 Millenium Dr",
        "email": "madelinecrowley@gmail.com",
        "name": "Madeline Crowley",
        "id": 5
    }
]

def get_all_customers():
    """Returns a list of the customers
    """
    return CUSTOMERS

def get_single_customer(id):
    """get a single customer by its id
    """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    """add a customer to the database
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """delete a customer from the database
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
