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

    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
