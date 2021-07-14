LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "229 Emory Drive"
    },
    {
        "name": "Nashville East",
        "address": "500 Main St",
        "id": 3
    }
]


def get_all_locations():
    """Returns a list of the locations
    """
    return LOCATIONS

def get_single_location(id):
    """get a single location by its id
    """
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location

def create_location(location):
    """add a location to the database
    """
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    """delete a location from the database
    """
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """update a location in the database
    """
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
