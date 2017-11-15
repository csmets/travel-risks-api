"""
Travel Risks API

This api will return risk data related to selected source and country
"""

import falcon

from risk_source import Risk_Source
from country_risks import Country_Risks

api = falcon.API()
api.add_route('/{country}', Country_Risks())
api.add_route('/{country}/source/{source}', Risk_Source())
