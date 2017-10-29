""" Script to return country code from given country name """

import json

def get_country_code(country_name):
    """
    Read country code file and match given country to return country code
    """

    with open('ingester/assets/country-codes.json') as f:

        countries = json.load(f)

        for country in countries:

            if country['name'].lower() == country_name.lower():

                return country['code'].upper()

    return None
