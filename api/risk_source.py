#!/usr/bin/python3

"""
API Endpoint to retrieve travel risk related to country and source
"""

import json
import falcon
from database import Database

class Risk_Source(object):

    def on_get(self, req, resp, country, source):

        db = Database()

        risks = db.fetchall_match_column(
            'travel_risks',
            'source',
            source)

        if country.lower() == 'all':
            
            resp.body = json.dumps(risks)

            resp.content_type = 'application/json'

            resp.status = falcon.HTTP_200

        else:

            for risk in risks:

                if risk['name'] == country:

                    resp.body = json.dumps(risk)

                    resp.content_type = 'application/json'

                    resp.status = falcon.HTTP_200

                    break
