import sqlite3
import json
from models import Customer

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
    """Returns a list of the customers from kennel.db
    """
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)
        customers = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)


def get_single_customer(id):
    """get a single customer by its id
    """
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)


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


def update_customer(id, new_customer):
    """update a customer in the database
    """
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
