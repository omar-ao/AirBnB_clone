#!/usr/bin/python3
"""This module contains one class place"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a class Place that is based on BaseModel

    Attributes:
        city_id(str): City id, it will store City.id
        user_id(str): User id, it will store User.id
        name(str): Place name
        description(str): Description of place
        number_rooms(int): Number of roooms
        number_bathrooms(int) Number of bathrooms
        max_guest(int): Maximum number of guests
        price_by_night(int): Price of the place by night
        latitude(float): Latitude of the place
        longitude(float): Longitued of the place
        amenity_ids(list): It will be the list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
