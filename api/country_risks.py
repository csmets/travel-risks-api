#!/usr/bin/python3

"""
API Endpoint to retrieve travel risk related to country and source
"""

import json
import falcon
from database import Database

class Country_Risks(object):

    def on_get(self, req, resp, country):

        db = Database()

        if country.lower() == 'all':
            country_risk = db.fetchall('travel_risks')

        else:
            country_risk = db.fetch('travel_risks', 'name', country)

        resp.body = json.dumps(country_risk)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200
